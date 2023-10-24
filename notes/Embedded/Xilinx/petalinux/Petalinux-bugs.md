


# \[FIX\] using a remote ssh session with x-11 forwarding

You will have to edit the terminal.py script (for Petalinux on the A53 core in a ZYNQ ultrascale this would be in the aarch64 branch)
eg. <path-to-petalinux-install>/2019.1/components/yocto/source/aarch64/layers/core/meta/lib/oe/terminal.py
Edit the class Gnome(XTerminal): as follows:
class Gnome(XTerminal):
#command = 'gnome-terminal -t "{title}" -x {command}'
command = 'dbus-launch gnome-terminal -x {command}' # use dbus, -t no longer supported
priority = 2
def __init__(self, sh_cmd, title=None, env=None, d=None):
...
The scripting should be able to launch a new terminal now.