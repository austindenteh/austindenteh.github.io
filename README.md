# Augustine Denteh Website

Quarto source for the professional website at `austindenteh.com`.

## Local Preview

```bash
quarto preview
```

## Build

```bash
quarto render
```

The rendered site is written to `_site/`.

## Main Content Files

- `index.qmd`: homepage
- `research.qmd`: research page
- `resources.qmd`: resources, code, data, and workshop materials page
- `teaching.qmd`: teaching page
- `media.qmd`: media coverage, videos, public engagement, and profile links
- `methods-matter.qmd`: Methods Matter index, listing posts newest first
- `methods-matter/*/index.qmd`: editable Methods Matter posts and their supporting assets
- `blog.qmd`: draft blog page, currently hidden from the rendered site
- `cv.qmd`: CV page
- `data/publications.json`: structured publications, working papers, and works in progress
- `data/resources.json`: structured resources, code, data, and workshop materials
- `assets/cv/CV_denteh.pdf`: current CV PDF
- `assets/img/headshot.jpg`: web-optimized headshot

## Deployment

The GitHub Actions workflow in `.github/workflows/publish.yml` renders the Quarto site and deploys `_site/` to GitHub Pages. In the GitHub repository settings, set Pages to deploy from GitHub Actions.

The custom domain is `austindenteh.com`. The root `CNAME` file is included in the Quarto resources so GitHub Pages preserves the custom-domain setting during deploys.

## Methods Matter Posts

Each post lives in its own folder under `methods-matter/`, with an `index.qmd`,
bibliography, and the figures and media it uses. The listing uses the post's
title, date, and description automatically. Keep the folder name stable when
editing a published post so its URL stays the same. For substantial revisions,
add `date-modified` while preserving the original publication date.

The first post was adapted from the final Quarto source in
`pre_trends_did/blogs/01-what-can-we-learn/`. The website copy preserves the prose;
only publishing metadata, media paths, and loading attributes were adapted.
Keep later author edits and this website copy synchronized before deploying.
