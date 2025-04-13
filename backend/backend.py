from streamcontroller_plugin_tools import BackendBase 

class Backend(BackendBase):
    def __init__(self):
        super().__init__()
        
        nvidia_smi.nvmlInit()
        handle = nvidia_smi.nvmlDeviceGetHandleByIndex(0)
        
class TemperatureSensor:
    def __init__(self):﻿
        self._gpu_temp = None

    def get_temperature(self):
        # Run the nvidia-smi command to get the GPU temperature
        result = subprocess.run(['nvidia-smi', '--query=GPU_TEMPERATURE'], capture_output=True, text=True)
﻿
        # Parse the output of the command and extract the temperat﻿ure value
        self._gpu_temp = r﻿e.sea﻿rch(r"(\d+\.\d+)", result.st﻿d﻿﻿out).group()

    def get_temperature_value(self):
        return self._gpu_temp

if __name__ == "__main__":
    # Create an instance of the GPU Temperature class to get your GPU temperature
    gpu_temp = GPU Temperature()

backend = Backend()
