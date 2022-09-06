# -*- coding: utf-8 -*-

"""
本模块提供了对数据文件进行编辑, 管理, 引用的工作流.

1. 把数据文件 check in 到代码库的时候, 存的是 .tsv.gz 文件. 你可以用 ``make update_gzip``
    命令进行批量更新.
2. 你编辑数据内容的时候, 是用 ``make restore`` 命令将 .tsv.gz 恢复成 .tsv 文件
    (如果 .tsv 已经存在则认为你正在编辑, 不进行恢复), 然后 copy paste .tsv 文件的内容
    到 Google Sheet 中编辑. 满意了再用 #1 中的步骤更新, 并 check in 到代码库.
3. 对数据的 DataFrame 进行引用的时候用的是 :class:`TsvGzReader`` 类,  初始化的时候
    只 pass 一个 ``reader = TsvGzReader(__file__)`` 参数, 让它能定位到你当前目录.
    然后用 df = reader.read_df("filename.tsv.gz") 来读取 DataFrame 数据.
"""

import gzip
import attr
from attrs_mate import AttrsClass
from pathlib_mate import Path
import polars as pl


def gzip_compress(f_in: str, f_out: str):
    with gzip.open(f_out, "wb") as f:
        f.write(Path(f_in).read_bytes())


def gzip_decompress(f_in: str, f_out: str):
    with gzip.open(f_in, "rb") as f:
        Path(f_out).write_bytes(f.read())


dir_here = Path.dir_here(__file__)


def update_gzip():
    for path in dir_here.select_by_ext(recursive=True, ext=".tsv"):
        path_gz = Path(path.abspath + ".gz")
        gzip_compress(f_in=path.abspath, f_out=path_gz.abspath)


def restore_tsv():
    for path_gz in dir_here.select_by_ext(recursive=True, ext=".gz"):
        path_tsv = path_gz.change(new_basename=path_gz.fname)
        if not path_tsv.exists():
            gzip_decompress(f_in=path_gz.abspath, f_out=path_tsv.abspath)


@attr.s
class TsvGzReader(AttrsClass):
    file: str = attr.ib()

    @property
    def dir_here(self) -> Path:
        return Path(self.file).parent

    def read_df(self, filename: str) -> pl.DataFrame:
        p = self.dir_here / filename
        return pl.read_csv(p.abspath, sep="\t")


def example():
    reader = TsvGzReader(__file__)
    print(reader.read_df("example-items.tsv.gz"))
