#!/usr/bin/env python3

import hashlib
import re
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "_site"
PAGES = ["cv", "research", "resources", "teaching", "media"]
DISABLED_PAGES = ["talks", "notes", "blog", "code"]
BOOTSTRAP_ICONS_LINK_RE = re.compile(
    r'^\s*<link href="[^"]*site_libs/bootstrap/bootstrap-icons\.css" rel="stylesheet">\s*\n?',
    re.MULTILINE,
)
BOOTSTRAP_ICON_CLASS_RE = re.compile(r'class="[^"]*\bbi\b')


def rewrite_for_directory_page(html_text):
    replacements = {
        'href="site_libs/': 'href="../site_libs/',
        'src="site_libs/': 'src="../site_libs/',
        'href="styles.css"': 'href="../styles.css"',
        'href="assets/': 'href="../assets/',
        'src="assets/': 'src="../assets/',
        'href="index.html"': 'href="../index.html"',
        'href="./index.html"': 'href="../index.html"',
        'href="./"': 'href="../index.html"',
    }
    for page in PAGES:
        replacements[f'href="{page}.html"'] = f'href="../{page}.html"'
        replacements[f'href="./{page}.html"'] = f'href="../{page}.html"'

    for old, new in replacements.items():
        html_text = html_text.replace(old, new)
    return html_text


def copy_extensionless_pages():
    for page in PAGES:
        src = SITE / f"{page}.html"
        if not src.exists():
            continue
        dest_dir = SITE / page
        dest_dir.mkdir(exist_ok=True)
        text = src.read_text()
        (dest_dir / "index.html").write_text(rewrite_for_directory_page(text))


def remove_disabled_pages():
    for page in DISABLED_PAGES:
        html_file = SITE / f"{page}.html"
        page_dir = SITE / page
        if html_file.exists():
            html_file.unlink()
        if page_dir.exists():
            shutil.rmtree(page_dir)


def strip_unused_bootstrap_icons():
    html_files = list(SITE.rglob("*.html"))
    if any(BOOTSTRAP_ICON_CLASS_RE.search(path.read_text()) for path in html_files):
        return

    for path in html_files:
        text = path.read_text()
        path.write_text(BOOTSTRAP_ICONS_LINK_RE.sub("", text))

    bootstrap_dir = SITE / "site_libs" / "bootstrap"
    for asset in bootstrap_dir.glob("bootstrap-icons.*"):
        asset.unlink()


def fingerprint_custom_css():
    css_file = SITE / "styles.css"
    if not css_file.exists():
        return

    digest = hashlib.sha256(css_file.read_bytes()).hexdigest()[:12]
    fingerprinted_name = f"styles-{digest}.css"
    fingerprinted_file = SITE / fingerprinted_name
    shutil.copy2(css_file, fingerprinted_file)

    for path in SITE.rglob("*.html"):
        text = path.read_text()
        text = text.replace('href="styles.css"', f'href="{fingerprinted_name}"')
        text = text.replace('href="../styles.css"', f'href="../{fingerprinted_name}"')
        path.write_text(text)


def main():
    if not SITE.exists():
        return
    copy_extensionless_pages()
    remove_disabled_pages()
    strip_unused_bootstrap_icons()
    fingerprint_custom_css()
    (SITE / ".nojekyll").write_text("")


if __name__ == "__main__":
    main()
