import terminatorlib.plugin as plugin
from terminatorlib.translation import _
from gi.repository import Gtk,Vte,Gdk

AVAILABLE = ['CopyAsHTML']

class CopyAsHTML(plugin.MenuItem):
	capabilities = ['terminal_menu']
	
	def __init__(self):
		plugin.MenuItem.__init__(self)
	
	def callback(self, menuitems, menu, terminal):
		copy_html_item = Gtk.MenuItem.new_with_mnemonic(_('Copy As HTML'))
		vte = terminal.get_vte()
		if not vte.get_has_selection():
			copy_html_item.set_sensitive(False)
		copy_html_item.connect("activate", self.copy_as_html, terminal)
		menuitems.append(copy_html_item)

	def copy_as_html(self, menuitem, terminal):
		vte = terminal.get_vte()
		background_color = terminal.config['background_color']		
		foreground_color = terminal.config['foreground_color']
		font_family, font_size = terminal.config['font'].rsplit(" ", 1)

		div = f'<div style="'
		div += f"background-color: {background_color}; "
		div += f"color: {foreground_color}; "
		#div += "display: inline-block; "
		#div += "padding: 10px"
		div += '">'

		pre = f'<pre style="'
		pre += f"font-family: '{font_family}'; "
		pre += f"font-size: {font_size}; "
		pre += '">'

		html = vte.get_text_selected_full(Vte.Format.HTML)[0]
		html = div + pre + html[5:]
		html = html[:-6] + "</pre></div>"

		clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)
		clipboard.set_text(html, -1)
