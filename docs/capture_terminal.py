"""Run a mission in a real GTK/VTE terminal and screenshot its X11 window."""
import os
os.environ['GDK_BACKEND'] = 'x11'
import sys
from pathlib import Path
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Vte', '2.91')
from gi.repository import Gtk, Vte, GLib, Gdk, Pango
root = Path(__file__).resolve().parent.parent
name = sys.argv[1]
assert name in ('mission1', 'mission2', 'mission3', 'mission4')
window = Gtk.Window(title=f'24i-3166 - python {name}.py')
terminal = Vte.Terminal()
terminal.set_font(Pango.FontDescription('Monospace 14'))
terminal.set_size(115, {'mission1':7,'mission2':31,'mission3':11,'mission4':13}[name])
window.add(terminal)
window.show_all()
def screenshot():
    surface = window.get_window()
    shot = Gdk.pixbuf_get_from_window(surface, 0, 0, surface.get_width(), surface.get_height())
    shot.savev(str(root / f'DemonHunt_data/output/{name}_output.png'), 'png', [], [])
    Gtk.main_quit()
    return False
def finished(term, status):
    if status != 0:
        raise RuntimeError(f'Mission failed: {status}')
    GLib.timeout_add(600, screenshot)
terminal.connect('child-exited', finished)
# bash xtrace shows the command actually executed, and tee preserves identical stdout.
command = f'set -o pipefail; set -x; python {name}.py | tee ../output/{name}.txt'
terminal.spawn_async(Vte.PtyFlags.DEFAULT, str(root / 'DemonHunt_data/starter'),
                     ['/bin/bash', '-c', command], None, GLib.SpawnFlags.DEFAULT,
                     None, None, -1, None, None, None)
Gtk.main()
