#!/usr/bin/python

import os
import gtk
import vte
import pygtk
pygtk.require("2.0")


class MainWindow:
  
  def __init__(self):
    mainInterface = gtk.Builder()
    mainInterface.add_from_file("SD_mainWindow.glade")
    
    #liste de tous les buttons et objets en tout genre en attribut de la classe
    
    MainInterface.connect_signals(self)
    
  def mainWindowQuit(self,widget):
    gtk.main_quit()
    
    
    