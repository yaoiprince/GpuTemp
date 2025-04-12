# Import StreamController modules
from src.backend.PluginManager.ActionBase import ActionBase 
from src.backend.DeckManagement.DeckController import DeckController 
from src.backend.PageManagement.Page import Page 
from src.backend.PluginManager.PluginBase import PluginBase 

# Import python modules
import GPUtil

# Import gtk modules - used for the config rows
import gi
gi.require_version("Gtk", "4.0") 
gi.require_version("Adw", "1") 
from gi.repository import Gtk, Adw 

class Temp(ActionBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def on_ready(self) -> None:
    	GPUs = GPUtil.getGPUs()
        
        if not GPUs:  # Check if any GPU is available
            print("No temps found")
        else:
            for GPU in GPUs:
                print(f"Temp: {GPU.temperature}")

    def on_key_down(self) -> None:
        print("Key down") 

    def on_key_up(self) -> None:
        print("Key up")
