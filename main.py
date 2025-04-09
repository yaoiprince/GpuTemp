# import StreamController modules
from src.backend.PluginManager.ActionBase import ActionBase
from src.backend.DeckManagement.DeckController import DeckController
from src.backend.PageManagement.Page import Page
from src.backend.PluginManager.PluginBase import PluginBase

# import actions
from .actions.SimpleAction.NvidiaGpu import GpuTemp

class PluginTemplate(PluginBase):
    def __init__(self):
        super().__init__()

        ## register actions
        self.gpu_action = ActionHolder(
            plugin_base = self,
            action_base = GpuTemp,
            action_id = "dev_yaoiprince_GpuTemp::GpuTemp", # change this to your own plugin id
            action_name = "Gpu Temperature",
        )
        self.add_action_holder(self.gpu_action)

        # register plugin
        self.register(
            plugin_name = "GpuTemp",
            github_repo = "https://github.com/yaoiprince/GpuTemp",
            plugin_version = "1.0.0",
            app_version = "1.1.1-alpha"
        )
