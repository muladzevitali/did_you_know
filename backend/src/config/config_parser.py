"""Configuration class for applications"""

import configparser
from pathlib import Path
from dataclasses import dataclass

config = configparser.ConfigParser()
config.read("config.ini")
base_dir = Path('.')


@dataclass()
class Application:
    debug = config['APPLICATION'].getboolean('DEBUG')
