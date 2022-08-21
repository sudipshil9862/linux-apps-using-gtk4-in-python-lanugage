import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk, Gio


class AppWindow(Gtk.ApplicationWindow):

    def __init__(self, app):

        super(AppWindow, self).__init__(application=app)

        self.init_ui(app)

    def init_ui(self, app):

        self.set_title('Simple menu')

        main = Gio.Menu.new()
        fmi = Gio.MenuItem.new('File')

        menu = Gio.Menu.new()
        emi = Gio.MenuItem.new('Exit', 'app.quit')
        menu.append_item(emi)

        fmi.set_submenu(menu)
        main.append_item(fmi)

        app.set_menubar(main)

        act_quit = Gio.SimpleAction.new('quit', None)
        Gio.ActionMap.add_action(app, act_quit)
        act_quit.connect('activate', self.on_close, app)

        self.set_show_menubar(True)
        self.set_default_size(350, 250)

    def on_close(self, *_):
        self.close()


def on_activate(app):

    win = AppWindow(app)
    win.present()


app = Gtk.Application(application_id='org.gtk.Example')
app.connect('activate', on_activate)
app.run(None)
