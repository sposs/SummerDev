#!/usr/bin/python
import pygtk
pygtk.require("2.0")
import gtk
i=0
class Fenetre:
  def __init__(self):
    interface = gtk.Builder()
    interface.add_from_file('test2.glade')
    
    self.label1 = interface.get_object("label1")
    self.buttonQuiTue = interface.get_object("togglebutton1")
    self.button3 = interface.get_object("button3")
    self.button1 = interface.get_object("button1")
    interface.connect_signals(self)
    
  def fct_cliquer(self,widget):
    global i
    self.label1.set_text(str(i))
    i=i+1
      
  def gtk_main_quit(self, widget):
    gtk.main_quit()
    
  def button3Clicked(self,widget):
    self.button3.set_label("Je suis pas la! Va voir ailleurs!")
    self.button1.set_label("Essaye la pour voir!!")
    
  def button1Clicked(self,widget):
    self.button1.set_label("Je suis pas la! Va voir ailleurs!")
    self.button3.set_label("Essaye la pour voir!!")
    
  
Fenetre()
gtk.main()