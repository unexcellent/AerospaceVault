#!/usr/bin/env python3
import argparse
from pathlib import Path
from glob import glob
import shutil
import os
import re

TARGET_REPO_PATH = Path(__file__).parent

def copy_vault(vault_path: Path):
    _erase_repo()
    all_file_paths = _list_all_files(vault_path)
    attachments = _copy_uni_md_files_and_return_attachment_names(all_file_paths, vault_path)
    _copy_attachments(all_file_paths, attachments, vault_path)

def _erase_repo():
    files_that_should_not_be_erased = [
        Path(__file__),
        TARGET_REPO_PATH / ".gitignore",
        TARGET_REPO_PATH / "README.md",
    ]

    all_files_in_this_repo = _list_all_files(TARGET_REPO_PATH)
    for file_path in all_files_in_this_repo:
        if file_path in files_that_should_not_be_erased:
            continue

        os.remove(str(file_path))

def _list_all_files(vault_path: Path) -> list[Path]:
    return [Path(p) for p in sorted(glob(str(vault_path) + "/**/**.**", recursive=True))]

def _copy_uni_md_files_and_return_attachment_names(
    all_file_paths: list[Path], 
    vault_path: Path
) -> set[str]:
    attachment_list = []
    for file_path in all_file_paths:
        
        file_is_not_markdown = file_path.suffix != ".md" or "excalidraw" in file_path.name
        if file_is_not_markdown:
            continue

        with file_path.open() as file:
            content = file.read()

        file_is_not_for_uni = "#uni/courses/" not in content
        if file_is_not_for_uni:
            continue

        attachment_list.extend(_extract_attachment_list_from_md(content))

        _copy_file(file_path, vault_path)

    return set(attachment_list)

def _extract_attachment_list_from_md(file_content: str) -> list[str]:
    attachment_list = re.findall(r'!\[\[(.*?)(?:\|.*?)?\]\]', file_content)

    for i, attachment in enumerate(attachment_list):
        if attachment.endswith(".excalidraw"):
            attachment_list[i] += ".md"

    return attachment_list

def _copy_file(file_path: Path, vault_path: Path):
    target_path = TARGET_REPO_PATH / "vault" / file_path.relative_to(vault_path)
    target_path.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(file_path, target_path)

def _copy_attachments(all_file_paths: list[Path], attachments: set[str], vault_path: Path):
    for file_path in all_file_paths:
        if file_path.name not in attachments:
            continue

        _copy_file(file_path, vault_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="Copy Vault",
        description="This program copies all uni related files from an obsidian vault into this repo."
    )
    parser.add_argument(
        "vault_path", 
        help="Path to the vault where the files should be copied from."
    )

    args = parser.parse_args()
    copy_vault(Path(args.vault_path))