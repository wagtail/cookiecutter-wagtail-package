# Documentation & tooling

This page explains how the project's documentation is built, how to write and maintain it, and the reasoning behind the tooling choices.

## How the docs are built

The documentation site is built with [MkDocs](https://www.mkdocs.org/) using the [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) theme, and published to [GitHub Pages](https://pages.github.com/). Source files live in `docs/` at the repository root, and the site config is `mkdocs.yml`.

Two commands drive local development:

```sh
just docs-build    # Build the site into `site/`, failing on any warning (strict mode).
just docs-serve    # Build and serve the site at http://localhost:8001 with live reload.
```

On every push to `main`, CI builds the documentation in [strict mode](https://www.mkdocs.org/user-guide/configuration/#strict) and deploys the result to GitHub Pages.

### Why MkDocs over Sphinx

| Tool | MkDocs | Sphinx | Zensical |
|---|---|---|---|
| Language | Markdown | reStructuredText / Markdown | Markdown |
| Python API reference | [mkdocstrings](https://mkdocstrings.com/) | [autodoc](https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html) | Marketing-oriented |
| Default theme quality | Material (excellent, modern) | Read the Docs / Furo | Hosted |
| Configuration burden | Low, YAML-only | High (`conf.py`, reStructuredText quirks) | Low (no self-hosting) |
| Ecosystem maturity | Large plugin set | Largest, mature | Small |

MkDocs was chosen because the Material theme removes most of the effort required to get a polished, responsive site, and markdown is easier for contributors to write correctly than reStructuredText. `mkdocstrings` provides first-class extraction of API references from Python docstrings, matching Sphinx's `autodoc` without the configuration overhead.

### Why GitHub Pages over Read the Docs

| Host | GitHub Pages | Read the Docs |
|---|---|---|
| Cost | Free | Free |
| Access to source | Lives with the code, deploys from CI | Separate account + service |
| Custom domains | Supported | Supported |
| Versioned docs | Manual "latest/stable" (by branch) | Built-in "latest"/"stable" |
| Build dependencies | Fully controlled by your own CI | Limited to their build environment |

GitHub Pages is chosen because the deployment already happens in the repository's own CI, keeping docs builds in lockstep with the exact Python toolchain the project uses. For packages in the early template's target (single maintained branch), the added "stable" vs "latest" routing on Read the Docs offers little value over just publishing `main`. Documentation deploys on a push to `main`, so docs always match the current code.

## Evaluation criteria

When this setup was chosen, the options were compared against these criteria:

- **Ease of use** – how quickly a new contributor can write docs and get a preview. Favours Markdown and a curated default theme.
- **Support for docstrings / docs from Python code** – how well the tool can turn source docstrings into an API reference. Favours `mkdocstrings` / `autodoc`.
- **Deployment fit** – how much friction there is to publish, and whether the build runs in the project's own CI.
- **Maturity** – longevity, plugin ecosystem, and the size of the community maintaining it.

## Writing documentation

- Put pages in `docs/` and register them in `nav:` inside `mkdocs.yml`. A page not listed in `nav:` will not be part of the site.
- Follow the Material theme's [Markdown extensions](https://squidfunk.github.io/mkdocs-material/reference/) for admonitions, tabs, code annotations, and checklists. They are already enabled in `mkdocs.yml`.
- Cross-link pages with relative links (e.g. `[Usage](usage.md)`).
- Keep examples copy-pasteable and taken from the package's real code.
- Run `just docs-build` before pushing; strict mode fails the build on any warning, including broken links and unreadable reference directives.

## Keeping docstrings in sync

The [API reference](../reference/api.md) is generated from source docstrings with `mkdocstrings`, using `::: module.path.symbol` directives. Because this template relies on a placeholder for the package name, write docstrings in the package's source code and let CI catch drift — if a directive can't be resolved, `just docs-build` fails.

When a public API member is added or renamed, update `docs/reference/api.md` accordingly and verify with `just docs-build`.

## LLM-friendly output

The `mkdocs-llmstxt` plugin generates `llms.txt` and `llms-full.txt` in the built site, a Markdown digest of the docs tailored for LLMs and agents (per [llms.txt](https://llmstxt.org/)). Configure the included pages via the `llmstxt.sections` setting in `mkdocs.yml`. Because these are served from GitHub Pages, the digest is available at the site root, e.g. `https://your-org.github.io/my-project-name/llms.txt`.

## Agent skill discovery

Like the reference implementation this is based on ([draftjs_exporter](https://github.com/wagtail/draftjs_exporter)), the docs publish the package's own [agent skills](https://agentskills.io/) under `.well-known/agent-skills/` and `.well-known/ai-catalog.json`. Skills live under `src/my_project_name/.agents/skills/` (one directory per skill, each containing a `SKILL.md`), and an `on_post_build` hook (`docs/hooks.py`) copies them into the site and generates both discovery catalogs.

The hook reads host metadata from the `site_url` in `mkdocs.yml`, so no URLs are hardcoded. A placeholder skill is scaffolded by the template; edit or replace it in `src/my_project_name/.agents/skills/`. See the [Agent skills](../agent-skills.md) page for the published endpoints, and note that `.github/workflows/test.yml` sets `include-hidden-files: true` on the Pages upload so the `.well-known/` files are deployed.

## Contributing to these docs

Make changes to the relevant Markdown file in `docs/` or to `mkdocs.yml`, then verify with `just docs-build`. See the [contributing guidelines](https://github.com/org-name-or-username/my-project-name/blob/main/CONTRIBUTING.md) for the general workflow.
