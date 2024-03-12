import pathlib


def should_include_file(path):
    return path.is_file() and not any(
        exclude in path.parts for exclude in (".git", ".trash")
    )


def get_file_paths(base_dir, include_substrings, exclude_substrings):
    file_paths = [
        str(path.resolve())
        for path in pathlib.Path(base_dir).glob("**/*")
        if should_include_file(path)
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
