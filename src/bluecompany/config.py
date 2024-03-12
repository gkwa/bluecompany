import pathlib

import platformdirs
import yaml


def add_config_subparser(subparsers):
    config_parser = subparsers.add_parser("config", help="Configure the base directory")
    config_subparsers = config_parser.add_subparsers(dest="config_subcommand")

    config_dir_parser = config_subparsers.add_parser(
        "dir", help="Set the base directory"
    )
    config_dir_parser.add_argument(
        "dir",
        help="Base directory to search for files",
    )


def handle_config_subcommand(args):
    if args.config_subcommand == "dir":
        base_dir = args.dir
        save_base_directory(base_dir)
        print(f"Base directory configured: {base_dir}")
        return 0
    elif args.config_subcommand is None:
        base_dir = load_base_directory()
        if base_dir:
            print(f"Current base directory: {base_dir}")
        else:
            print("Base directory not configured.")
        return 0


def load_base_directory():
    config_dir = platformdirs.user_data_dir("bluecompany", "Acme")
    config_path = pathlib.Path(config_dir) / "config.yaml"
    print(f"config_path: {config_path}")
    if config_path.exists():
        with open(config_path, "r") as f:
            config = yaml.safe_load(f)
            return config.get("base_dir")
    return None


def save_base_directory(base_dir):
    config_dir = platformdirs.user_data_dir("bluecompany", "Acme")
    pathlib.Path(config_dir).mkdir(parents=True, exist_ok=True)
    config_path = pathlib.Path(config_dir) / "config.yaml"
    config = {"base_dir": base_dir}
    with open(config_path, "w") as f:
        yaml.dump(config, f)
