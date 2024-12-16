from ._anvil_designer import canvasTemplate
from anvil import *


class canvas(canvasTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    
