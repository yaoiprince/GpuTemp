# Import StreamController modules
from src.backend.PluginManager.ActionBase import ActionBase
from src.backend.DeckManagement.DeckController import DeckController
from src.backend.PageManagement.Page import Page
from src.backend.PluginManager.PluginBase import PluginBase

# Import python modules
import os
import psutil

# Import gtk modules
import gi
gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Gtk, Adw

class GpuTemp(ActionBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.has_configuration = False

        self.unit_row = ComboRow(
            action_core=self,
            var_name="unit",
            default_value="C",
            items=[SimpleComboRowItem("C", "°C"), SimpleComboRowItem("F", "°F")],
            title="Unit",
            can_reset=False,
            on_change=lambda *args: self.update()
        )
    
    def on_ready(self):
        self.update()
        
    def on_tick(self):
        self.update()

    def celcius_to_fahrenheit(self, celsius):
        return celsius * 1.8 + 32

    def update(self):
        temperature = psutil.sensors_temperatures()
        # intel cpu
        if "nvme-Composite" in temperature:
            temperature = temperature.get("nvme-Composite")[0].current
        else:
            self.set_center_label(text="N/A", font_size=18)
            return

        unit_key = self.unit_row.get_value()
        temp = int(temperature)
        if unit_key == "F":
            temp = self.celcius_to_fahrenheit(temp)
        self.set_center_label(text=f"{round(temp)} °{unit_key}", font_size=18)
