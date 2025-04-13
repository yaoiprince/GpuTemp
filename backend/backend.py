from streamcontroller_plugin_tools import BackendBase 

class Backend(BackendBase):
    def __init__(self):
        super().__init__()
        
        nvidia_smi.nvmlInit()
        handle = nvidia_smi.nvmlDeviceGetHandleByIndex(0)

backend = Backend()
