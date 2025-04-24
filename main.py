# Import StreamController modules
from src.backend.PluginManager.ActionCore import ActionCore
from src.backend.PluginManager.PluginBase import PluginBase
from src.backend.PluginManager.ActionHolder import ActionHolder
from src.backend.DeckManagement.DeckController import DeckController
from src.backend.PageManagement.Page import Page

# Import actions
from .actions.SimpleAction.temperature import GpuTemp

class temperature(PluginBase):
    def __init__(self):
        super().__init__()

        ## Register actions
        self.temperature = ActionHolder(
            plugin_base = self,
            action_base = GpuTemp,
            action_id = "dev_yaoiprince_GpuTemp::temperature", # Change this to your own plugin id
            action_name = "GpuTemp",
        )
        self.add_action_holder(self.temperature)

        # Register plugin
        self.register(
            plugin_name = "GpuTemp",
            github_repo = "https://github.com/yaoiprince/GpuTemp",
            plugin_version = "1.0.0",
            app_version = "1.1.1-alpha"
        )
