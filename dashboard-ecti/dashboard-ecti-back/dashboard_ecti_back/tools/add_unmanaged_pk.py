#!/usr/bin/env python3
# scripts/add_unmanaged_pk.py

import re, sys

# repère la ligne de début d'une classe modèle
CLASS_RE      = re.compile(r'^(\s*)class\s+(\w+)\(models\.Model\):')
# repère "class Meta:"
META_RE       = re.compile(r'^(\s*)class\s+Meta:')
# repère la ligne "managed = False"
MANAGED_FALSE = re.compile(r'^\s*managed\s*=\s*False')
# repère un champ primary_key
PKFIELD_RE    = re.compile(r'primary_key\s*=\s*True')

def process_file(path):
    lines = open(path, encoding='utf-8').read().splitlines()
    out   = []
    in_model       = False
    indent         = ''
    saw_managed    = False
    saw_pk         = False

    for line in lines:
        # début d'une classe Model ?
        m = CLASS_RE.match(line)
        if m:
            in_model    = True
            indent      = m.group(1)
            saw_managed = False
            saw_pk      = False

        # si on est dans un modèle, on regarde les flags
        if in_model:
            if MANAGED_FALSE.match(line):
                saw_managed = True
            if PKFIELD_RE.search(line):
                saw_pk = True

        # juste avant "class Meta:", si c'est un modèle unmanaged sans PK
        mm = META_RE.match(line)
        if in_model and mm and saw_managed and not saw_pk:
            # on vous demande la colonne de clé primaire
            table = re.match(r".*db_table\s*=\s*'([^']+)'", "\n".join(lines[:len(out)+1]))
            tblname = table.group(1) if table else '?'
            col = input(f"[{path} → modèle '{tblname}'] nom de la colonne PK (PRI) ? ")
            # on injecte le champ juste avant le Meta
            field = (
                f"{indent}    "
                f"id = models.AutoField(db_column='{col}', primary_key=True)"
            )
            out.append(field)
            saw_pk = True

        out.append(line)

        # si on passe la Meta, on sort du modèle
        if in_model and mm:
            in_model = False

    # réécrit le fichier
    with open(path, 'w', encoding='utf-8') as f:
        f.write("\n".join(out) + "\n")
    print(f"  traité {path}")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python add_unmanaged_pk.py fichier1.py [fichier2.py ...]")
        sys.exit(1)
    for fn in sys.argv[1:]:
        process_file(fn)
