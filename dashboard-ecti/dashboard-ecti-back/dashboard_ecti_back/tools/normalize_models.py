# tools/normalize_models.py
import re, sys
from pathlib import Path

def normalize(path: Path):
    raw = path.read_bytes()
    # 1) On décode en latin1 pour pouvoir attraper tous les octets
    txt = raw.decode('latin1')
    # 2) On retire les BOM résiduels
    txt = txt.lstrip('\ufeff')
    # 3) On supprime tous les caractères non imprimables (hors LF/CR/Tab)
    txt = re.sub(r'[^\x09\x0A\x0D\x20-\x7E]', '', txt)
    # 4) On uniformise les tabs en 4 espaces
    txt = txt.expandtabs(4)
    # 5) On supprime les espaces en fin de ligne
    lines = [l.rstrip() for l in txt.splitlines()]
    # 6) On réécrit en UTF-8 sans BOM
    path.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(f"✓ normalized {path.name}")

if __name__ == '__main__':
    for fp in sys.argv[1:]:
        normalize(Path(fp))
