import gi
gi.require_version("Gtk", "4.0") 
from gi.repository import Gtk

class AppWindow(Gtk.ApplicationWindow):

    def __init__(self, app):

        super(AppWindow, self).__init__(application=app)

        self.init_ui()

    def init_ui(self):

        self.set_title('Check button is clicked')

        box = Gtk.Box.new(Gtk.Orientation.VERTICAL, 0)
        box.set_margin_start(5)
        box.set_margin_top(5)

        cbtn = Gtk.CheckButton.new_with_label('Show title')
        cbtn.set_active(True)
        cbtn.connect('toggled', self.on_toggle)

        box.append(cbtn)

        self.set_child(box)
        self.set_default_size(450, 350)

    def on_toggle(self, wid):

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


'''
def on_toggle(btn):
    if btn.get_active():
        win.set_title('Check Box is clicked now')
    else:
        win.set_title('Check Box is NOT clicked now')


def on_activate(app):
    win = Gtk.ApplicationWindow(application=app)
    win.set_title('Check Box is clicked now')
    #create a box and left width is 5 and top width is 5 means buton will be in left-upper corner
    box = Gtk.Box.new(Gtk.Orientation.VERTICAL, 0)
    box.set_margin_start(10);
    box.set_margin_top(10);
    btn = Gtk.CheckButton.new_with_label('Show Title')
    btn.set_active(True) #means checkbox is ticked by default
    btn.connect('toggled', win.on_toggle,btn) #When we check or uncheck the Gtk.CheckButton, the toggled signal is emitted. We plug the on_toggle handler to the signal.
    box.append(btn)


    win.set_child(box)
    win.set_default_size(350,350);
    win.present()
'''

