import mistletoe

from . import custom_link


def add_process_subparser(subparsers):
    process_parser = subparsers.add_parser(
        "process", help="Process files in the base directory"
    )
    process_parser.add_argument(
        "--include",
        dest="include_substrings",
        action="append",
        help="Include files by substring in their absolute path (can be specified multiple times, case-insensitive)",
    )
    process_parser.add_argument(
        "--exclude",
        dest="exclude_substrings",
        action="append",
        help="Exclude files by substring in their absolute path (can be specified multiple times, case-insensitive)",
    )


def process_files(file_paths):
    results = []
    for file_path in file_paths:
        print(f"Processing {file_path}")
        try:
            with open(file_path, "r") as fin:
                with custom_link.CustomLinkRenderer() as renderer:
                    renderer.render(mistletoe.Document(fin))
                result = {
                    "path": file_path,
                    "links": renderer.links,
                }
                results.append(result)
        except UnicodeDecodeError:
            print(f"Skipping {file_path} due to UnicodeDecodeError (binary file)")
            continue

    return results
