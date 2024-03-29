.. _doc-style-guide:

Doc Style Guide
==============================================================================
本文档规定了在写此文档项目的时候, 要遵循的一些规范.


标题 和 引用链接 Title and Reference Link
------------------------------------------------------------------------------
如果一篇文档只适用于特定的资料片版本, 那么在标题和引用链接中请包含版本名称的缩写. 例如:

.. code-block:: ReST

    .. _wotlk-leveling-guide:

    巫妖王之怒 升级攻略
    ==============================================================================


关键字 Keyword
------------------------------------------------------------------------------
文档网站可被搜索的最小单元是 词. 如果你一长串中文中间的词是无法被搜索到的. 为了使得各个文档能更容易地被搜索到, 我们要求在每篇文档的顶级标题下面有一行: ``关键词: 词1, 词2, ...``, 定义了搜索这篇文档的关键词. 例如:

.. code-block:: ReST

    .. _wotlk-leveling-guide:

    巫妖王之怒 升级攻略
    ==============================================================================
    关键词: 升级, level, leveling


目录 Table of Content
------------------------------------------------------------------------------
RestructuredText 允许你用 ``.. contents::`` 自动创建目录. 但是我们用的 furo 主题已经内置了这个功能. 在大部分的文档顶部, 我们已经不再需要目录元素了. 如果有特殊需求, 还是可以自定义的, 但是尽量不要.

.. code-block:: ReST

    .. contents::
        :class: this-will-duplicate-information-and-it-is-still-useful-here
        :depth: 1
        :local:
