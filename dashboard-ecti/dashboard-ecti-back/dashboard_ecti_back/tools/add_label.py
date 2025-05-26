# tools/add_label.py
from pathlib import Path
import sys, re

def patch_file(path: Path, label: str):
    # Lire le fichier (UTF-8 avec BOM ou fallback latin1)
    try:
        raw = path.read_text(encoding='utf-8-sig')
    except UnicodeDecodeError:
        raw = path.read_text(encoding='latin-1')

    lines = raw.splitlines()
    out = []

    for line in lines:
        # 1) Supprimer toute app_label existante
        if re.match(r"^\s*app_label\s*=" , line):
            continue

        # 2) Repérer 'class Meta' et injecter directement la ligne app_label juste après
        m = re.match(r"^(\s*)class\s+Meta\b", line)
        if m:
            out.append(line)
            indent = m.group(1) + '    '
            out.append(f"{indent}app_label = '{label}'")
            continue

        # 3) Conserver les autres lignes
        out.append(line)

    # Réécrire le fichier en UTF-8
    path.write_text('\n'.join(out) + '\n', encoding='utf-8')
    print(f"✓ added app_label='{label}' to {path.name}")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: add_label.py <fichier> <app_label>")
        sys.exit(1)
    patch_file(Path(sys.argv[1]), sys.argv[2])