# Import StreamController modules
from src.backend.PluginManager.ActionBase import ActionBase
from src.backend.PluginManager.PluginBase import PluginBase

# Import actions
from .actions.SimpleAction.temperature import Temp

class PluginTemplate(PluginBase):
    def __init__(self):
        super().__init__()

        ## Register actions
        self.temperature = ActionHolder(
            plugin_base = self,
            action_base = Temp,
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
