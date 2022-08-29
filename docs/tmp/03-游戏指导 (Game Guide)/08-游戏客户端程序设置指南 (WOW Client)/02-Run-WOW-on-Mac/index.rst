.. _RunWowOnMac:

Run WOW (Wrath of the Lich King) on Mac Computer (在Mac电脑上运行魔兽世界)
==============================================================================


English
------------------------------------------------------------------------------

1. Download from client from https://www.warmane.com/download.
2. Drag the entire folder ``Wrath of the Lich King 3.3.5a (Mac)`` into Mac's Application folder.

In Windows, there's ``WOW.exe`` file, it is single, executable file. But in MacOS, it is an application, each application is actually set of files and folder, and there's only one executable binary file for this APP (Correspond to .exe file)

3. Right click ``World of Warcraft`` (or ``World of Warcraft.app``), click ``Show Package Contents``.
4. Go to ``World of Warcraft/Contents/MacOS`` there's a executable binary file ``World of Warcraft``, but our system doesn't recognize it yet.
5. Open a ``Terminal`` App, its in Launchpad -> Other -> Terminal.
6. Just copy (``Cmd + C``) the ``World of Warcraft`` File.
7. In ``Terminal``, Enter ``chmod +x `` (There's a space at the end) and paste (``Cmd + V``), then the Path of ``World of Warcraft`` are automatically copied with escape keys, you will see something like ``chmod +x /Applications/Wrath\ of\ the\ Lich\ King\ 3.3.5a\ \(Mac\)/World\ of\ Warcraft.app/Contents/MacOS/World\ of\ Warcraft``, and enter. This command tells your system that ``World of Warcraft`` is an executable binary file.
8. Then you can double click ``World of Warcraft.app`` to start the game, or you can drag it to your icon docker.

If you want to open 2 windows at same time, you could create a copy of the ``World of Warcraft.app``, so you can rename it to a new name, and use this as your second window.


中文
------------------------------------------------------------------------------

1. 在 https://www.warmane.com/download 下载Mac客户端。
2. 将整个 ``Wrath of the Lich King 3.3.5a (Mac)`` 文件夹移动到 ``/Applications`` 目录下，像这个样子 ``/Application/Wrath of the Lich King 3.3.5a (Mac)``。

在Windows里，WOW.exe文件是一个可执行文件，而在Mac里，每一个Application实际上是一个文件夹，里面包含了许多文件和文件夹。而其中必然有一个可执行文件用于启动这个App。

3. 右键点击 ``World of Warcraft`` (或 ``World of Warcraft.app``)，点击 ``Show Package Contents``。
4. 进入 ``World of Warcraft/Contents/MacOS`` 文件夹，里面有一个可执行文件 ``World of Warcraft``，可是我们的系统还并不知道这点。
5. 打开一个终端App，在你的Launchpad里，Other里可以找到这个App。
6. 选中 ``World of Warcraft`` 文件并复制 (``Cmd + C``)。
7. 在终端里输入 ``chmod +x `` 然后按粘贴 (``Cmd + V``)，这会将该文件的整个路径复制到终端里。最后命令看起来会像这个样子: ``chmod +x /Applications/Wrath\ of\ the\ Lich\ King\ 3.3.5a\ \(Mac\)/World\ of\ Warcraft.app/Contents/MacOS/World\ of\ Warcraft``。然后按下回车。这个命令是告诉系统，这个文件是一个可执行文件！以后可以双击运行了！
8. 然后你可以直接点击 ``World of Warcraft.app`` 来启动游戏，或者将其拖到Dock上来快速启动。

如果你想双开（开多个窗口），那么你可以复制一份 ``World of Warcraft.app`` 然后重命名为新的名字，用不同的 App 在不同的窗口中运行游戏即可。
