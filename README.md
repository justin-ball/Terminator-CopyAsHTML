# Terminator-CopyAsHTML
[Terminator](https://github.com/gnome-terminator/terminator) plugin that allows you to copy the selected text as HTML

![images/Screenshot_Menu.png?raw=true](https://github.com/justin-ball/Terminator-CopyAsHTML/blob/43fd95fae0b1806e6ca8bd4d647764a593427a0c/images/Screenshot_Menu.png)

While the feature request for Terminator to natively support "Copy As HTML" (see [Copy as HTML [Feature Request] #754](https://github.com/gnome-terminator/terminator/issues/754)), this plugin does the same thing.

# Installing the plugin
A plugin can be installed by adding the `copyAsHTML.py` python file in one of two locations:

- `/usr/[local/]share/terminator/terminatorlib/plugins/`
This will need root permissions to do. The optional local/ is usually for packages installed by hand, rather than through the package manager, and this depends on how Terminator was installed on your system.
- `~/.config/terminator/plugins/`
This allows you to use plugins without needing root.
