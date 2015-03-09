# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin


##~~ Init Plugin and Metadata


class ZOffset(octoprint.plugin.TemplatePlugin,
			  octoprint.plugin.AssetPlugin,
			  octoprint.plugin.SettingsPlugin):

		##~~ AssetsPlugin
		def get_assets(self):
			return dict(
				js=["js/zoffset.js"],
				css=["css/zoffset.css"]
			)

		##~~ Set default settings
		def get_settings_defaults(self):
			return dict(zOffset=0.0)


		def get_template_configs(self):
			return [
				dict(type="settings", custom_bindings=False)
			]

		def script_hook(self, comm, script_type, script_name):
			if not script_type == "gcode":
				return None
	
			if script_name == "beforePrintStarted":
				return ["M206 Z" + self._settings.get_int(["zOffset"])], None

			if script_name == "afterPrinterConnected":
				return ["M206 Z" + self._settings.get_int(["zOffset"])], None

def __plugin_init__():
    global __plugin_implementations__
    global __plugin_hooks__
    plugin = ZOffset()
    __plugin_implementations__ = [plugin]
    __plugin_hooks__ = {
        "octoprint.comm.protocol.scripts": plugin.script_hook
    }

__plugin_name__ = "zOffset"
