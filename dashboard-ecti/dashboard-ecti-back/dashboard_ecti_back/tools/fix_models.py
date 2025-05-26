# tools/fix_models.py
from pathlib import Path
import sys, unicodedata

def fix_file(p: Path):
    raw = p.read_bytes()
    try:
        s = raw.decode('utf-8')
        s = s.encode('latin1', errors='ignore').decode('utf-8', errors='ignore')
    except:
        s = raw.decode('latin1', errors='ignore')
    # (Optionnel) enlever diacritiques
    s = unicodedata.normalize('NFKD', s)
    s = ''.join(c for c in s if not unicodedata.combining(c))
    # tabs → 4 espaces
    s = s.replace('\t', ' ' * 4)
    p.write_text(s, encoding='utf-8')
    print(f"✓ fix_models → {p.name}")

if __name__ == '__main__':
    for fp in sys.argv[1:]:
        fix_file(Path(fp))
