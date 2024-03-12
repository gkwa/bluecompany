import argparse
import json
import pathlib
import sys

import mistletoe

from . import custom_link


def get_file_paths(base_dir, include_substrings, exclude_substrings):
    file_paths = [
        str(path.resolve())
        for path in pathlib.Path(base_dir).glob("**/*")
        if path.is_file()
    ]

    if include_substrings:
        file_paths = [
            path
            for path in file_paths
            if all(
                substring.lower() in path.lower() for substring in include_substrings
            )
        ]

    if exclude_substrings:
        file_paths = [
            path
            for path in file_paths
            if not any(
                substring.lower() in path.lower() for substring in exclude_substrings
            )
        ]

    return file_paths


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Process files in a directory and extract links using custom_link."
    )
    parser.add_argument(
        "base_dir",
        help="Base directory to search for files",
    )
    parser.add_argument(
        "--include",
        dest="include_substrings",
        action="append",
        help="Include files by substring in their absolute path (can be specified multiple times, case-insensitive)",
    )
    parser.add_argument(
        "--exclude",
        dest="exclude_substrings",
        action="append",
        help="Exclude files by substring in their absolute path (can be specified multiple times, case-insensitive)",
    )
    args = parser.parse_args()

    file_paths = get_file_paths(
        args.base_dir, args.include_substrings, args.exclude_substrings
    )

    if not file_paths:
        print("No matching files found.")
        sys.exit(1)

    results = []
    for file_path in file_paths:
        with open(file_path, "r") as fin:
            with custom_link.CustomLinkRenderer() as renderer:
                renderer.render(mistletoe.Document(fin))
            result = {
                "path": file_path,
                "links": renderer.links,
            }
            results.append(result)

    print(json.dumps(results, indent=2))
    return 0
