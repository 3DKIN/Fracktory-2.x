import wx
import wx.xrc
import urllib
import urllib2
import json
import datetime

from Cura.util import profile

class complaintWindow ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 353,600 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Services Request Complaint", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		self.m_staticText1.SetFont( wx.Font( 18, 74, 90, 90, False, "Arial" ) )

		bSizer1.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer1.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Name/Company", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		bSizer1.Add( self.m_staticText6, 0, wx.ALL, 5 )


		self.name = wx.TextCtrl( self, wx.ID_ANY,str(profile.getMachineSetting('name',int(profile.getPreferenceFloat('active_machine')) )), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.name, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"Email id", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )
		bSizer1.Add( self.m_staticText9, 0, wx.ALL, 5 )

		self.email = wx.TextCtrl( self, wx.ID_ANY, str(profile.getMachineSetting('email',int(profile.getPreferenceFloat('active_machine')) )), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.email, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Phone no", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		bSizer1.Add( self.m_staticText7, 0, wx.ALL, 5 )

		self.phone = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.phone, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"Address", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		bSizer1.Add( self.m_staticText8, 0, wx.ALL, 5 )

		self.address = wx.TextCtrl( self, wx.ID_ANY, str(profile.getMachineSetting('address',int(profile.getPreferenceFloat('active_machine')) )), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.address, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Serial #", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		bSizer1.Add( self.m_staticText11, 0, wx.ALL, 5 )

		self.serial_no = wx.TextCtrl( self, wx.ID_ANY, str(profile.getMachineSetting('sn_number',int(profile.getPreferenceFloat('active_machine')) )), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.serial_no, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"Problem type", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )
		bSizer1.Add( self.m_staticText10, 0, wx.ALL, 5 )

		problem_choiceChoices = [ u"Nozzel Jam", u"Bed Level", u"Printer not moving", u"Bad quality prints", u"Print not sticking to bed", u"Bed/Nozzel not heating", u"Other..." ]
		self.problem_choice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, problem_choiceChoices, 0 )
		self.problem_choice.SetSelection( 6 )
		bSizer1.Add( self.problem_choice, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"Detailed description ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )
		bSizer1.Add( self.m_staticText12, 0, wx.ALL, 5 )

		self.detail_desc = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.detail_desc, 1, wx.ALL|wx.EXPAND, 5 )

		self.submit_complaint = wx.Button( self, wx.ID_ANY, u"Submit request", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.submit_complaint, 1, wx.ALL|wx.EXPAND, 5 )
		self.submit_complaint.Bind( wx.EVT_BUTTON, self.OnComplaint )



		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

	def OnComplaint(self, e):
		data = {
			'name' : str(self.name.GetValue()),
			'email': str(self.email.GetValue()),
			'phone': str(self.phone.GetValue()),
			'address': str(self.address.GetValue()),
			'sn_number': str(self.serial_no.GetValue()),
			'problem': str(self.problem_choice.GetString(self.problem_choice.GetSelection())),
			'detailed_info': str(self.detail_desc.GetValue()),
		}
		if not data['name']:
			dlg = wx.MessageDialog(self, "Enter name", 'Please check...', wx.OK | wx.ICON_INFORMATION)
			dlg.ShowModal()
			return
		if not data['email']:
			dlg = wx.MessageDialog(self, "Enter email", 'Please check...', wx.OK | wx.ICON_INFORMATION)
			dlg.ShowModal()
			return
		if not data['phone']:
			dlg = wx.MessageDialog(self, "Enter phone no", 'Please check...', wx.OK | wx.ICON_INFORMATION)
			dlg.ShowModal()
			return
		if not data['sn_number']:
			dlg = wx.MessageDialog(self, "Enter serial number", 'Please check...', wx.OK | wx.ICON_INFORMATION)
			dlg.ShowModal()
			return
		if not data['detailed_info']:
			dlg = wx.MessageDialog(self, "Please enter detailed information about the problem", 'Please check...', wx.OK | wx.ICON_INFORMATION)
			dlg.ShowModal()
			return
		try:
			# print data
			bi = wx.BusyInfo("Please Wait...", self)
			f = urllib2.urlopen("http://printers.fracktory.in/api/Complaints/", data = urllib.urlencode(data), timeout = 3)
			msg_response = json.loads(f.read())
			f.close()
			t = datetime.datetime.now()
			tm = t.strftime("%B")
			ticket_complaint = "{}-{}-{}".format(tm[0], t.day, msg_response['id'])
			print ticket_complaint
			data['id'] = ticket_complaint
			print data
			if f.getcode() == 201:
				r = urllib2.urlopen("http://printers.fracktory.in/complaint_mail", data = urllib.urlencode(data), timeout = 3)
				print r.read()
				r.close()
			bi.Destroy()
			dlg = wx.MessageDialog(self, "Complaint registered, Please wait for email confirmation ", 'Response from server', wx.OK | wx.ICON_INFORMATION)
			dlg.ShowModal()
			self.Close()
		except Exception as e:
			bi.Destroy()
			dlg = wx.MessageDialog(self, str(e), 'Error', wx.OK | wx.ICON_WARNING)
			dlg.ShowModal()


	def __del__( self ):
		pass
