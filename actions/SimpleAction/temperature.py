# Import StreamController modules
from src.backend.PluginManager.ActionBase import ActionBase
from src.backend.PluginManager.PluginBase import PluginBase
from src.backend.PluginManager.ActionHolder import ActionHolder

from nvidia_ml_py import nvidia_smi
import pynvml
import subprocess

# Import gtk modules - used for the config rows
import gi
gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Gtk, Adw

class temp(ActionBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.gpu_temp_sensor = TemperatureSensor()

    def on_ready(self) -> None:
        try:
            print(f"{gpu_temp}°C")
        except Exception as e:
            print(e)

    def on_key_down(self) -> None:
        try:
            print(f"GPU Temperature: {gpu_temp}°C")
            # You can also display this temperature in the StreamController UI if available
        except Exception as e:
            print(e)

    def on_key_up(self) -> None:
        print("Key up")

# Example usage
if __name__ == "main":
    plugin = Temp()
    plugin.on_ready()  # This will output the current GPU temperature
