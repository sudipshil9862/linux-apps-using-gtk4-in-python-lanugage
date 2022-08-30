#!/usr/bin/python3

import sys

from gi import require_version # type: ignore
require_version('Gio', '2.0')
from gi.repository import Gio # type: ignore
require_version('Gtk', '4.0')
from gi.repository import Gtk

class HelpWindow(Gtk.Window): # type: ignore
    '''
    A window to show help

    :param parent: The parent object
    :param title: Title of the help window
    :param contents: Contents of the help window
    '''
    def __init__(self,
                 parent: Gtk.Window = None,
                 title: str = '',
                 contents: str = '') -> None:
        Gtk.Window.__init__(self, title=title)
        if parent:
            self.set_parent(parent)
            self.set_transient_for(parent)
            # to receive mouse events for scrolling and for the close
            # button
            self.set_modal(True)
        self.set_destroy_with_parent(False)
        self.set_default_size(600, 500)
        self.vbox = Gtk.Box.new(Gtk.Orientation.VERTICAL, spacing=0)
        self.set_child(self.vbox)
        self.text_buffer = Gtk.TextBuffer()
        self.text_buffer.insert_at_cursor(contents)
        self.text_view = Gtk.TextView()
        self.text_view.set_buffer(self.text_buffer)
        self.text_view.set_editable(False)
        self.text_view.set_cursor_visible(False)
        self.text_view.set_justification(Gtk.Justification.LEFT)
        self.text_view.set_wrap_mode(Gtk.WrapMode.WORD)
        self.scrolledwindow = Gtk.ScrolledWindow()
        self.scrolledwindow.set_hexpand(True)
        self.scrolledwindow.set_vexpand(True)
        self.scrolledwindow.set_child(self.text_view)
        self.vbox.append(self.scrolledwindow)
        self.close_button = Gtk.Button()
        self.close_button_label = Gtk.Label()
        self.close_button_label.set_text_with_mnemonic('_Close')
        self.close_button.set_child(self.close_button_label)
        self.close_button.set_hexpand(True)
        self.close_button.set_halign(Gtk.Align.END)
        self.close_button.connect("clicked", self._on_close_button_clicked)
        self.hbox = Gtk.Box.new(Gtk.Orientation.HORIZONTAL, spacing=0)
        self.hbox.append(self.close_button)
        self.vbox.append(self.hbox)

    def _on_close_button_clicked(self, _button: Gtk.Button) -> None:
        '''
        Close the input method help window when the close button is clicked
        '''
        self.destroy()

class App(Gtk.Application):
     def __init__(self):
         Gtk.Application.__init__(self, application_id="org.gnome.example", flags=Gio.ApplicationFlags.FLAGS_NONE)
     def do_activate(self):
         text = (
             'The way a crow\n'
             'Shook down on me\n'
             'The dust of snow\n'
             'From a hemlock tree\n'
             '\n'
             'Has given my heart\n'
             'A change of mood\n'
             'And saved some part\n'
             'Of a day I had rued.\n'
             '------------------------------------------------------------'
             '------------------------------------------------------------'
             '------------------------------------------------------------'
             '------------------------------------------------------------'
             '------------------------------------------------------------\n'
             * 10
         )
         window = HelpWindow(
             parent=None,
             title='Hello World!',
             contents=text)
         self.add_window(window)
         window.show()

if __name__ == '__main__':
    app = App()
    app.run(sys.argv)

