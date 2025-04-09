# import StreamController modules
from src.backend.PluginManager.ActionBase import ActionBase
from src.backend.DeckManagement.DeckController import DeckController
from src.backend.PageManagement.Page import Page
from src.backend.PluginManager.PluginBase import PluginBase

# import actions
from .actions.SimpleAction.GpuTemp import Gpu

# import pyNVML
import nvidia_smi

nvidia_smi.nvmlInit()
handle = nvidia_smi.nvmlDeviceGetHandleByIndex(0)

nvidia-smi -q –d CLOCK

class PluginTemplate(PluginBase):
    def __init__(self):
        super().__init__()

        ## register actions
        self.simple_action_holder = ActionHolder(
            plugin_base = self,
            action_base = Gpu,
            action_id = "dev_yaoiprince_GpuTemp::GpuTemp", # change this to your own plugin id
            action_name = "Gpu Temperature",
        )
        self.add_action_holder(self.simple_action_holder)

        # register plugin
        self.register(
            plugin_name = "GpuTemp",
            github_repo = "https://github.com/yaoiprince/GpuTemp",
            plugin_version = "1.0.0",
            app_version = "1.1.1-alpha"
        )
