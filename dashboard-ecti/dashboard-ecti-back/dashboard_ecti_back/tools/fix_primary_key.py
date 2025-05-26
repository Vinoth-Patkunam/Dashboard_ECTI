# tools/fix_models.py
from pathlib import Path
import sys, unicodedata

def fix_file(p: Path):
    raw = p.read_bytes()

    # 1) On tente une passe de « mojibake fix » :
    try:
        # on lit tout en UTF-8 (génère "FiliÃ¨re" si c'était mal encodé)
        s = raw.decode('utf-8')
        # on ré-encode en latin1 (en ignorant les inencodables) puis re-décode en UTF-8
        s = s.encode('latin1', errors='ignore').decode('utf-8', errors='ignore')
    except UnicodeDecodeError:
        # si ça échoue, on tombe en latin1 brut (ignore les bytes invalides)
        s = raw.decode('latin1', errors='ignore')

    # 2) (Optionnel) décomposer + retirer tous les diacritiques
    s = unicodedata.normalize('NFKD', s)
    s = ''.join(ch for ch in s if not unicodedata.combining(ch))

    # 3) Uniformiser les tabulations → 4 espaces
    s = s.replace('\t', ' ' * 4)

    # 4) Réécrire en UTF-8 pur
    p.write_text(s, encoding='utf-8')
    print(f"✓ fix_mojibake & normalize dans {p.name}")

if __name__ == '__main__':
    for fp in sys.argv[1:]:
        fix_file(Path(fp))
