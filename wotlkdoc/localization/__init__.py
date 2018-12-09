# -*- coding: utf-8 -*-

from loc import LocDict
import pandas as pd
from pathlib_mate import PathCls as Path

TAB = "\t"
DATA_DIR = Path(Path(__file__).change(new_basename="data"))


def read_loc_dict(file):
    df = pd.read_csv(Path(DATA_DIR, file).abspath, sep=TAB)
    ld = LocDict(data=df.to_dict(orient="list"))
    return ld


ld_wotlk = read_loc_dict("wotlk-dict.txt")


def trim_space():
    for p in DATA_DIR.select_by_ext(".txt"):
        df = pd.read_csv(p.abspath, sep=TAB)
        df = df.applymap(str.strip)
        df.to_csv(p.abspath, index=False, sep=TAB)


if __name__ == "__main__":
    trim_space()
    pass
