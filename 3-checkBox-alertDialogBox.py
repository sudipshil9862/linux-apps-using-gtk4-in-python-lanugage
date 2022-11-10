import gi
gi.require_version("Gtk", "4.0") 
from gi.repository import Gtk

class CustomDialog(Gtk.Dialog):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #self.parent = kwargs.get('transient_for')

        self.set_title(title='Dialog Box')
        self.use_header_bar = True
        self.connect('response', self.dialog_response)

        self.set_width = 683
        self.set_height = 384

        self.add_buttons(
            '_Cancel', Gtk.ResponseType.CANCEL,
            '_OK', Gtk.ResponseType.OK,
        )

        btn_ok = self.get_widget_for_response(
            response_id=Gtk.ResponseType.OK,
        )
        btn_ok.get_style_context().add_class(class_name='suggested-action')
        btn_cancel = self.get_widget_for_response(
            response_id=Gtk.ResponseType.CANCEL,
        )
        btn_cancel.get_style_context().add_class(class_name='destructive-action')

        content_area = self.get_content_area()
        content_area.set_orientation(orientation=Gtk.Orientation.VERTICAL)
        content_area.set_spacing(spacing=24)
        content_area.set_margin_top(margin=12)
        content_area.set_margin_end(margin=12)
        content_area.set_margin_bottom(margin=12)
        content_area.set_margin_start(margin=12)

        self.label = Gtk.Label.new(str='press OK or CANCEL:')
        content_area.append(self.label)


    def dialog_response(self, dialog, response):
        if response == Gtk.ResponseType.OK:
            print('pressed ok')
        elif response == Gtk.ResponseType.CANCEL:
            print('pressed cancel')
            self.label.set_text(str=f'pressed CANCEL')

        dialog.close()


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

        cbtn = Gtk.CheckButton.new_with_label('Show title')
        cbtn.set_active(True)
        cbtn.connect('toggled', self.on_toggle)
        box.append(cbtn)

        self.button = Gtk.Button(label="dialog open")
        #self.button.connect("clicked", self.on_info_clicked)
        self.button.connect('clicked', self.open_dialog)
        box.append(self.button)

        #self.showWarning()
        #self.on_info_clicked()
        self.set_child(box)
        self.set_default_size(450, 350)

    def open_dialog(self, button):
        #CustomDialog is a class
        custom_dialog = CustomDialog(transient_for=self, use_header_bar=True)
        custom_dialog.present()

    '''
    def	showWarning(self):
        self.message = Gtk.MessageDialog(title = 'Warning', text = 'Something has gone wrong')
        self.message.add_buttons('OK', 1)	
        self.message.set_transient_for(self)	# Makes the dialog always appear in front of the parent window
        self.message.set_modal(self)	        # Makes the parent	window unresponsive while dialog is showing
        self.message.show()
    '''

    '''
    def on_info_clicked(self, button):
        self.dialog = Gtk.MessageDialog(
            transient_for=self,
            message_type=Gtk.MessageType.INFO,
            buttons=Gtk.ButtonsType.OK,
            text="This is an INFO MessageDialog",
        )
        #dialog.run()
        self.response = self.dialog.show()
        if self.response == Gtk.ResponseType.OK:
            print("WARN dialog closed by clicking OK button")
        print("INFO dialog closed")
        self.dialog.destroy()

    '''

    def on_toggle(self, wid):

        if wid.get_active():
            self.set_title('CheckButton is clicked')
        else:
            self.set_title('CheckButton is NOT clicked')


'''
#another way of check button - after one button clicked hello function starts and here we have check button functions
def hello(self, button):
    print("Hello world")
    if self.check.get_active():
        print("Goodbye world!")
        self.close()
'''

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

