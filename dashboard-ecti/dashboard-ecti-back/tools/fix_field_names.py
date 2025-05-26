#!/usr/bin/env python3
# tools/fix_field_names.py

import sys, re, unicodedata
from pathlib import Path

def repair_mojibake(s: str) -> str:
    # si on a un « Ã » ou « Â », on force la passe inverse latin1→utf8
    try:
        return s.encode('latin1').decode('utf-8')
    except Exception:
        return s

def slugify(name: str) -> str:
    # 1) réparer d'abord le mojibake
    s = repair_mojibake(name)
    # 2) normaliser pour exploser les diacritiques
    s = unicodedata.normalize('NFKD', s)
    # 3) virer tout ce qui est combining (accents, tilde, etc.)
    s = ''.join(ch for ch in s if not unicodedata.combining(ch))
    # 4) transformer toute séquence non-alnum en underscore
    s = re.sub(r'[^0-9A-Za-z]+', '_', s)
    # 5) compactage des multiples underscore, minuscules
    s = re.sub(r'_+', '_', s).strip('_').lower()
    # 6) si démarre par chiffre, préfixer par underscore
    if re.match(r'^[0-9]', s):
        s = '_' + s
    return s

# On capte l’attribut, le field type et le db_column
FIELD_RE = re.compile(
    r'^(?P<indent>\s*)(?P<attr>\w+)\s*=\s*models\.\w+\(.*db_column\s*=\s*[\'"](?P<col>[^\'"]+)[\'"]'
)

def fix_file(path: Path):
    text = path.read_text(encoding='utf-8')
    out = []
    for ln in text.splitlines():
        m = FIELD_RE.match(ln)
        if m:
            indent = m.group('indent')
            col    = m.group('col')
            new_attr = slugify(col)
            # on remplace l'ancien nom par le nouveau
            ln = ln.replace(f"{indent}{m.group('attr')}", f"{indent}{new_attr}", 1)
        out.append(ln)
    path.write_text("\n".join(out)+"\n", encoding='utf-8')
    print(f"✓ fix_field_names → {path.name}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: fix_field_names.py <fichier1.py> [<fichier2.py> ...]")
        sys.exit(1)
    for fp in sys.argv[1:]:
        fix_file(Path(fp))
