import gi
gi.require_version("Gtk", "4.0") 
from gi.repository import Gtk

class AppWindow(Gtk.ApplicationWindow):

    def __init__(self, app):

        super(AppWindow, self).__init__(application=app)

        self.init_ui()

    def init_ui(self):

        self.set_title('Check button is clicked')

        
        self.box = Gtk.Box.new(Gtk.Orientation.VERTICAL, 0)
        #box.set_margin_start(5)
        #box.set_margin_top(5)

        #alert_box
        self.button1 = Gtk.Button(label="open dialog")
        self.button1.connect('clicked', self.fun_dialog())
        
        self.box.append(button)
        
       
        self.set_child(self.box) #box into wndow
        self.set_default_size(450, 450)


    #dialog buttons clicked action
    def fun_dialog(self):
        '''
        dialog = Gtk.dialog_new()
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            print("The OK button was clicked")
        if response == Gtk.ResponseType.CANCEL:
            print("The CANCEL button was clicked")
        dialog.destroy()
        '''
        window = self.get_toplevel()
        dialog = gtk.Dialog(_('Rename Window'), window,
                        gtk.DIALOG_MODAL,
                        ( gtk.STOCK_CANCEL, gtk.RESPONSE_REJECT,
                          gtk.STOCK_OK, gtk.RESPONSE_ACCEPT ))
        dialog.set_default_response(gtk.RESPONSE_ACCEPT)
        dialog.set_has_separator(False)
        dialog.set_resizable(False)
        dialog.set_border_width(8)

        label = gtk.Label(_('Enter a new title for the Terminator window...'))
        name = gtk.Entry()
        name.set_activates_default(True)
        if window.title.text != self.vte.get_window_title():
            name.set_text(self.get_toplevel().title.text)

        dialog.vbox.pack_start(label, False, False, 6)
        dialog.vbox.pack_start(name, False, False, 6)

        dialog.show_all()
        res = dialog.run()
        if res == gtk.RESPONSE_ACCEPT:
            if name.get_text():
                window.title.force_title(None)
                window.title.force_title(name.get_text())
            else:
                window.title.force_title(None)
        dialog.destroy()
        return


def on_activate(app):

    win = AppWindow(app)
    win.present()


app = Gtk.Application(application_id='org.gtk.Example')
app.connect('activate', on_activate)
app.run(None)


