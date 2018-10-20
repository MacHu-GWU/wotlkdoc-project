# -*- coding: utf-8 -*-

import pandas as pd
from pathlib_mate import PathCls as Path
from pypinyin import pinyin, Style, lazy_pinyin


class CurrentDirDataFrameReader(object):
    def __init__(self, this_file):
        self.this_file = this_file

    def read_csv(self, filename, **kwargs):
        return pd.read_csv(
            Path(self.this_file).change(new_basename=filename).abspath,
            sep="\t",
            **kwargs
        )


def get_pinyin(word):
    return "".join(lazy_pinyin(word))


def get_first_letter_pinyin(word):
    return "".join([l[0] for l in pinyin(word, style=Style.FIRST_LETTER)])
