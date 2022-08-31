import gi
gi.require_version("Gtk", "4.0") 
from gi.repository import Gtk, Pango

#making the code into classes cause doing it in functional style is a little python.
class AppWindow(Gtk.ApplicationWindow):

    def __init__(self, app):

        super(AppWindow, self).__init__(application=app)

        self.init_ui()

    def init_ui(self):

        self.set_title('Change Font')

        
        self.box = Gtk.Box.new(Gtk.Orientation.VERTICAL, 0)
        #box.set_margin_start(5)
        #box.set_margin_top(5)

        #self.label = Gtk.Label(label="Hello World")
        self.label = Gtk.Label(label="Hello World")
        #self.label.get_font_markup('Noto Sans Regular 20', f'Hello World')
        #self.button = Gtk.Button(label='Select font')
        self.button = Gtk.FontButton.new()
        self.button.set_title(title='Select Font')
        self.button.connect('font-set', self.on_font_button_font_set)
        self.box.append(self.label)
        self.box.append(self.button)

        self.set_child(self.box) #box into wndow
        self.set_default_size(750, 750)
    
    def on_font_button_font_set(self, button):
        pango_font_description = Pango.FontDescription.from_string(str=button.get_font(),)

        pango_attr_font_desc = Pango.AttrFontDesc.new(desc=pango_font_description,)

        pango_attr_list = Pango.AttrList.new()
        pango_attr_list.insert(attr=pango_attr_font_desc)

        self.label.set_attributes(attrs=pango_attr_list)

        '''
        fontchooserdialog = Gtk.FontChooserDialog()
        fontchooserdialog.set_title("Select Font")
        response = fontchooserdialog.run()
        if response == Gtk.ResponseType.OK:
            print("Font Selected: %s" % fontchooserdialog.get_font())
        fontchooserdialog.destroy()
        '''
        #picker = gtk_font_button_new();
        #font = "Sans Regular 50";
        #gtk_font_chooser_set_font(picker, font);


def on_activate(app):

    win = AppWindow(app)
    win.present()


app = Gtk.Application(application_id='org.gtk.Example')
app.connect('activate', on_activate)
app.run(None)


