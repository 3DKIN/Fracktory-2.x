__copyright__ = "Copyright (C) 2013 David Braam - Released under terms of the AGPLv3 License"

import wx
import urllib
import urllib2

from Cura.gui import configWizard
from Cura.gui import configBase
from Cura.util import machineCom
from Cura.util import profile
from Cura.util import pluginInfo
from Cura.util import resources

class preferencesDialog(wx.Dialog):
	def __init__(self, parent):
		super(preferencesDialog, self).__init__(None, title=_("Preferences"))

		wx.EVT_CLOSE(self, self.OnClose)

		self.parent = parent
		extruderCount = int(profile.getMachineSetting('extruder_amount'))

		self.panel = configBase.configPanelBase(self)

		left, right, main = self.panel.CreateConfigPanel(self)

		printWindowTypes = ['Basic']
		for p in pluginInfo.getPluginList('printwindow'):
			printWindowTypes.append(p.getName())
		configBase.TitleRow(left, _("Print window"))
		configBase.SettingRow(left, 'printing_window', printWindowTypes)

		configBase.TitleRow(left, _("Colours"))
		configBase.SettingRow(left, 'model_colour', wx.Colour)
		for i in xrange(1, extruderCount):
			configBase.SettingRow(left, 'model_colour%d' % (i+1), wx.Colour)

		if len(resources.getLanguageOptions()) > 1:
			configBase.TitleRow(left, _("Language"))
			configBase.SettingRow(left, 'language', map(lambda n: n[1], resources.getLanguageOptions()))

		configBase.TitleRow(right, _("Filament settings"))
		configBase.SettingRow(right, 'filament_physical_density')
		configBase.SettingRow(right, 'filament_cost_kg')
		configBase.SettingRow(right, 'filament_cost_meter')

		#configBase.TitleRow(right, 'Slicer settings')
		#configBase.SettingRow(right, 'save_profile')

		#configBase.TitleRow(right, 'SD Card settings')

		configBase.TitleRow(right, _("Fracktory settings"))
		configBase.SettingRow(right, 'auto_detect_sd')
		# configBase.SettingRow(right, 'check_for_updates')
		configBase.SettingRow(right, 'submit_slice_information')

		self.okButton = wx.Button(right, -1, 'Ok')
		right.GetSizer().Add(self.okButton, (right.GetSizer().GetRows(), 0), flag=wx.BOTTOM, border=5)
		self.okButton.Bind(wx.EVT_BUTTON, lambda e: self.Close())

		main.Fit()
		self.Fit()

	def OnClose(self, e):
		#self.parent.reloadSettingPanels()
		self.Destroy()

