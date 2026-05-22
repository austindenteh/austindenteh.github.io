# Augustine Denteh Website

Quarto source for the professional website at `austindenteh.github.io`.

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
- `code.qmd`: code and repositories page
- `teaching.qmd`: teaching page
- `talks.qmd`: talks and workshops page
- `notes.qmd`: notes page
- `cv.qmd`: CV page
- `data/publications.json`: structured publications, working papers, and works in progress
- `data/repos.json`: featured public repositories
- `assets/cv/CV_denteh.pdf`: current CV PDF
- `assets/img/headshot.jpg`: web-optimized headshot

## Deployment

The GitHub Actions workflow in `.github/workflows/publish.yml` renders the Quarto site and deploys `_site/` to GitHub Pages. In the GitHub repository settings, set Pages to deploy from GitHub Actions.

The custom domain `austindenteh.com` should be added later, after this GitHub Pages version is reviewed. At that point, update `site-url`, add a `CNAME` file containing `austindenteh.com`, and then change DNS.
