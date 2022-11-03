.. _color-code-example:

Color Code Example
==============================================================================
这里是一些 Color Code 的示例. 你可以用 ``:Color:`text``` 这样的语法在 RestructuredText 中书写带颜色的文字, 或者加入其他格式.

- :black:`black`
- :gray:`gray`
- :silver:`silver`
- :white:`white`
- :brown:`brown`
- :maroon:`maroon`
- :red:`red`
- :magenta:`magenta`
- :fuchsia:`fuchsia`
- :pink:`pink`
- :orange:`orange`
- :yellow:`yellow`
- :lime:`lime`
- :darkseagreen:`darkseagreen`
- :green:`green`
- :olive:`olive`
- :teal:`teal`
- :cyan:`cyan`
- :aqua:`aqua`
- :dodgerblue:`dodgerblue`
- :blue:`blue`
- :navy:`navy`
- :blueviolet:`blueviolet`
- :purple:`purple`

- :under:`under`
- :over:`over`
- :blink:`blink`
- :line:`line`
- :strike:`strike`

- :it:`it`
- :ob:`ob`

- :small:`small`
- :large:`large`

这个项目使用了 ``custom-style.css`` 格式文件定义了 HTML CSS 格式. 然后在 ``.custom-style.rst`` 文件中将这些 HTML 格式注册为成了 ``.. role::``. 然后再在 `rst_prolog <https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-rst_prolog>`_ 配置中包含了 ``.custom-style.rst``, 使得这些格式会在每一个 RST 文件中被加载.
