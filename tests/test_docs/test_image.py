# -*- coding: utf-8 -*-

import os
import pytest
from wotlkdoc.docs.images import (
    image_path_to_href,
    dir_source,
)


def test_image_path_to_href():
    img_path = (dir_source / "_static" / "wotlkdoc-logo.png").abspath
    image_path_to_href(img_path)


if __name__ == "__main__":
    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
