from ._anvil_designer import Form1Template
from anvil import *


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    canvas = Canvas()
    canvas.background = "red"
    self.linear_panel_1.add_component(canvas)
