from streamcontroller_plugin_tools import BackendBase
from pynvml import *

import nvidia_smi
import subprocess

class Backend(BackendBase):
    def __init__(self):
        super().__init__()

        nvsmi = nvidia_smi.getInstance()
        nvidia_smi.nvmlInit()
        handle = nvidia_smi.nvmlDeviceGetHandleByIndex(0)

class TemperatureSensor:
    def __init__(self):
	nvmlInit()

    def get_temperature(self):
        # Run the nvidia-smi command to get the GPU temperature
        result = subprocess.run(['nvidia-smi -q -d TEMPERATURE'], capture_output=True, text=True)

        # Parse the output of the command and extract the temperat﻿ure value
        self.gpu_temp = re.search(r"(\d+\.\d+)", result.stdout).group()

    def get_temperature_value(self):
        return float(self._gpu_temp)

    if __name__ == "main":
	# Create an instance of the GPU Temperature class to get your GPU temperature
	gpu_temp_sensor = TemperatureSensor()
	gpu_temp_sensor.get_temperature()

    print(f"GPU Temp: {gpu_temp_sensor.get_temperature_value()}°C")

backend = Backend()
