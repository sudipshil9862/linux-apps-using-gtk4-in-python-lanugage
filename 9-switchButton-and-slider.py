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

        
        self.box = Gtk.Box.new(Gtk.Orientation.VERTICAL, 0)
        #box.set_margin_start(5)
        #box.set_margin_top(5)

        #Check buttons can be turned into radio buttons by adding them to a group

        rbtn1 = Gtk.CheckButton.new_with_label('test')
        rbtn2 = Gtk.CheckButton.new_with_label('test')
        rbtn3 = Gtk.CheckButton.new_with_label('test')
        rbtn2.set_group(rbtn1)
        rbtn3.set_group(rbtn1)
        rbtn1.set_active(True)
        rbtn1.connect('toggled', self.radio_toggle)

        self.box.append(rbtn1)
        
        #switch button/switch box

        self.switch_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.switch = Gtk.Switch()
        self.switch.set_active(True) #default to on
        self.switch.connect("state-set", self.switch_switched)  #switch_switched function
        self.switch_box.append(self.switch) #switch button under switch box

        self.label = Gtk.Label(label = "A Switch")
        self.switch_box.append(self.label) #switch name/label into switch box
        self.switch_box.set_spacing(20) #switch box spacing

        self.box.append(self.switch_box) #switch box into main box

        #slider
        self.slider = Gtk.Scale()
        self.slider.set_digits(0) #no of decimal places to use
        self.slider.set_range(0,20)
        self.slider.set_draw_value(True) #showing current value in slider
        self.slider.set_value(5) #set initial value
        self.slider.connect('value-changed', self.slider_changed)
        self.box.append(self.slider)  #slider into box

        self.set_child(self.box) #box into wndow
        self.set_default_size(450, 450)

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


