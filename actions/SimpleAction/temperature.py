# Import StreamController modules
from src.backend.PluginManager.ActionBase import ActionBase 
from src.backend.DeckManagement.DeckController import DeckController 
from src.backend.PageManagement.Page import Page 
from src.backend.PluginManager.PluginBase import PluginBase 

# Import python modules
import subprocess
import nvidia_smi

# Import gtk modules - used for the config rows
import gi
gi.require_version("Gtk", "4.0") 
gi.require_version("Adw", "1") 
from gi.repository import Gtk, Adw 

class TemperatureSensor:
    def __init__(self):
        self._gpu_temp = None

    def get_temperature(self):
        # Run the nvidia-smi command to get the GPU temperature
        result = subprocess.run(['nvidia-smi', '--query=GPU_TEMPERATURE'], capture_output=True, text=True)

        # Parse the output of the command and extract the temperature value
        self._gpu_temp = re.search(r"(\d+\.\d+)", result.stdout).group()

    def get_temperature_value(self):
        return self._gpu_temp

if __name__ == "__main__":
    # Create an instance of the GPU Temperature class to get your GPU temperature
    gpu_temp = GPU Temperature()


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
