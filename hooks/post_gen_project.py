from pathlib import Path
import shutil


def remove_frontend_files():
    files_to_remove = [
        ".eslintignore",
        ".eslintrc.js",
        ".nvmrc",
        ".prettierignore",
        ".stylelintignore",
        ".stylelintrc.js",
        "package.json",
        "prettier.config.js",
        "tsconfig.json",
        "webpack.config.js",
    ]
    dirs_to_remove = [
        Path("{{ cookiecutter.__project_name_snake }}", "static_src")
    ]
    for filename in files_to_remove:
        Path.unlink(Path(filename))
    for directory in dirs_to_remove:
        shutil.rmtree(directory)


def main():
    if "{{ cookiecutter.use_frontend }}".lower() != "y":
        remove_frontend_files()


if __name__ == "__main__":
    main()
