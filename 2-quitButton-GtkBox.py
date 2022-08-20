import gi
gi.require_version("Gtk", "4.0") 
from gi.repository import Gtk

def on_activate(app):
    win = Gtk.ApplicationWindow(application=app)
    win.set_title('Quit Button and GtkBox')
    #create a box and left width is 5 and top width is 5 means buton will be in left-upper corner
    box = Gtk.Box.new(Gtk.Orientation.VERTICAL, 0)
    box.set_margin_start(5);
    box.set_margin_top(5);
    btn = Gtk.Button(label="Quit")
    btn.connect('clicked', lambda x: win.close())
    btn.set_halign(Gtk.Align.START)
    box.append(btn)


    win.set_child(box)
    win.set_default_size(350,350);
    win.present()

app = Gtk.Application(application_id='org.gtk.Example')
app.connect('activate', on_activate)
app.run(None)
