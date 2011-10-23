import os
import gtk
import vte
import time



window = gtk.Window()
window.connect('destroy', lambda w: gtk.main_quit())

terminal = vte.Terminal()


child_pid = terminal.fork_command()

window.add(terminal)
window.show_all()
gtk.main()
