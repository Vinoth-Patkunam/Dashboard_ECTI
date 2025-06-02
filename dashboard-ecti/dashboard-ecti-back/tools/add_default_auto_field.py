import sys
from pathlib import Path
import re

def patch_file(path: Path):
    text = path.read_text(encoding='utf-8')
    lines = text.splitlines()
    out = []
    i = 0
    while i < len(lines):
        line = lines[i]
        out.append(line)
        # detect class Meta declaration
        if re.match(r"^\s*class\s+Meta\s*:\s*", line):
            # compute indent for inside Meta
            indent = re.match(r"^(\s*)", lines[i+1] if i+1 < len(lines) else line).group(1)
            # default indent is indent + 4 spaces
            default_indent = re.match(r"^(\s*)", line).group(1) + '    '
            # insert default_auto_field if not already present
            # look ahead in Meta block to ensure not already present
            j = i+1
            present = False
            while j < len(lines) and (lines[j].startswith(default_indent) or lines[j].strip() == ''):
                if 'default_auto_field' in lines[j]:
                    present = True
                    break
                j += 1
            if not present:
                out.append(f"{default_indent}default_auto_field = None")
        i += 1
    # write back
    path.write_text("\n".join(out) + "\n", encoding='utf-8')
    print(f"Updated {path}")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: add_default_auto_field.py <file1> [<file2> ...]")
        sys.exit(1)
    for fp in sys.argv[1:]:
        patch_file(Path(fp))
