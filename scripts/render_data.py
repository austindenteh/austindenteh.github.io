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


def render_author(author):
    if isinstance(author, str):
        return html.escape(author)
    name = html.escape(author["name"])
    url = author.get("url")
    if not url:
        return name
    return f'<a href="{html.escape(url, quote=True)}">{name}</a>'


def render_authors(authors):
    if not authors:
        return ""
    if isinstance(authors, str):
        return html.escape(authors)

    rendered = [render_author(author) for author in authors]
    if len(rendered) == 1:
        return rendered[0]
    if len(rendered) == 2:
        return f"{rendered[0]} and {rendered[1]}"
    return f'{", ".join(rendered[:-1])}, and {rendered[-1]}'


def render_venue(item):
    venue = item.get("venue", "")
    if not venue:
        return ""

    journal = item.get("journal")
    if not journal:
        return html.escape(venue)

    prefix, separator, suffix = venue.partition(journal)
    if not separator:
        raise ValueError(f'Journal "{journal}" is not present in venue "{venue}"')
    return (
        f'{html.escape(prefix)}'
        f'<strong class="pub-journal">{html.escape(journal)}</strong>'
        f'{html.escape(suffix)}'
    )


def render_publications():
    data = json.loads((ROOT / "data" / "publications.json").read_text())
    sections = []
    for group in data["groups"]:
        sections.append(f'## {html.escape(group["label"])}\n')
        sections.append('<div class="publication-list">\n')
        for item in group["items"]:
            title = html.escape(item["title"])
            authors = render_authors(item.get("authors", ""))
            year = html.escape(item.get("year", ""))
            venue = render_venue(item)
            links = link_list(item.get("links", []))
            meta_bits = [bit for bit in [year, venue] if bit]
            meta = " | ".join(meta_bits)
            meta_html = f'  <p class="pub-meta">{meta}</p>\n' if meta else ""
            links_html = f'  <div class="link-row">{links}</div>\n' if links else ""
            sections.append(
                '<article class="publication-item">\n'
                f'  <h3>{title}</h3>\n'
                f'  <p class="pub-authors">{authors}</p>\n'
                f'{meta_html}'
                f'{links_html}'
                '</article>\n'
            )
        sections.append("</div>\n")
    (GENERATED / "research.md").write_text("\n".join(sections))


def render_resources():
    data = json.loads((ROOT / "data" / "resources.json").read_text())
    sections = []
    for group in data["groups"]:
        items = group.get("items", [])
        if not items:
            continue
        sections.append(f'## {html.escape(group["label"])}\n')
        sections.append('<div class="repo-grid">\n')
        for item in items:
            title = html.escape(item["title"])
            url = html.escape(item["url"], quote=True)
            description = html.escape(item["description"])
            tags = " ".join(f"<span>{html.escape(tag)}</span>" for tag in item.get("tags", []))
            sections.append(
                '<article class="repo-card">\n'
                f'  <h3><a href="{url}">{title}</a></h3>\n'
                f'  <p>{description}</p>\n'
                f'  <div class="tag-row">{tags}</div>\n'
                f'  <a class="text-link" href="{url}">View resource</a>\n'
                '</article>\n'
            )
        sections.append("</div>\n")
    (GENERATED / "resources.md").write_text("\n".join(sections))


def main():
    GENERATED.mkdir(exist_ok=True)
    render_publications()
    render_resources()


if __name__ == "__main__":
    main()
