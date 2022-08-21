import gi
gi.require_version("Gtk", "4.0") 
from gi.repository import Gtk

#making the code into classes cause doing it in functional style is a little python.
class AppWindow(Gtk.ApplicationWindow):

    def __init__(self, app):

        super(AppWindow, self).__init__(application=app)

        self.init_ui()

    def init_ui(self):

        self.set_title('Check button is clicked')

        box = Gtk.Box.new(Gtk.Orientation.VERTICAL, 0)
        box.set_margin_start(5)
        box.set_margin_top(5)

        #Check buttons can be turned into radio buttons by adding them to a group

        rbtn1 = Gtk.CheckButton.new_with_label('test')
        rbtn2 = Gtk.CheckButton.new_with_label('test')
        rbtn3 = Gtk.CheckButton.new_with_label('test')
        rbtn2.set_group(rbtn1)
        rbtn3.set_group(rbtn1)
        #btn.set_active(True)
        rbtn1.connect('toggled', self.radio_toggle)

        box.append(rbtn1)

        self.set_child(box)
        self.set_default_size(450, 450)

    def radio_toggle(self, wid):

        if wid.get_active():
            self.set_title('CheckButton is clicked')
        else:
            self.set_title('CheckButton is NOT clicked')


def on_activate(app):

    win = AppWindow(app)
    win.present()


app = Gtk.Application(application_id='org.gtk.Example')
app.connect('activate', on_activate)
app.run(None)


