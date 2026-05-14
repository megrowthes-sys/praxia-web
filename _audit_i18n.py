"""Extract ALL user-visible Spanish strings from a page and report which are
NOT in praxia-i18n.js dictionary yet.

Usage: python3 _audit_i18n.py <page.html>
"""
from bs4 import BeautifulSoup, NavigableString
from pathlib import Path
import re, sys

def extract_strings(path):
    html = Path(path).read_text(encoding="utf-8")
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()

    out = []
    for txt in soup.find_all(string=True):
        if not isinstance(txt, NavigableString):
            continue
        s = str(txt).strip()
        s = re.sub(r"\s+", " ", s)
        if not s:
            continue
        if 1 < len(s) < 1000:
            out.append(s)

    for tag in soup.find_all(True):
        for attr in ("placeholder", "alt", "title", "aria-label"):
            v = tag.get(attr)
            if v:
                v = re.sub(r"\s+", " ", v.strip())
                if v:
                    out.append(v)
        if tag.name in ("input", "button"):
            v = tag.get("value")
            if v:
                v = re.sub(r"\s+", " ", v.strip())
                if v:
                    out.append(v)
        if tag.name == "option":
            t = tag.get_text(strip=True)
            if t:
                out.append(t)

    seen = set()
    uniq = []
    for s in out:
        if s in seen:
            continue
        seen.add(s)
        uniq.append(s)
    return uniq


def is_translatable(s):
    if len(s) < 2:
        return False
    if all(c.isdigit() or c in ' +-€%·.,/()€mhk' for c in s):
        return False
    if ' ' not in s and re.match(r'^[A-Za-z0-9._/+#-]+$', s):
        return False
    return True


def is_in_dict(s, i18n):
    cand1 = "'" + s.replace("\\", "\\\\").replace("'", "\\'") + "'"
    cand2 = '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'
    return cand1 in i18n or cand2 in i18n


def main():
    target = sys.argv[1] if len(sys.argv) > 1 else "colaboradores.html"
    i18n = Path("praxia-i18n.js").read_text(encoding="utf-8")
    strings = extract_strings(target)
    trans = [s for s in strings if is_translatable(s)]
    missing = [s for s in trans if not is_in_dict(s, i18n)]

    print(f"== {target} ==")
    print(f"Total visible strings: {len(strings)}")
    print(f"Translatable: {len(trans)}")
    print(f"NOT in dict: {len(missing)}")
    print()
    for i, s in enumerate(missing, 1):
        print(f"  [{i}] {s}")


if __name__ == "__main__":
    main()
