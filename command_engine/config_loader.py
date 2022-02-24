from enum import Enum
from typing import Optional

import yaml


class LocationEnum(Enum):
    EU_WEST_ONE = "eu_west_1"


class ConfigEngine(dict):

    def __init__(self, config_path: str) -> None:
        super().__init__({})
        self.config_path: str = config_path
        self.location: Optional[LocationEnum] = None
        self._read()
        self._establish_location()

    def _read(self) -> None:
        with open(self.config_path) as file:
            data = yaml.load(file, Loader=yaml.FullLoader)
            self.update(data)

    def _establish_location(self) -> None:
        self.location = LocationEnum(self["location"])
