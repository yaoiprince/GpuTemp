# Import StreamController modules
from src.backend.PluginManager.ActionBase import ActionBase 
from src.backend.DeckManagement.DeckController import DeckController 
from src.backend.PageManagement.Page import Page 
from src.backend.PluginManager.PluginBase import PluginBase 

# Import python modules
import nvidia-smi
import subprocess
import re

nvidia_smi.nvmlInit() handle = nvidia_smi.nvmlDeviceGetHandleByIndex(0) 

class TemperatureSensor:
    def __init__(self):
        self._gpu_temp = None

    def get_temperature(self):
        # Run the nvidia-smi command to get the GPU temperature
        result = subprocess.run(['nvidia-smi', '--query=GPU_TEMPERATURE'], capture_output=True, text=True)

        # Parse the output of the command and extract the temperature value
        self._gpu_temp = re.search(r"(\d+\.\d+)", result.stdout).group()

    def get_temperature_value(self):
        return float(self._gpu_temp)  # Convert to a float for easier use

if __name__ == "__main__":
    # Create an instance of the GPU Temperature class to get your GPU temperature
    gpu_temp = TemperatureSensor()

class GpuTemp(ActionBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.gpu_temp = TemperatureSensor()

    def on_ready(self) -> None:
        print(f"{self.gpu_temp.get_temperature_value()}°C")

    def on_key_down(self) -> None:
        print("Key down") 

    def on_key_up(self) -> None:
        print("Key up")
