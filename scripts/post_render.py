#!/usr/bin/env python3

import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "_site"
PAGES = ["cv", "research", "resources", "teaching"]
DISABLED_PAGES = ["talks", "notes", "blog", "code"]


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


def main():
    if not SITE.exists():
        return
    copy_extensionless_pages()
    remove_disabled_pages()
    (SITE / ".nojekyll").write_text("")


if __name__ == "__main__":
    main()
