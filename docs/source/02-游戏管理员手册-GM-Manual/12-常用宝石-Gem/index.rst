.. _常用宝石GM命令:

常用宝石 Gem
==============================================================================


燃烧的远征
------------------------------------------------------------------------------


巫妖王之怒
------------------------------------------------------------------------------


:red:`红色`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
:red:`力量`::

	.add 40111

:red:`敏捷`::

	.add 40112

:red:`AP`::

	.add 40114

:red:`SP`::

	.add 40113

:red:`破甲`::

	.add 40117

:red:`精准`::

	.add 40118

:red:`躲闪`::

	.add 40115

:red:`招架`::

	.add 40116


:yellow:`黄色`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
:yellow:`智力`::

	.add 40123

:yellow:`命中`::

	.add 40125

:yellow:`暴击`::

	.add 40124

:yellow:`急速`::

	.add 40128

:yellow:`防御`::

	.add 40126

:yellow:`韧性`::

	.add 40127


:dodgerblue:`蓝色`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
:dodgerblue:`耐力`::

	.add 40119

:dodgerblue:`精神`::

	.add 40120

:dodgerblue:`MP5`::

	.add 40121

:dodgerblue:`减抗`::

	.add 40122


:orange:`橙色`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
:red:`力量`, :yellow:`命中`::

	.add 40143

:red:`力量`, :yellow:`暴击`::

	.add 40142

:red:`力量`, :yellow:`急速`::

	.add 40146

:red:`力量`, :yellow:`防御`::

	.add 40144

:red:`力量`, :yellow:`韧性`::

	.add 40145

:red:`敏捷`, :yellow:`命中`::

	.add 40148

:red:`敏捷`, :yellow:`暴击`::

	.add 40147

:red:`敏捷`, :yellow:`急速`::

	.add 40150

:red:`敏捷`, :yellow:`韧性`::

	.add 40149

:red:`SP`, :yellow:`智力`::

	.add 40151

:red:`SP`, :yellow:`命中`::

	.add 40153

:red:`SP`, :yellow:`暴击`::

	.add 40152

:red:`SP`, :yellow:`急速`::

	.add 40155

:red:`SP`, :yellow:`韧性`::

	.add 40154

:red:`AP`, :yellow:`命中`::

	.add 40157

:red:`AP`, :yellow:`暴击`::

	.add 40156

:red:`AP`, :yellow:`急速`::

	.add 40159

:red:`AP`, :yellow:`韧性`::

	.add 40158

:red:`闪躲`, :yellow:`防御`::

	.add 40160

:red:`招架`, :yellow:`防御`::

	.add 40161

:red:`精准`, :yellow:`命中`::

	.add 40162

:red:`精准`, :yellow:`防御`::

	.add 40163


:blueviolet:`紫色`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
:red:`力量`, :dodgerblue:`耐力`::

	.add 40129

:red:`敏捷`, :dodgerblue:`耐力`::

	.add 40130

:red:`敏捷`, :dodgerblue:`MP5`::

	.add 40131

:red:`SP`, :dodgerblue:`耐力`::

	.add 40132

:red:`SP`, :dodgerblue:`精神`::

	.add 40133

:red:`SP`, :dodgerblue:`MP5`::

	.add 40134

:red:`SP`, :dodgerblue:`减抗`::

	.add 40135

:red:`AP`, :dodgerblue:`耐力`::

	.add 40136

:red:`AP`, :dodgerblue:`MP5`::

	.add 40137

:red:`躲闪`, :dodgerblue:`耐力`::

	.add 40138

:red:`招架`, :dodgerblue:`耐力`::

	.add 40139

:red:`破甲`, :dodgerblue:`耐力`::

	.add 40140

:red:`精准`, :dodgerblue:`耐力`::

	.add 40141


:lime:`绿色`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
:yellow:`智力`, :dodgerblue:`耐力`::

	.add 40164

:yellow:`防御`, :dodgerblue:`耐力`::

	.add 40167

:yellow:`命中`, :dodgerblue:`耐力`::

	.add 40166

:yellow:`暴击`, :dodgerblue:`耐力`::

	.add 40165

:yellow:`急速`, :dodgerblue:`耐力`::

	.add 40168

:yellow:`韧性`, :dodgerblue:`耐力`::

	.add 40168

:yellow:`智力`, :dodgerblue:`精神`::

	.add 40170

:yellow:`命中`, :dodgerblue:`精神`::

	.add 40172

:yellow:`暴击`, :dodgerblue:`精神`::

	.add 40171

:yellow:`急速`, :dodgerblue:`精神`::

	.add 40174

:yellow:`韧性`, :dodgerblue:`精神`::

	.add 40173

:yellow:`智力`, :dodgerblue:`MP5`::

	.add 40175

:yellow:`命中`, :dodgerblue:`MP5`::

	.add 40177

:yellow:`暴击`, :dodgerblue:`MP5`::

	.add 40176

:yellow:`急速`, :dodgerblue:`MP5`::

	.add 40179

:yellow:`韧性`, :dodgerblue:`MP5`::

	.add 40178

:yellow:`命中`, :dodgerblue:`减抗`::

	.add 40181

:yellow:`暴击`, :dodgerblue:`减抗`::

	.add 40180

:yellow:`急速`, :dodgerblue:`减抗`::

	.add 40182


锻造打孔所需材料
------------------------------------------------------------------------------
锻造职业可以用锻造在 手套 和 护腕 上增加一个额外的插槽:

.. list-table::
    :widths: 10 60
    :header-rows: 1

    * - 添加物品命令
      - 说明
    * - ::

            /target player
            .add 36913 8
            .add 35627
            .add 35624
      - ::

            /target player
            .add 36913 8 萨刚锭
            .add 35627 永恒暗影
            .add 35624 永恒大地

非锻造职业可以使用锻造的物品 ``永恒腰带扣``, 为自己的腰带添加一个珠宝插槽::

    .add 41611


职业
------------------------------------------------------------------------------


牧师
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


暗影
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. list-table::
    :widths: 10 60
    :header-rows: 1

    * - 添加物品命令
      - 说明
    * - ::

            /target player
            .add 41285 1
            .add 49110 1
            .add 42144 3
            .add 40113 7
            .add 40155 5
            .add 40133 6
      - ::

            /target player
            .add 41285 1 变换 21 暴, 3% 暴击伤害
            .add 49110 1 棱彩 10 全属性
            .add 42144 3 龙眼石 红 39 法伤
            .add 40113 7 红 法伤
            .add 40155 5 橙 法伤, 急速
            .add 40133 6 紫 法伤, 精神










































































