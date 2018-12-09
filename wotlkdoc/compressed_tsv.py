# -*- coding: utf-8 -*-

"""

"""

import gzip
import pandas as pd
from pathlib_mate import Path


def make_gzip(this_file, filename):
    """
    将文件名为 <filename> 的 ``.tsv`` 文件 (后缀名必须是tsv, 否则出粗) 压缩成 ``.tsv.gz``
    的压缩包文件. 执行该操作的 python 脚本必须和 ``.tsv`` 文件在同一目录下.

    :param this_file: 当前 python 脚本的文件全路径
    :param filename: ``.tsv`` 文件名.
    """
    if not filename.endswith(".tsv"):
        raise ValueError

    dst = Path(this_file).change(new_basename=filename + ".gz")
    if not dst.exists():
        with open(Path(this_file).change(new_basename=filename).abspath, "rb") as f:
            b = f.read()
        with gzip.open(dst.abspath, 'wb') as f:
            f.write(b)


def read_compressed_tsv(this_file, filename):
    """
    从当前脚本所在的文件夹读取压缩的 ``.tsv.gz`` 文件. 读成 ``pd.DataFrame``.

    :param this_file:
    :param filename: ``.tsv.gz`` 文件
    :return: ``pd.DataFrame``
    """
    if not filename.endswith(".tsv.gz"):
        raise ValueError
    dst = Path(this_file).change(new_basename=filename)
    return pd.read_csv(
        dst.abspath,
        sep="\t", compression="gzip",
    )


