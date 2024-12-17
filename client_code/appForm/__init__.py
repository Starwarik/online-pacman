from ._anvil_designer import appFormTemplate
from anvil import *


class appForm(appFormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def canvas_mouse_down(self, x, y, button, keys, **event_args):
    """This method is called when a mouse button is pressed on this component"""
    c = self.canvas
    print(c.get_height(), c.get_width())
    c.begin_path()
    c.move_to(100,100)
    c.line_to(100,200)
    c.line_to(200,200)
    c.close_path()
  
    c.stroke_style = "#2196F3"
    c.line_width = 3
    c.fill_style = "#E0E0E0"
  
    c.fill()
    c.stroke()