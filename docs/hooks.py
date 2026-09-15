"""MkDocs build hook publishing the package's agent skills.

Copies the skills bundled with the package (under the package's
``.agents/skills/*/SKILL.md``) into the built site under
``.well-known/agent-skills/`` and generates two discovery catalogs:

- ``.well-known/agent-skills/index.json`` – the agent skills discovery format.
- ``.well-known/ai-catalog.json`` – the AI catalog format.

The host metadata is derived from the configured ``site_url`` at build time, so
it stays correct for both the template and generated packages without hardcoding
URLs.
"""

from __future__ import annotations

import hashlib
import json
import shutil

from datetime import UTC, datetime
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

import yaml


# --- Constants ---------------------------------------------------------------

# Canonical skill source files under the package, bundled with the published docs.
SKILLS_DIR = (
    Path(__file__).parent.parent / "src" / "my_project_name" / ".agents" / "skills"
)

WELL_KNOWN_DIR = ".well-known/agent-skills"
"""Output directory for skills, relative to the site directory."""

CATALOG_FILENAME = ".well-known/ai-catalog.json"
"""Name of the AI catalog file, relative to the site directory."""

HOST_DISPLAY_NAME = "My project name"
SKILL_TYPE = "skill-md"
SKILL_MIME = "application/agent-skills+md"
SKILL_VERSION = "1.0.0"
# Human-readable catalog titles keyed by skill directory name.
SKILL_DISPLAY_NAMES = {
    "my-project-name": "My project name",
}


# --- Helpers -----------------------------------------------------------------


def _parse_frontmatter(content: str) -> dict[str, Any]:
    """Parse YAML frontmatter from a Markdown file's content."""
    if not content.startswith("---"):
        return {}
    parts = content.split("---", 2)
    if len(parts) < 3:
        return {}
    return yaml.safe_load(parts[1]) or {}


def _sha256(path: Path) -> str:
    """Compute the ``sha256:…`` digest of a file."""
    h = hashlib.sha256(path.read_bytes())
    return f"sha256:{h.hexdigest()}"


def _iso_date(path: Path) -> str:
    """Format a file's last-modified time as ``YYYY-MM-DDTHH:MM:SSZ``."""
    ts = datetime.fromtimestamp(path.stat().st_mtime, tz=UTC)
    return ts.strftime("%Y-%m-%dT00:00:00Z")


def _read_version() -> str:
    """Read the package version from ``__init__.py`` without importing it."""
    init = Path(__file__).parent.parent / "src" / "my_project_name" / "__init__.py"
    for line in init.read_text().splitlines():
        stripped = line.strip()
        # Match both a literal `__version__ = "x.y.z"` and the template's
        # `VERSION = (0, 1, 0)` tuple form.
        if stripped.startswith("__version__") or stripped.startswith("VERSION"):
            numbers = "".join(ch for ch in stripped if ch.isdigit() or ch == ",")
            parts = [part for part in numbers.split(",") if part]
            if parts:
                return ".".join(parts)
    return SKILL_VERSION


def _discover_skills() -> list[Path]:
    """Find every ``SKILL.md`` under the package's ``.agents/skills/``."""
    if not SKILLS_DIR.exists():
        return []
    return sorted(SKILLS_DIR.glob("*/SKILL.md"))


def _site_root(config: dict[str, Any]) -> str:
    """Return the site's root URL, with a trailing slash stripped."""
    return str(config.get("site_url", "")).rstrip("/")


def _host(config: dict[str, Any]) -> dict[str, str]:
    """Build the host metadata from the configured ``site_url``."""
    site_root = _site_root(config)
    parsed = urlparse(site_root)
    # GitHub Pages project sites live under a path segment: the subpath becomes
    # the resource in path-based did:web and the URN authority.
    authority = parsed.netloc
    subpath = "/".join(parsed.path.strip("/").split("/"))
    if subpath:
        authority = f"{authority}:{subpath}"
    return {
        "displayName": HOST_DISPLAY_NAME,
        "identifier": f"did:web:{authority}",
        "documentationUrl": f"{site_root}/",
        "urnAuthority": authority,
    }


# --- Hook --------------------------------------------------------------------


def on_post_build(config: dict[str, Any], **kwargs: Any) -> None:
    """Copy skill files and generate discovery catalogs after the build."""
    site_dir = Path(config["site_dir"])
    site_root = _site_root(config)
    host = _host(config)

    # Directory where the skills land in the built site.
    skills_out = site_dir / WELL_KNOWN_DIR
    skills_out.mkdir(parents=True, exist_ok=True)

    # Discover and copy all SKILL.md files.
    index_entries: list[dict[str, Any]] = []
    catalog_entries: list[dict[str, Any]] = []

    for skill_path in _discover_skills():
        name = skill_path.parent.name
        target_dir = skills_out / name
        target_dir.mkdir(parents=True, exist_ok=True)
        shutil.copy2(skill_path, target_dir / "SKILL.md")

        # Parse frontmatter for metadata.
        frontmatter = _parse_frontmatter(skill_path.read_text(encoding="utf-8"))
        description = frontmatter.get("description", "")
        display_name = SKILL_DISPLAY_NAMES.get(name, name)
        digest = _sha256(skill_path)
        updated_at = _iso_date(skill_path)

        # Absolute URL for the AI catalog. Prefer a directory-relative URL in
        # the agent-skills index so path-absolute `/.well-known/...` does not
        # resolve against the GitHub Pages *origin* (missing project subpath).
        rel_path = f"{WELL_KNOWN_DIR}/{name}/SKILL.md"
        full_url = f"{site_root}/{rel_path}"

        index_entries.append(
            {
                "name": name,
                "type": SKILL_TYPE,
                "description": description,
                "url": f"{name}/SKILL.md",
                "digest": digest,
            }
        )
        catalog_entries.append(
            {
                "identifier": f"urn:air:{host['urnAuthority']}:skill:{name}",
                "displayName": display_name,
                "type": SKILL_MIME,
                "url": full_url,
                "description": description,
                "version": _read_version(),
                "updatedAt": updated_at,
                "publisher": host,
            }
        )

    # Write the agent-skills discovery index.
    index = {
        "$schema": "https://schemas.agentskills.io/discovery/0.2.0/schema.json",
        "skills": index_entries,
    }
    (skills_out / "index.json").write_text(
        json.dumps(index, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    # Write the AI catalog.
    catalog = {
        "specVersion": "1.0",
        "host": host,
        "entries": catalog_entries,
    }
    (site_dir / CATALOG_FILENAME).write_text(
        json.dumps(catalog, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
