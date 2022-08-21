import gi  #gi. repository is the python module for PyGObject
gi.require_version("Gtk", "4.0") 
from gi.repository import Gtk

def on_activate(app):
    win = Gtk.ApplicationWindow(application=app)
    win.set_title('first application in python in gtk4')
    win.set_default_size(350,350);

    btn = Gtk.Button(label="Hello, World!")
    btn.connect('clicked', lambda x: win.close())
    win.set_child(btn)

    win.present()

app = Gtk.Application(application_id='org.gtk.Example')  #sometimes we just don't need to write id just the function
app.connect('activate', on_activate)
app.run(None)
