import pathlib
import sys

import platformdirs
import yaml

CONFIG_DIR = platformdirs.user_data_dir("bluecompany", "Acme")
CONFIG_PATH = pathlib.Path(CONFIG_DIR) / "config.yaml"


def add_config_subparser(subparsers):
    config_parser = subparsers.add_parser("config", help="Configure the base directory")
    config_subparsers = config_parser.add_subparsers(dest="config_subcommand")
    config_dir_parser = config_subparsers.add_parser(
        "dir", help="Set the base directory"
    )
    config_dir_parser.add_argument("dir", help="Base directory to search for files")


def handle_config_subcommand(args):
    if args.config_subcommand == "dir":
        base_dir = args.dir
        save_config("base_dir", base_dir)
        print(f"Base directory configured: {base_dir}")
    elif args.config_subcommand is None:
        base_dir = load_config("base_dir")
        if base_dir:
            print(f"Current base directory: {base_dir}")
        else:
            print("Base directory not configured.")
    return 0


def load_config(key):
    print(f"config_path: {CONFIG_PATH}", file=sys.stderr)
    if CONFIG_PATH.exists():
        with open(CONFIG_PATH, "r") as f:
            config = yaml.safe_load(f)
        return config.get(key)
    return None


def save_config(key, value):
    CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)
    if CONFIG_PATH.exists():
        with open(CONFIG_PATH, "r") as f:
            config = yaml.safe_load(f)
    else:
        config = {}
    config[key] = value
    with open(CONFIG_PATH, "w") as f:
        yaml.dump(config, f)
