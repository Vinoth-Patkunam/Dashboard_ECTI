# api/views_stats.py
from typing import List, Dict, Any
from django.http import JsonResponse
from django.db import connections, close_old_connections
from django.views.decorators.http import require_GET

# --- Config ---
DB_ALIAS = "tablecti"             
AFFECTATIONS_TABLE = "affectations"   
KMS_TABLE          = "tmplignedekms"  

# --- Helpers DB ---
def _conn():
    return connections[DB_ALIAS]

def _table_names_lower() -> set[str]:
    names = _conn().introspection.table_names()
    return {n.lower() for n in names}

def _table_exists(name: str, names_lower: set[str] | None = None) -> bool:
    if names_lower is None:
        names_lower = _table_names_lower()
    return name.lower() in names_lower

def _year_expr(col: str) -> str:
    vendor = _conn().vendor  
    if vendor == "mysql":
        return f"YEAR({col})"
    if vendor == "sqlite":
        return f"strftime('%Y', {col})"
    return f"EXTRACT(YEAR FROM {col})"

def _affectations_par_departement() -> List[Dict[str, Any]]:
    if not _table_exists(AFFECTATIONS_TABLE):
        return []
    sql = f"""
        SELECT Depar AS depar, COUNT(*) AS total
        FROM {AFFECTATIONS_TABLE}
        GROUP BY Depar
        ORDER BY Depar
    """
    with _conn().cursor() as cur:
        cur.execute(sql)
        return [{"depar": r[0], "total": int(r[1] or 0)} for r in cur.fetchall()]

def _affectations_par_annee() -> List[Dict[str, Any]]:
    if not _table_exists(AFFECTATIONS_TABLE):
        return []
    year = _year_expr("DatOuvL")  
    sql = f"""
        SELECT {year} AS annee, COUNT(*) AS total
        FROM {AFFECTATIONS_TABLE}
        WHERE DatOuvL IS NOT NULL
        GROUP BY annee
        ORDER BY annee
    """
    with _conn().cursor() as cur:
        cur.execute(sql)
        return [{"annee": str(r[0]), "total": int(r[1] or 0)} for r in cur.fetchall()]

def _km_par_annee() -> List[Dict[str, Any]]:
    if not _table_exists(KMS_TABLE):
        return []
    year = _year_expr("jour")    
    sql = f"""
        SELECT {year} AS annee, SUM(nbkm) AS km
        FROM {KMS_TABLE}
        WHERE jour IS NOT NULL
        GROUP BY annee
        ORDER BY annee
    """
    with _conn().cursor() as cur:
        cur.execute(sql)
        return [{"annee": str(r[0]), "km": float(r[1] or 0)} for r in cur.fetchall()]


@require_GET
def stats_affectations_par_departement(request):
    data = _affectations_par_departement()
    close_old_connections()
    return JsonResponse(data, safe=False)

@require_GET
def stats_affectations_par_annee(request):
    data = _affectations_par_annee()
    close_old_connections()
    return JsonResponse(data, safe=False)

@require_GET
def stats_km_par_annee(request):
    data = _km_par_annee()
    close_old_connections()
    return JsonResponse(data, safe=False)

# --- Endpoint unique pour le dashboard (1 appel HTTP, 1 connexion MySQL) ---
@require_GET
def stats_dashboard_all(request):
    payload = {
        "dep": _affectations_par_departement(),
        "aff": _affectations_par_annee(),
        "km":  _km_par_annee(),
    }
    close_old_connections()
    return JsonResponse(payload, safe=False)

# --- Debug : liste les tables visibles pour chaque connexion DB ---
@require_GET
def stats_debug_tables(request):
    out: Dict[str, Any] = {}
    for alias in connections.databases.keys():
        try:
            conn = connections[alias]
            names = conn.introspection.table_names()
            out[alias] = {"vendor": conn.vendor, "tables": names, "count": len(names)}
        except Exception as e:
            out[alias] = {"error": str(e)}
    return JsonResponse(out)
