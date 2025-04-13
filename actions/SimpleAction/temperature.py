# Import StreamController modules
from src.backend.PluginManager.ActionBase import ActionBase
from src.backend.DeckManagement.DeckController import DeckController
from src.backend.PageManagement.Page import Page
from src.backend.PluginManager.PluginBase import PluginBase

# Import python modules
import subprocess
import nvidia_smi
import re
﻿﻿﻿﻿
# Import gtk modules - used for the config rows
import gi
gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Gtk, Adw

class Temp(ActionBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.gpu_temp = TemperatureSensor()

    def on_ready(self) -> None:
        print(f"{self.gpu_temp.get_temperature_value()}°C")

    def on_key_down(self) -> None:
        print("Key down")

    def on_key_up(self) -> None:
        print("Key up")
