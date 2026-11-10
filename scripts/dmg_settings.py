# dmgbuild settings: DHbox.app next to an Applications shortcut.
import os
app = os.environ["DHBOX_APP"]
format = "UDZO"
filesystem = "HFS+"
files = [app]
symlinks = {"Applications": "/Applications"}
icon_locations = {"DHbox.app": (160, 190), "Applications": (480, 190)}
window_rect = ((200, 200), (640, 400))
icon_size = 128
text_size = 14
default_view = "icon-view"
show_icon_preview = False
show_status_bar = False
show_tab_view = False
show_toolbar = False
show_pathbar = False
show_sidebar = False
