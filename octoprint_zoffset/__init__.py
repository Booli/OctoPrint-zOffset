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
			return dict(zOffset=0.2)


		def get_template_configs(self):
			return [
				dict(type="settings", custom_bindings=False)
			]

__plugin_implementations__ = [ZOffset()]
__plugin_name__ = "zOffset"