"""Copies the state from `copy_from` to `copy_to`."""
import appdaemon.plugins.hass.hassapi as hass

## Example `appdaemon.yaml` config:
# copy_switch:
#   module: copy_state
#   class: CopyState
#   copy_from: sensor.desk_lamp_current
#   copy_to: switch.light2

class CopyState(hass.Hass):
    def initialize(self):
        self.listen_state(self.change_state, self.args["copy_from"], new="on")
        self.listen_state(self.change_state, self.args["copy_from"], new="off")

    def change_state(self, entity, attribute, old, new, kwargs):
        switch = self.args["copy_to"]
        if new == "on":
            self.turn_on(switch)
        elif new == "off":
            self.turn_off(switch)
