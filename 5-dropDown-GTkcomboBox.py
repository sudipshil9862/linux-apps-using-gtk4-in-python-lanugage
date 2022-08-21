import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk


class AppWindow(Gtk.ApplicationWindow):

    def __init__(self, app):

        super(AppWindow, self).__init__(application=app)

        self.init_ui()

    def init_ui(self):

        self.set_title('Quit button')

        vbox = Gtk.Box.new(Gtk.Orientation.VERTICAL, 8)
        hbox = Gtk.Box.new(Gtk.Orientation.HORIZONTAL, 8)

        combo = Gtk.ComboBoxText()  #initiazing drop down widget

        vbox.set_margin_start(5)
        vbox.set_margin_top(5)
        hbox.append(combo)

        combo.connect('changed', self.on_changed)

        combo.append_text('Fedora34')
        combo.append_text('Fedora35')
        combo.append_text('Fedora36')
        combo.append_text('Fedora37')
        combo.append_text('Fedora38')
        
        self.label = Gtk.Label.new('Fedora34')
        hbox.append(self.label)

        self.set_title('DropDown - ComboBoxText')
        self.set_default_size(450, 450)

        vbox.append(hbox)
        self.set_child(vbox)

    def on_changed(self, wid):

        self.label.set_label(wid.get_active_text())


def on_activate(app):

    win = AppWindow(app)
    win.present()


app = Gtk.Application(application_id='org.gtk.Example')
app.connect('activate', on_activate)
app.run(None)
