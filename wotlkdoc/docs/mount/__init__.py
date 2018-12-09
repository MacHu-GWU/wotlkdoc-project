# -*- coding: utf-8 -*-

from wotlkdoc.compressed_tsv import make_gzip, read_compressed_tsv
from wotlkdoc.df_to_list_table import df_to_list_table

make_gzip(this_file=__file__, filename="all-mount.tsv")
df = read_compressed_tsv(this_file=__file__, filename="all-mount.tsv.gz")
lt_mount = df_to_list_table(
    df,
    title="坐骑相关GM命令",
    code_column_and_transform_func={"添加坐骑": None, "上马命令": None},
)

if __name__ == "__main__":
    print(lt_mount.render())
