import argparse
import json

from . import config, file_utils, process_files


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Process files in a directory and extract links using custom_link."
    )
    subparsers = parser.add_subparsers(dest="subcommand")

    config.add_config_subparser(subparsers)
    process_files.add_process_subparser(subparsers)

    args = parser.parse_args()

    if args.subcommand == "config":
        return config.handle_config_subcommand(args)
    elif args.subcommand == "process":
        base_dir = config.load_base_directory()
        if not base_dir:
            print(
                "Base directory not configured. Please run 'bluecompany config dir /path/to/base/dir' first."
            )
            return 1

        file_paths = file_utils.get_file_paths(
            base_dir, args.include_substrings, args.exclude_substrings
        )

        if not file_paths:
            print("No matching files found.")
            return 1

        results = process_files.process_files(file_paths)
        print(json.dumps(results, indent=2))
        return 0
    else:
        parser.print_help()
        return 1
