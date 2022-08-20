import gi
gi.require_version("Gtk", "4.0") 
from gi.repository import Gtk

def on_activate(app):
    win = Gtk.ApplicationWindow(application=app)
    win.set_title('Image')
    image = Gtk.Image.new_from_file('/home/sshil/Pictures/Wallpapers/rabbit.jpg');
    win.set_child(image)

    win.set_default_size(350,350);
    win.present()

app = Gtk.Application(application_id='org.gtk.Example')
app.connect('activate', on_activate)
app.run(None)
