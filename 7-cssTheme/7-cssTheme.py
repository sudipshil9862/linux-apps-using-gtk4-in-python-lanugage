import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk, Gio


class AppWindow(Gtk.ApplicationWindow):

    def __init__(self, app):

        super(AppWindow, self).__init__(application=app)

        self.init_ui()

    def init_ui(self):

        self.set_title('CSS theme')

        box = Gtk.Box.new(Gtk.Orientation.VERTICAL, 0)

        btn = Gtk.Button(label="Quit")
        btn.connect('clicked', lambda _: self.close())

        btn.set_margin_start(5)
        btn.set_margin_top(5)
        btn.set_halign(Gtk.Align.START)

        box.append(btn)

        self.set_child(box)
        self.set_default_size(350, 250)


def on_activate(app):

    win = AppWindow(app)

    display = Gtk.Widget.get_display(win)
    provider = Gtk.CssProvider.new()
    fname = Gio.file_new_for_path('theme.css')
    provider.load_from_file(fname)
    Gtk.StyleContext.add_provider_for_display(display, provider,
        Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

    win.present()


app = Gtk.Application(application_id='org.gtk.Example')
app.connect('activate', on_activate)
app.run(None)
