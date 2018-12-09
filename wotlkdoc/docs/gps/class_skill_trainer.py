# -*- coding: utf-8 -*-

"""

"""

try:
    from .helper import (
        remove_go_cmd_construct_teleport,
        disaggregate_df_transform_to_list_table,
    )
except:
    from wotlkdoc.docs.gps.helper import (
        remove_go_cmd_construct_teleport,
        disaggregate_df_transform_to_list_table,
    )
from wotlkdoc.compressed_tsv import make_gzip, read_compressed_tsv
from wotlkdoc.docs.images import img_class_icon
from rstobj.directives import Image

class_trainer_gps_columns = "阵营,职业,城市,位置,gm_cmd".split(",")


def read_data_and_derive_df_list(tsv_filename):
    make_gzip(this_file=__file__, filename=tsv_filename)
    df = read_compressed_tsv(this_file=__file__, filename=tsv_filename + ".gz")
    df.columns = class_trainer_gps_columns
    df = remove_go_cmd_construct_teleport(df)
    df["职业"] = df["职业"].apply(lambda v: Image(uri=img_class_icon[v]))
    lt_list = disaggregate_df_transform_to_list_table(df, "阵营")
    return lt_list


lt_list_class_trainer_gsp = read_data_and_derive_df_list("class-skill-trainer.tsv")

if __name__ == "__main__":
    print(lt_list_class_trainer_gsp[0][1].render())
