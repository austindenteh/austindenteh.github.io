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
- `blog.qmd`: draft blog page, currently hidden from the rendered site
- `cv.qmd`: CV page
- `data/publications.json`: structured publications, working papers, and works in progress
- `data/resources.json`: structured resources, code, data, and workshop materials
- `assets/cv/CV_denteh.pdf`: current CV PDF
- `assets/img/headshot.jpg`: web-optimized headshot

## Deployment

The GitHub Actions workflow in `.github/workflows/publish.yml` renders the Quarto site and deploys `_site/` to GitHub Pages. In the GitHub repository settings, set Pages to deploy from GitHub Actions.

The custom domain is `austindenteh.com`. The root `CNAME` file is included in the Quarto resources so GitHub Pages preserves the custom-domain setting during deploys.
