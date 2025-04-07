# Import StreamController modules
from src.backend.PluginManager.ActionBase import ActionBase
from src.backend.DeckManagement.DeckController import DeckController
from src.backend.PageManagement.Page import Page
from src.backend.PluginManager.PluginBase import PluginBase

# Import actions
from .actions.SimpleAction.GpuTemp import GPU

class PluginTemplate(PluginBase):
    def __init__(self):
        super().__init__()

        ## Register actions
        self.simple_action_holder = ActionHolder(
            plugin_base = self,
            action_base = GPU,
            action_id = "dev_yaoiprince_GpuTemp::GpuTemp", # Change this to your own plugin id
            action_name = "Gpu Temperature",
        )
        self.add_action_holder(self.simple_action_holder)

        # Register plugin
        self.register(
            plugin_name = "GpuTemp",
            github_repo = "https://github.com/yaoiprince/GpuTemp",
            plugin_version = "1.0.0",
            app_version = "1.1.1-alpha"
        )
