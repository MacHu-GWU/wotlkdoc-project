# -*- coding: utf-8 -*-

import pytest


def test():
    import wotlkdoc
    from wotlkdoc.docs import doc_data


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
