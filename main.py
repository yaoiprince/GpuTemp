# Import StreamController modules
from src.backend.PluginManager.ActionBase import ActionBase
from src.backend.DeckManagement.DeckController import DeckController
from src.backend.PageManagement.Page import Page
from src.backend.PluginManager.PluginBase import PluginBase

# Import actions from your own module
from .actions.SimpleAction.temperature import Temp

class PluginTemplate(PluginBase):
    def __init__(self):
        super().__init__()

        ## register actions
        self.gpu_action = ActionHolder(
            plugin_base = self,
            action_base = Temp,
            action_id = "dev_yaoiprince_GpuTemp::temperature",  # change this to your own plugin id
            action_name = "GPU Temperature",
        )
        self.add_action_holder(self.gpu_action)

        # register plugin
        self.register(
            plugin_name = "GpuTemp",
            github_repo = "https://github.com/yaoiprince/GpuTemp",
            plugin_version = "1.0.0",
            app_version = "1.1.1-alpha"
        )
