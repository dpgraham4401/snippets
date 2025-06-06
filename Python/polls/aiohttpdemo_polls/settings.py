# aiohttpdemo_polls/settings.py
import pathlib

import yaml

BASE_DIR = pathlib.Path(__file__).parent.parent
config_path = BASE_DIR / "config" / "polls.yaml"


def get_config(path):
    with pathlib.Path(path).open("r") as f:
        config = yaml.safe_load(f)
    return config


config = get_config(config_path)
