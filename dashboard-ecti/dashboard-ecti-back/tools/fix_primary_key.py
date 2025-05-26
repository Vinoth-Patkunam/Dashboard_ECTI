#!/usr/bin/env python3
# tools/fix_primary_key.py
import sys
from pathlib import Path
import re

def main(path):
    text = Path(path).read_text(encoding="utf8")
    lines = text.splitlines()
    out   = []
    in_class = False
    pk_done  = False

    for line in lines:
        # Quand on entre dans une classe Django
        if re.match(r'class\s+\w+\(models\.Model\):', line):
            in_class = True
            pk_done  = False
            out.append(line)
            continue

        # Dès qu’on est dans une classe, on cherche la première définition de champ
        if in_class and not pk_done and re.match(r'\s+\w+\s*=\s*models\.\w+', line):
            # On insère , primary_key=True juste avant la fin de la parenthèse
            line = re.sub(r'\)$', r', primary_key=True)', line)
            pk_done = True

        # Si on sort de la classe (on atteint Meta ou une ligne vide), on réinitialise
        if in_class and (line.strip().startswith('class Meta') or line.strip() == ''):
            in_class = False

        out.append(line)

    Path(path).write_text('\n'.join(out) + '\n', encoding="utf8")
    print(f"  ✓ primary_key fixé dans {path}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: fix_primary_key.py chemin/vers/fichier.py")
        sys.exit(1)
    main(sys.argv[1])
