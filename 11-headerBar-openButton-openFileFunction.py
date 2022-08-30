import gi
gi.require_version("Gtk", "4.0") 
from gi.repository import Gtk

#making the code into classes cause doing it in functional style is a little python.
class AppWindow(Gtk.ApplicationWindow):

    def __init__(self, app):

        super(AppWindow, self).__init__(application=app)

        self.init_ui()

    def init_ui(self):

        self.set_title('Header Box')

        
        self.box = Gtk.Box.new(Gtk.Orientation.VERTICAL, 0)
        #box.set_margin_start(5)
        #box.set_margin_top(5)

        self.header = Gtk.HeaderBar()
        self.set_titlebar(self.header)
        #adding button to headerBar
        self.button = Gtk.Button(label='Open')
        self.header.pack_start(self.button) #add button in header bar
        self.button.set_icon_name("document-open-symbolic") #icon image of the button in headerbar
        #open dialog after button click
        self.open_dialog = Gtk.FileChooserNative.new(title="Choose a file", parent=self, action=Gtk.FileChooserAction.OPEN)
        self.open_dialog.connect('response', self.open_response) #button function
        self.button.connect('clicked', self.show_open_dialog) #button function
        
        self.box.append(self.header)  #slider into box

        self.set_child(self.box) #box into wndow
        self.set_default_size(450, 450)

    def open_response(self, dialog, response):
        if response == Gtk.ResponseType.ACCEPT:
            file = dialog.get_file()
            filename = file.get_path()
            print(filename) #here is the operation I can write what to do after file select

    def show_open_dialog(self, button):
        self.open_dialog.show()

    def slider_changed(self, slider):
        print(int(slider.get_value()))


    def switch_switched(self, switch, state):
        print(f"The switch has been switched {'on' if state else 'off'}")
        '''
        if(state):
            self.set_title('switch button is clicked')
        else:
            self.set_title('switch button is NOT clicked')
        '''

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


