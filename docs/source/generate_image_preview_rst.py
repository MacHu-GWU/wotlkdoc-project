# -*- coding: utf-8 -*-

"""
Automatically generate index.rst file to display images. (except the 'icon' dir)
"""

try:
    from pathlib_mate import PathCls as Path
except:
    from pathlib_mate import Path

dir_here = Path(__file__).parent
"""
wotlkdoc_images-project/docs/source
"""
dir_static = Path(dir_here, "_static")
dir_images = Path(dir_static, "image")


def create_rst_file(dir_path):
    p = Path(dir_path)
    relpath = p.relative_to(dir_images)
    rst_dirpath = Path(dir_here, "99-附录 (Appendix)", "01-常用图标外链查询", relpath)

    if not rst_dirpath.exists():
        rst_dirpath.mkdir()
    rst_path = Path(rst_dirpath, "index.rst")

    lines = list()
    lines.append(p.basename)
    lines.append("=" * 80)
    lines.append(".. contents:: 索引")
    lines.append("    :local:")

    sub_p_list = Path.sort_by_abspath(dir_path.select_dir(recursive=False))
    if len(sub_p_list):
        lines.append("\n**目录**:\n")
        lines.append("\n.. articles::\n")

    for p_png in Path.sort_by_abspath(p.select_image(recursive=False)):
        lines.append("\n" + p_png.fname)
        lines.append("-" * 80)
        url = "/" + str(p_png.relative_to(dir_here))
        directive = ".. image:: {}".format(url)
        lines.append(directive)

    content = "\n".join(lines)
    rst_path.write_text(content, "utf-8")

    if len(sub_p_list):
        for sub_p in sub_p_list:
            create_rst_file(sub_p)


if __name__ == "__main__":
    for p in Path.sort_by_abspath(dir_images.select_dir(recursive=False)):
        if p.basename != "icon":
            create_rst_file(p)
