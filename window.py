import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, WebKit2

class MyBrowser(Gtk.Window):
    def __init__(self):
        super().__init__(title="Simple Browser")
        self.set_default_size(800, 600)

        # Create a VBox to hold the web view and address bar
        vbox = Gtk.VBox()
        self.add(vbox)

        # Create an address bar
        self.entry = Gtk.Entry()
        self.entry.connect("activate", self.load_url)
        vbox.pack_start(self.entry, False, False, 0)

        # Create a web view
        self.webview = WebKit2.WebView()
        vbox.pack_start(self.webview, True, True, 0)

        # Load a default URL
        self.load_url("https://www.google.com")

    def load_url(self, widget=None, event=None):
        url = self.entry.get_text()
        self.webview.load_uri(url)

if __name__ == "__main__":
    win = MyBrowser()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()


