# -*- coding: utf-8 -*-

"""
Parse and format ``.go x y z`` command.
"""

import attr
from attrs_mate import AttrsClass


@attr.s
class GoCmd(AttrsClass):
    """
    Represent a GM ``.go x y z`` command.
    """
    x: float = attr.ib()
    y: float = attr.ib()
    z: float = attr.ib()
    map_id: int = attr.ib()

    @property
    def go_cmd(self) -> str:
        return ".go {:.2f} {:.2f} {:.2f} {}".format(
            self.x,
            self.y,
            self.z,
            self.map_id,
        )

    @property
    def go_xyz_cmd(self) -> str:
        return ".go xyz {:.2f} {:.2f} {:.2f} {}".format(
            self.x,
            self.y,
            self.z,
            self.map_id,
        )

    @classmethod
    def from_string(cls, s: str) -> 'GoCmd':
        """
        Valid format:

        - "1.23 4.56 7.89 0"
        - ".go 1.23 4.56 7.89 0"
        - ".go xyz 1.23 4.56 7.89 0"
        """
        s = s.strip()
        if s.startswith(".go"):
            if "xyz" in s:
                _, _, x, y, z, map_id = s.split(" ")
            else:
                _, x, y, z, map_id = s.split(" ")
        else:
            x, y, z, map_id = s.split(" ")
        return GoCmd(
            x=float(x),
            y=float(y),
            z=float(z),
            map_id=int(map_id),
        )
