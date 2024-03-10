import argparse
import json
import pathlib
import sys

import mistletoe

from . import custom_link


def parse_file_paths(args):
    if not sys.stdin.isatty():
        return [path.strip() for path in sys.stdin.readlines()]
    else:
        if not args.file_paths:
            return []
        return [path.strip() for path in args.file_paths[0].split("\n") if path.strip()]


def get_file_paths():
    parser = argparse.ArgumentParser(
        description="Process file paths from stdin and extract links using custom_link."
    )
    parser.add_argument(
        "file_paths",
        nargs="*",
        help="File paths to process (if not provided via stdin)",
    )
    args = parser.parse_args()

    file_paths = parse_file_paths(args)

    if not file_paths:
        parser.print_help()
        sys.exit(1)

    return file_paths


def main() -> int:
    file_paths = get_file_paths()

    results = []
    for file_path in file_paths:
        with open(file_path, "r") as fin:
            with custom_link.CustomLinkRenderer() as renderer:
                renderer.render(mistletoe.Document(fin))
                result = {
                    "path": str(pathlib.Path(file_path).resolve()),
                    "links": renderer.links,
                }
                results.append(result)

    print(json.dumps(results, indent=2))
    return 0
