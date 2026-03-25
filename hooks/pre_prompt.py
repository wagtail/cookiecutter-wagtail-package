"""
Cookiecutter pre_prompt hook, restructuring the tool-agnostic template ahead of Cookiecutter processing.
"""

import os
import shutil


EXCLUDE_FROM_TEMPLATE = {
    "template",
    "hooks",
    "cookiecutter.json",
    ".git",
    "__pycache__",
}


# Placeholder replacements: (pattern, replacement)
# Order matters: replace longer/more specific patterns first to avoid partial replacements
PLACEHOLDER_REPLACEMENTS = [
    ("my_project_name", "{{ cookiecutter.__project_name_snake }}"),
    ("my-project-name", "{{ cookiecutter.__project_name_kebab }}"),
    ("MyProjectName", "{{ cookiecutter.__project_name_camel }}"),
    ("My project name", "{{ cookiecutter.project_name }}"),
    (
        "Placeholder: Project short description",
        "{{ cookiecutter.project_short_description }}",
    ),
    (
        "https://github.com/org-name-or-username/my-project-name",
        "{{ cookiecutter.repository_url }}",
    ),
    ("<YEAR>", "{% now 'local', '%Y' %}"),
]

# Extensions for text files (skip replacement for binary files)
TEXT_EXTENSIONS = {
    ".py",
    ".md",
    ".txt",
    ".json",
    ".toml",
    ".yml",
    ".yaml",
    ".js",
    ".css",
    ".html",
    ".xml",
    ".ini",
    ".cfg",
    ".sh",
    ".bat",
}


def should_process_file(filepath: str) -> bool:
    """Check if file should be processed for text replacement."""
    ext = os.path.splitext(filepath)[1].lower()
    basename = os.path.basename(filepath)
    return ext in TEXT_EXTENSIONS or basename.startswith(".")


def copy_and_merge(
    src_root: str, target_root: str, exclude: set[str] | None = None
) -> None:
    """Copy root files to target, then overlay template files."""
    exclude = exclude or EXCLUDE_FROM_TEMPLATE

    def _ignore_excluded(directory: str, contents: list[str]) -> set[str]:
        if os.path.normpath(directory) == os.path.normpath(src_root):
            return {c for c in contents if c in exclude}
        return {c for c in contents if c in ("__pycache__", ".git")}

    shutil.copytree(src_root, target_root, ignore=_ignore_excluded, dirs_exist_ok=True)

    # Overlay template contents (overrides root files)
    template_path = os.path.join(src_root, "template")
    if os.path.isdir(template_path):
        shutil.copytree(template_path, target_root, dirs_exist_ok=True)


def rename_project_dirs(root: str) -> None:
    """Rename my_project_name directories to {{ cookiecutter.__project_name_snake }}."""
    # Walk bottom-up so we can rename nested directories
    for dirpath, dirnames, _ in os.walk(root, topdown=False):
        if "my_project_name" in dirnames:
            old_path = os.path.join(dirpath, "my_project_name")
            new_path = os.path.join(dirpath, "{{ cookiecutter.__project_name_snake }}")
            if os.path.exists(old_path):
                shutil.move(old_path, new_path)


def replace_placeholders_in_file(filepath: str) -> None:
    """Replace placeholders in a text file."""
    try:
        with open(filepath, encoding="utf-8", errors="replace") as f:
            content = f.read()
    except (OSError, UnicodeDecodeError):
        return

    original = content
    for pattern, replacement in PLACEHOLDER_REPLACEMENTS:
        content = content.replace(pattern, replacement)

    if content != original:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)


def replace_placeholders_in_tree(root: str) -> None:
    """Replace placeholders in all text files under root."""
    for dirpath, _, filenames in os.walk(root):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            if should_process_file(filepath):
                replace_placeholders_in_file(filepath)


def main() -> None:
    repo_root = os.getcwd()
    target_folder_name = "{{ cookiecutter.__project_name_kebab }}"
    target_path = os.path.join(repo_root, target_folder_name)

    # Create target folder and merge content (exclude target from copy)
    os.makedirs(target_path, exist_ok=True)
    copy_exclude = EXCLUDE_FROM_TEMPLATE | {target_folder_name}
    copy_and_merge(repo_root, target_path, copy_exclude)

    # Rename my_project_name directories
    rename_project_dirs(target_path)

    # Replace placeholders in file contents
    replace_placeholders_in_tree(target_path)


if __name__ == "__main__":
    main()
