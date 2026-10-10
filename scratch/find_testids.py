import glob
import re

matches = set()
for f in glob.glob(".venv/Lib/site-packages/streamlit/static/static/js/*.js"):
    content = open(f, encoding="utf-8", errors="ignore").read()
    testids = re.findall(r'data-testid="([^"]+)"', content)
    matches.update(testids)
    aria_labels = re.findall(r'aria-label="([^"]+)"', content)
    for a in aria_labels:
        if "sidebar" in a.lower() or "menu" in a.lower() or "close" in a.lower() or "open" in a.lower():
            print("ARIA:", a)

print("Matching testids:")
for m in sorted(matches):
    if any(k in m.lower() for k in ["sidebar", "collapse", "expand", "header", "chevron"]):
        print("TESTID:", m)
