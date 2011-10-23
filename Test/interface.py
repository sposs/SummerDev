import pygtk
pygtk.require("2.0")
import gtk


class SD_APropos:
	def __init__(self):
		interface = gtk.Builder()
		interface.add_from_file('SD-APropos.glade')
		
		self.aboutdialog1 = interface.get_object("aboutdialog1")
		interface.connect_signals(self)

	def on_mainWindow_destroy(self, widget):
		gtk.main_quit()

if __name__ == "__main__":
	SD_APropos()
	gtk.main()
