#!/usr/bin/env python3

import html
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
GENERATED = ROOT / "_generated"


def link_list(links):
    if not links:
        return ""
    pieces = []
    for link in links:
        label = html.escape(link["label"])
        url = html.escape(link["url"], quote=True)
        pieces.append(f'<a class="pill-link" href="{url}">{label}</a>')
    return "\n".join(pieces)


def render_publications():
    data = json.loads((ROOT / "data" / "publications.json").read_text())
    sections = []
    for group in data["groups"]:
        sections.append(f'## {html.escape(group["label"])}\n')
        sections.append('<div class="publication-list">\n')
        for item in group["items"]:
            title = html.escape(item["title"])
            authors = html.escape(item.get("authors", ""))
            year = html.escape(item.get("year", ""))
            venue = html.escape(item.get("venue", ""))
            links = link_list(item.get("links", []))
            meta_bits = [bit for bit in [year, venue] if bit]
            meta = " | ".join(meta_bits)
            sections.append(
                '<article class="publication-item">\n'
                f'  <h3>{title}</h3>\n'
                f'  <p class="pub-authors">{authors}</p>\n'
                f'  <p class="pub-meta">{meta}</p>\n'
                f'  <div class="link-row">{links}</div>\n'
                '</article>\n'
            )
        sections.append("</div>\n")
    (GENERATED / "research.md").write_text("\n".join(sections))


def render_repos():
    data = json.loads((ROOT / "data" / "repos.json").read_text())
    sections = ['<div class="repo-grid">\n']
    for repo in data["featured"]:
        title = html.escape(repo["title"])
        url = html.escape(repo["url"], quote=True)
        description = html.escape(repo["description"])
        tags = " ".join(f"<span>{html.escape(tag)}</span>" for tag in repo.get("tags", []))
        sections.append(
            '<article class="repo-card">\n'
            f'  <h3><a href="{url}">{title}</a></h3>\n'
            f'  <p>{description}</p>\n'
            f'  <div class="tag-row">{tags}</div>\n'
            f'  <a class="text-link" href="{url}">View repository</a>\n'
            '</article>\n'
        )
    sections.append("</div>\n")
    (GENERATED / "repos.md").write_text("\n".join(sections))


def main():
    GENERATED.mkdir(exist_ok=True)
    render_publications()
    render_repos()


if __name__ == "__main__":
    main()
