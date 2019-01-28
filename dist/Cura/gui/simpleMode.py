__copyright__ = "Copyright (C) 2013 David Braam - Released under terms of the AGPLv3 License"

import wx
import ConfigParser as configparser
import os.path

from Cura.util import profile
from Cura.util import resources

class simpleModePanel(wx.Panel):
	"Main user interface window for Quickprint mode"
	def __init__(self, parent, callback):
		super(simpleModePanel, self).__init__(parent)
		self._callback = callback
		self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )
		self._print_profile_options = []
		self._print_material_options = []

		printTypePanel = wx.Panel(self)
		for filename in resources.getSimpleModeProfiles():
			cp = configparser.ConfigParser()
			cp.read(filename)
			base_filename = os.path.splitext(os.path.basename(filename))[0]
			name = base_filename
			if cp.has_option('info', 'name'):
				name = cp.get('info', 'name')
			button = wx.RadioButton(printTypePanel, -1, name, wx.DefaultPosition, wx.Size( -1,25 ), style=wx.RB_GROUP if len(self._print_profile_options) == 0 else 0)
			button.SetFont( wx.Font( 12, 74, 90, 90, False, "Sans" ) )
			button.base_filename = base_filename
			button.filename = filename
			self._print_profile_options.append(button)
			if profile.getPreference('simpleModeProfile') == base_filename:
				button.SetValue(True)

		printMaterialPanel = wx.Panel(self)
		for filename in resources.getSimpleModeMaterials():
			cp = configparser.ConfigParser()
			cp.read(filename)
			base_filename = os.path.splitext(os.path.basename(filename))[0]
			name = base_filename
			if cp.has_option('info', 'name'):
				name = cp.get('info', 'name')
			button = wx.RadioButton(printMaterialPanel, -1, name, wx.DefaultPosition, wx.Size( -1,25 ), style=wx.RB_GROUP if len(self._print_material_options) == 0 else 0)
			button.SetFont( wx.Font( 12, 74, 90, 90, False, "Sans" ) )
			button.base_filename = base_filename
			button.filename = filename
			self._print_material_options.append(button)
			if profile.getPreference('simpleModeMaterial') == base_filename:
				button.SetValue(True)

		if profile.getMachineSetting('gcode_flavor') == 'UltiGCode':
			printMaterialPanel.Show(False)

		# self.printSupport = wx.CheckBox(self, -1, _("Print support structure"))
		# self.printSupport.SetFont( wx.Font( 12, 74, 90, 90, False, "Sans" ) )
		self.platform_adhesion_panel = wx.Panel(self)
		self.platform_adhesion_label = wx.StaticText(self.platform_adhesion_panel, -1, _("Platform adhesion: "))
		self.platform_adhesion_label.SetFont( wx.Font( 12, 74, 90, 90, False, "Sans" ) )
		self.platform_adhesion_combo = wx.ComboBox(self.platform_adhesion_panel, -1, '', choices=[_("None"), _("Brim"), _("Raft")], style=wx.CB_DROPDOWN|wx.CB_READONLY)
		self.platform_adhesion_combo.SetFont( wx.Font( 12, 74, 90, 90, False, "Sans" ) )
		self.platform_adhesion_combo.SetSelection(int(profile.getPreference('simpleModePlatformAdhesion')))
		sizer = wx.BoxSizer(wx.VERTICAL)
		sizer.Add(self.platform_adhesion_label, 0, wx.ALIGN_CENTER_VERTICAL | wx.TOP, 10)
		sizer.Add(self.platform_adhesion_combo, 0, wx.ALIGN_CENTER_VERTICAL | wx.TOP | wx.EXPAND, 10)
		self.platform_adhesion_panel.SetSizer(sizer)

		self.platform_support_panel = wx.Panel(self)
		self.platform_support_label = wx.StaticText(self.platform_support_panel, -1, _("Support Type:"))
		self.platform_support_label.SetFont( wx.Font( 12, 74, 90, 90, False, "Sans" ) )
		self.platform_support_combo = wx.ComboBox(self.platform_support_panel, -1, '', choices=[_("None"), _("Touching buildplate"), _("Everywhere")], style=wx.CB_DROPDOWN|wx.CB_READONLY)
		self.platform_support_combo.SetFont( wx.Font( 12, 74, 90, 90, False, "Sans" ) )
		self.platform_support_combo.SetSelection(int(profile.getPreference('simpleModeSupportType')))
		sizer = wx.BoxSizer(wx.VERTICAL)
		sizer.Add(self.platform_support_label, 0, wx.ALIGN_CENTER_VERTICAL | wx.TOP, 10)
		sizer.Add(self.platform_support_combo, 0, wx.ALIGN_CENTER_VERTICAL | wx.TOP | wx.EXPAND, 10)
		self.platform_support_panel.SetSizer(sizer)


		sizer = wx.GridBagSizer()
		self.SetSizer(sizer)
		sizer.Add((15, 15), (0, 0))
		sb = wx.StaticBox(printTypePanel, label=_("Print Quality:"))
		sb.SetFont( wx.Font( 12, 74, 90, 92, False, "Sans" ) )
		boxsizer = wx.StaticBoxSizer(sb, wx.VERTICAL)
		for button in self._print_profile_options:
			boxsizer.Add(button)
		printTypePanel.SetSizer(wx.BoxSizer(wx.VERTICAL))
		printTypePanel.GetSizer().Add(boxsizer, flag=wx.EXPAND)
		sizer.Add(printTypePanel, (1,0), flag=wx.EXPAND)
		sizer.Add((20, 20), (2, 0))
		sb = wx.StaticBox(printMaterialPanel, label=_("Material:"))
		sb.SetFont( wx.Font( 12, 74, 90, 92, False, "Sans" ) )
		boxsizer = wx.StaticBoxSizer(sb, wx.VERTICAL)
		for button in self._print_material_options:
			boxsizer.Add(button)
		printMaterialPanel.SetSizer(wx.BoxSizer(wx.VERTICAL))
		printMaterialPanel.GetSizer().Add(boxsizer, flag=wx.EXPAND)
		sizer.Add(printMaterialPanel, (3,0), flag=wx.EXPAND)
		sizer.Add((20, 20), (4, 0))
		sb = wx.StaticBox(self, label=_("Other:"))
		sb.SetFont( wx.Font( 12, 74, 90, 92, False, "Sans" ) )
		boxsizer = wx.StaticBoxSizer(sb, wx.VERTICAL)
		# boxsizer.Add(self.printSupport)
		boxsizer.Add(self.platform_adhesion_panel)
		boxsizer.Add(self.platform_support_panel)
		sizer.Add(boxsizer, (5,0), flag=wx.EXPAND)

		for button in self._print_profile_options:
			button.Bind(wx.EVT_RADIOBUTTON, self._update)
		for button in self._print_material_options:
			button.Bind(wx.EVT_RADIOBUTTON, self._update)

		# self.printSupport.Bind(wx.EVT_CHECKBOX, self._update)
		self.platform_adhesion_combo.Bind(wx.EVT_COMBOBOX, self._update)
		self.platform_support_combo.Bind(wx.EVT_COMBOBOX, self._update)

	def _update(self, e):
		for button in self._print_profile_options:
			if button.GetValue():
				profile.putPreference('simpleModeProfile', button.base_filename)
		for button in self._print_material_options:
			if button.GetValue():
				profile.putPreference('simpleModeMaterial', button.base_filename)
		profile.putPreference('simpleModePlatformAdhesion', self.platform_adhesion_combo.GetSelection())
		profile.putPreference('simpleModeSupportType', self.platform_adhesion_combo.GetSelection())
		self._callback()

	def getSettingOverrides(self):
		settings = {}
		for setting in profile.settingsList:
			if not setting.isProfile():
				continue
			if setting.isAdvanced() and setting.getName() == "nozzle_size":
				# print("2 {} = {}".format(setting.getName(), setting.getValue()))
				nozzle = profile.getMachineSetting('custom_nozzle')
				if nozzle:
					settings[setting.getName()] = nozzle
					continue
			settings[setting.getName()] = setting.getDefault()

		for button in self._print_profile_options:
			if button.GetValue():
				cp = configparser.ConfigParser()
				cp.read(button.filename)
				for setting in profile.settingsList:
					if setting.isProfile():
						if cp.has_option('profile', setting.getName()):
							settings[setting.getName()] = eval(cp.get('profile', setting.getName()), {"profile": profile}, {})
		if profile.getMachineSetting('gcode_flavor') != 'UltiGCode':
			for button in self._print_material_options:
				if button.GetValue():
					cp = configparser.ConfigParser()
					cp.read(button.filename)
					for setting in profile.settingsList:
						if setting.isProfile():
							if cp.has_option('profile', setting.getName()):
								settings[setting.getName()] = cp.get('profile', setting.getName())

		# if self.printSupport.GetValue():
		print self.platform_support_combo.GetSelection() 

		if self.platform_support_combo.GetSelection() == 0:
			settings['support'] = "None"			
		elif self.platform_support_combo.GetSelection() == 1:
			settings['support'] = "Touching buildplate"
		elif self.platform_support_combo.GetSelection() == 2:
			settings['support'] = "Everywhere"

		if self.platform_adhesion_combo.GetValue() == _("Brim"):
			settings['platform_adhesion'] = "Brim"
		elif self.platform_adhesion_combo.GetValue() == _("Raft"):
			settings['platform_adhesion'] = "Raft"
		else:
			settings['platform_adhesion'] = "None"

		return settings

	def updateProfileToControls(self):
		pass

	# def printSupportUpdate(self,support_bool):
	# 	self.printSupport.SetValue(support_bool)
	# 	print "Update function"
	# 	pass
