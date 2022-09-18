# -*- coding: utf-8 -*-

from ..importer import (
    TsvGzReader,
    dataframe_to_list_table,
)


def lt_expansion():
    reader = TsvGzReader(__file__)
    df = reader.read_df("expansion.tsv.gz")
    lt = dataframe_to_list_table(df, title=f"魔兽世界各资料片一栏", )
    return lt