class machineSettingsDialog(wx.Dialog):
	def __init__(self, parent):
		super(machineSettingsDialog, self).__init__(None, title=_("Machine settings"))

		wx.EVT_CLOSE(self, self.OnClose)

		self.parent = parent

		self.panel = configBase.configPanelBase(self)
		self.SetSizer(wx.BoxSizer(wx.HORIZONTAL))
		self.GetSizer().Add(self.panel, 1, wx.EXPAND)
		self.nb = wx.Notebook(self.panel)
		self.panel.SetSizer(wx.BoxSizer(wx.VERTICAL))
		self.panel.GetSizer().Add(self.nb, 1, wx.EXPAND)

		for idx in xrange(0, profile.getMachineCount()):
			extruderCount = int(profile.getMachineSetting('extruder_amount', idx))
			left, right, main = self.panel.CreateConfigPanel(self.nb)
			configBase.TitleRow(left, _("Machine settings"))
			configBase.SettingRow(left, 'steps_per_e', index=idx)
			configBase.SettingRow(left, 'machine_width', index=idx)
			configBase.SettingRow(left, 'machine_depth', index=idx)
			configBase.SettingRow(left, 'machine_height', index=idx)
			configBase.SettingRow(left, 'extruder_amount', index=idx)
			configBase.SettingRow(left, 'has_heated_bed', index=idx)
			configBase.SettingRow(left, 'machine_center_is_zero', index=idx)
			configBase.SettingRow(left, 'machine_shape', index=idx)
			configBase.SettingRow(left, 'gcode_flavor', index=idx)

			configBase.TitleRow(right, _("Printer head size"))
			configBase.SettingRow(right, 'extruder_head_size_min_x', index=idx)
			configBase.SettingRow(right, 'extruder_head_size_min_y', index=idx)
			configBase.SettingRow(right, 'extruder_head_size_max_x', index=idx)
			configBase.SettingRow(right, 'extruder_head_size_max_y', index=idx)
			configBase.SettingRow(right, 'extruder_head_size_height', index=idx)

			for i in xrange(1, extruderCount):
				configBase.TitleRow(left, _("Extruder %d") % (i+1))
				configBase.SettingRow(left, 'extruder_offset_x%d' % (i), index=idx)
				configBase.SettingRow(left, 'extruder_offset_y%d' % (i), index=idx)

			configBase.TitleRow(right, _("Communication settings"))
			configBase.SettingRow(right, 'serial_port', ['AUTO'] + machineCom.serialList(), index=idx)
			configBase.SettingRow(right, 'serial_baud', ['AUTO'] + map(str, machineCom.baudrateList()), index=idx)
			configBase.SettingRow(right, 'wireless_ip', index=idx)
			configBase.SettingRow(right, 'wireless_api', index=idx)
			# configBase.TitleRow(right, _("Printer Identification"))
			# configBase.SettingRow(right, 'name', index=idx)
			# configBase.SettingRow(right, 'address', index=idx)
			# configBase.SettingRow(right, 'state', index=idx)
			# configBase.SettingRow(right, 'city', index=idx)
			# configBase.SettingRow(right, 'email', index=idx)
			# configBase.SettingRow(right, 'sn_number', index=idx)

			self.nb.AddPage(main, profile.getMachineSetting('machine_name', idx).title())

		self.nb.SetSelection(int(profile.getPreferenceFloat('active_machine')))

		self.buttonPanel = wx.Panel(self.panel)
		self.panel.GetSizer().Add(self.buttonPanel)

		self.buttonPanel.SetSizer(wx.BoxSizer(wx.HORIZONTAL))
		self.okButton = wx.Button(self.buttonPanel, -1, _('Ok'))
		self.okButton.Bind(wx.EVT_BUTTON, lambda e: self.Close())
		self.buttonPanel.GetSizer().Add(self.okButton, flag=wx.ALL, border=5)

		self.addButton = wx.Button(self.buttonPanel, -1, _('Add new machine'))
		self.addButton.Bind(wx.EVT_BUTTON, self.OnAddMachine)
		self.buttonPanel.GetSizer().Add(self.addButton, flag=wx.ALL, border=5)

		self.remButton = wx.Button(self.buttonPanel, -1, _('Remove machine'))
		self.remButton.Bind(wx.EVT_BUTTON, self.OnRemoveMachine)
		self.buttonPanel.GetSizer().Add(self.remButton, flag=wx.ALL, border=5)

		self.renButton = wx.Button(self.buttonPanel, -1, _('Change machine name'))
		self.renButton.Bind(wx.EVT_BUTTON, self.OnRenameMachine)
		self.buttonPanel.GetSizer().Add(self.renButton, flag=wx.ALL, border=5)

		# self.regButton = wx.Button(self.buttonPanel, -1, _('Register machine'))
		# self.regButton.Bind(wx.EVT_BUTTON, self.OnRegisterMachine)
		# self.buttonPanel.GetSizer().Add(self.regButton, flag=wx.ALL, border=5)

		main.Fit()
		self.Fit()


	def OnRegisterMachine(self, e):
		if "Not" in profile.getMachineSetting('machine_name',self.nb.GetSelection()):
			data = {
				'name' : str(profile.getMachineSetting('name',self.nb.GetSelection())),
				'address': str(profile.getMachineSetting('address',self.nb.GetSelection())),
				'state': str(profile.getMachineSetting('state',self.nb.GetSelection())),
				'city': str(profile.getMachineSetting('city',self.nb.GetSelection())),
				'email': str(profile.getMachineSetting('email',self.nb.GetSelection())),
				'sn_number': str(profile.getMachineSetting('sn_number',self.nb.GetSelection())),
			}
			if not data['name']:
				dlg = wx.MessageDialog(self, "Enter name", 'Please check...', wx.OK | wx.ICON_INFORMATION)
				dlg.ShowModal()
				return
			if not data['email']:
				dlg = wx.MessageDialog(self, "Enter email", 'Please check...', wx.OK | wx.ICON_INFORMATION)
				dlg.ShowModal()
				return
			if not data['sn_number']:
				dlg = wx.MessageDialog(self, "Enter serial number", 'Please check...', wx.OK | wx.ICON_INFORMATION)
				dlg.ShowModal()
				return
			try:
				bi = wx.BusyInfo("Please Wait...", self)
				f = urllib2.urlopen("http://printers.fracktory.in/api/Client/", data = urllib.urlencode(data), timeout = 3)
				msg_response = f.read()
				f.close()
				if f.getcode() == 201:
					r = urllib2.urlopen("http://printers.fracktory.in/registered_mail", data = urllib.urlencode(data), timeout = 3)
					print r.read()
					r.close()
				bi.Destroy()
				# profile.putMachineSetting('name',str(self.name.GetValue()))
				# profile.putMachineSetting('address',str(self.address.GetValue()))
				# profile.putMachineSetting('state',str(self.state.GetValue()))
				# profile.putMachineSetting('city',str(self.city.GetValue()))
				# profile.putMachineSetting('email',str(self.email.GetValue()))
				# profile.putMachineSetting('sn_number',str(self.sn_number.GetValue()))
				machine_name = profile.getMachineSetting('machine_name',self.nb.GetSelection())
				sn_numbername = profile.getMachineSetting('sn_number',self.nb.GetSelection())
				profile.putMachineSetting('machine_name',str( "Julia" + ' - ' + sn_numbername ),self.nb.GetSelection())
				dlg = wx.MessageDialog(self, "Succesfully Registered With Fracktal Database, Email is sent with further information.", 'Response from server...', wx.OK | wx.ICON_INFORMATION)
				dlg.ShowModal()
				self.Close()
			except:
				dlg = wx.MessageDialog(self, 'Registration failed, Check your internet connection', 'Error', wx.OK | wx.ICON_WARNING)
				dlg.ShowModal()
		else:
			dlg = wx.MessageDialog(self, "Printer already registered with us", 'Printer already registered', wx.OK | wx.ICON_INFORMATION)
			dlg.ShowModal()


	def OnAddMachine(self, e):
		self.Hide()
		self.parent.Hide()
		configWizard.ConfigWizard(True)
		self.parent.Show()
		self.parent.reloadSettingPanels()
		self.parent.updateMachineMenu()

		prefDialog = machineSettingsDialog(self.parent)
		prefDialog.Centre()
		prefDialog.Show()
		wx.CallAfter(self.Close)

	def OnRemoveMachine(self, e):
		if profile.getMachineCount() < 2:
			wx.MessageBox(_("Cannot remove the last machine configuration in Cura"), _("Machine remove error"), wx.OK | wx.ICON_ERROR)
			return

		self.Hide()
		profile.removeMachine(self.nb.GetSelection())
		self.parent.reloadSettingPanels()
		self.parent.updateMachineMenu()

		prefDialog = machineSettingsDialog(self.parent)
		prefDialog.Centre()
		prefDialog.Show()
		wx.CallAfter(self.Close)

	def OnRenameMachine(self, e):
		dialog = wx.TextEntryDialog(self, _("Enter the new name:"), _("Change machine name"), self.nb.GetPageText(self.nb.GetSelection()))
		if dialog.ShowModal() != wx.ID_OK:
			return
		self.nb.SetPageText(self.nb.GetSelection(), dialog.GetValue())
		profile.putMachineSetting('machine_name', dialog.GetValue(), self.nb.GetSelection())
		self.parent.updateMachineMenu()

	def OnClose(self, e):
		self.parent.reloadSettingPanels()
		self.Destroy()
