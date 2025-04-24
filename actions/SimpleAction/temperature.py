# Import StreamController modules
from src.backend.PluginManager.ActionBase import ActionBase
from src.backend.PluginManager.PluginBase import PluginBase
from src.backend.PluginManager.ActionHolder import ActionHolder
from pynvml import *

import nvidia_smi
import subprocess

# Import gtk modules - used for the config rows
import gi
gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Gtk, Adw

class GpuTemp(ActionBase):
    def __init__(self, *args, **kwargs):
    	nvmlInit()
        super().__init__(*args, **kwargs)

    def on_ready(self) -> None:
        try:
        nvmlDeviceGetCount()
        except NVMLError as error:
	print(error)
            print(f"{gpu_temp}°C")

    def on_key_down(self) -> None:
        print("Key down")

    def on_key_up(self) -> None:
        print("Key up")

# Example usage
if __name__ == "main":
    plugin = Temp()
    plugin.on_ready()  # This will output the current GPU temperature
