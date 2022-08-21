import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk


class AppWindow(Gtk.ApplicationWindow):

    def __init__(self, app):

        super(AppWindow, self).__init__(application=app)

        self.init_ui()

    def init_ui(self):

        self.set_title('Quit button')

        vbox = Gtk.Box.new(Gtk.Orientation.VERTICAL, 10)
        hbox = Gtk.Box.new(Gtk.Orientation.HORIZONTAL, 10)

        vbox.set_margin_start(20)
        vbox.set_margin_top(20)
        vbox.set_margin_end(20)
        vbox.set_margin_bottom(20)
        
        #create a GTk.Entry widget
        self.entry = Gtk.Entry()
        hbox.append(self.entry)

        #to be able to process key events, we create a Gtk.EventControllerKey. we react to the on_key_released events
        keycont = Gtk.EventControllerKey()
        keycont.connect('key-released', self.on_key_released)
        self.add_controller(keycont)

        self.label = Gtk.Label.new('...')
        hbox.append(self.label)

        self.set_title('Gtk Entry - Simultaneous Typing')
        self.set_default_size(450, 350)

        vbox.append(hbox)
        self.set_child(vbox)


    def on_key_released(self, *_):
        self.label.set_text(self.entry.get_text())


def on_activate(app):

    win = AppWindow(app)
    win.present()


app = Gtk.Application(application_id='org.gtk.Example')
app.connect('activate', on_activate)
app.run(None)
