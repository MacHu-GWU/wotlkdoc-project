# -*- coding: utf-8 -*-

"""

"""

try:
    from .helper import (
        remove_go_cmd_construct_teleport,
        df_to_list_table,
    )
except:
    from wotlkdoc.docs.gps.helper import (
        remove_go_cmd_construct_teleport,
        df_to_list_table,
    )
from wotlkdoc.compressed_tsv import make_gzip, read_compressed_tsv
from wotlkdoc.docs.images import img_trade_skill
from rstobj.directives import Image

trade_skill_trainer_gps_columns = "阵营,商业技能,等级范围,位置,gm_cmd".split(",")


def read_data_and_derive_df_list(tsv_filename):
    make_gzip(this_file=__file__, filename=tsv_filename)
    df = read_compressed_tsv(this_file=__file__, filename=tsv_filename + ".gz")
    df.columns = trade_skill_trainer_gps_columns
    df = remove_go_cmd_construct_teleport(df)

    def construct_img(trade_skill_name):
        if trade_skill_name in img_trade_skill:
            return Image(uri=img_trade_skill[trade_skill_name], width=64, height=64)
        else:
            return trade_skill_name

    label_column = "商业技能"
    df_list = [
        [label, df[df[label_column] == label].copy()]
        for label in df[label_column].unique()
    ]
    for pair in df_list:
        trade_skill_name = pair[0]
        sub_df = pair[1]
        sub_df[label_column] = sub_df[label_column].apply(construct_img)
        pair[1] = df_to_list_table(sub_df, title="{}".format(trade_skill_name))

    lt_list = df_list
    return lt_list


lt_list_trade_skill_trainer_gsp = read_data_and_derive_df_list("trade-skill-trainer.tsv")

if __name__ == "__main__":
    print(lt_list_trade_skill_trainer_gsp[0][1].render())
