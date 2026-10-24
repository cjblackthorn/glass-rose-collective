#!/usr/bin/env python3
"""Source-level Jekyll layout and accessibility checks; not a rendered-site audit."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

def front_matter_layout(content):
    if not content.startswith("---\n"):
        return None
    boundary = content.find("\n---", 4)
    if boundary < 0:
        return None
    frontmatter = content[4:boundary]
    match = re.search(r"(?m)^layout:\s*([\w-]+)\s*$", frontmatter)
    return match.group(1) if match else None

def main():
    errors = []
    layout = (ROOT / "_layouts/default.html").read_text(encoding="utf-8")
    css = (ROOT / "assets/css/styles.scss").read_text(encoding="utf-8")
    if layout.count('id="main-content"') != 1 or 'tabindex="-1"' not in layout:
        errors.append("Default layout must have one focusable main-content landmark")
    if '<a class="grc-skip-link" href="#main-content">' not in layout:
        errors.append("Skip navigation must be present in default layout")
    if layout.index("grc-skip-link") > layout.index("include header.html"):
        errors.append("Skip navigation must precede repeated site header")
    for marker in (".grc-skip-link:focus", ":focus-visible", "prefers-reduced-motion"):
        if marker not in css:
            errors.append(f"Missing accessibility style: {marker}")

    checked = 0
    for file in ROOT.rglob("*"):
        if not file.is_file() or file.suffix.lower() not in (".html", ".md"):
            continue
        if ".git" in file.parts:
            continue
        content = file.read_text(encoding="utf-8")
        checked += 1
        for include in re.findall(r"{%[-]?\s*include\s+([\w./-]+)", content):
            if not (ROOT / "_includes" / include).is_file():
                errors.append(f"{file.relative_to(ROOT)}: missing include '{include}'")
        found = front_matter_layout(content)
        if found and not (ROOT / "_layouts" / f"{found}.html").is_file():
            errors.append(f"{file.relative_to(ROOT)}: missing layout '{found}'")

    if errors:
        print("Glass Rose Collective source validation FAILED")
        for error in errors:
            print(" - " + error)
        raise SystemExit(1)
    print(f"PASS: checked {checked} HTML/Markdown sources, shared navigation/focus rules, layout/include references.")

if __name__ == "__main__":
    main()
