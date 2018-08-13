import wx
import wx.xrc
import requests
import OctoUpload as upload_file

class uploadWindow ( wx.Dialog  ):

	def __init__( self, parent,printer_list,filename ):
		wx.Dialog .__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 287,405 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		self.Bind(wx.EVT_CLOSE, self.onClose)

		self.printer_list_class = printer_list
		self.filename_class = filename
		printer_listChoices = []
		for n in range(0,len(self.printer_list_class)):
			printer_listChoices.append(self.printer_list_class[n][0])

		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Select Printer from list", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		self.m_staticText1.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )

		bSizer1.Add( self.m_staticText1, 0, wx.ALL, 5 )

		self.printer_list = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, printer_listChoices, 0 )
		self.printer_list.SetSelection( 0 )
		self.printer_list.Bind(wx.EVT_CHOICE, self.onPrinterChoice)
		bSizer1.Add( self.printer_list, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer1.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

		self.printer_ip = wx.StaticText( self, wx.ID_ANY, u"<IP>", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.printer_ip.Wrap( -1 )
		self.printer_ip.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )

		bSizer2.Add( self.printer_ip, 1, wx.ALL, 5 )

		self.printer_status = wx.StaticText( self, wx.ID_ANY, u"<READY/BUSY/OFFLINE>", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.printer_status.Wrap( -1 )
		self.printer_status.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )

		bSizer2.Add( self.printer_status, 1, wx.ALL, 5 )

		self.m_staticline2 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer2.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )


		bSizer1.Add( bSizer2, 0, wx.EXPAND, 3 )

		self.m_staticline3 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer1.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Send file to printer", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		self.m_staticText4.SetFont( wx.Font( 9, 70, 90, 92, False, "Arial" ) )

		bSizer1.Add( self.m_staticText4, 0, wx.ALL, 5 )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		bSizer51 = wx.BoxSizer( wx.HORIZONTAL )

		storage_selectChoices = [ u"SD Card (safer)", u"Local Stream (faster)" ]
		self.storage_select = wx.RadioBox( self, wx.ID_ANY, u"Select Storage", wx.DefaultPosition, wx.DefaultSize, storage_selectChoices, 1, wx.RA_SPECIFY_COLS )
		self.storage_select.SetSelection( 1 )
		bSizer5.Add( self.storage_select, 0, wx.ALL|wx.EXPAND, 5 )

		self.print_now = wx.CheckBox( self, wx.ID_ANY, u"Start Printing", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer51.Add( self.print_now, 1, wx.ALL|wx.EXPAND, 5 )

		bSizer5.Add( bSizer51, 0, wx.EXPAND, 5 )

		self.start_button = wx.Button( self, wx.ID_ANY, u"Start Upload", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.start_button, 1, wx.ALL|wx.EXPAND, 5 )
		self.start_button.Bind( wx.EVT_BUTTON, self.start_upload_file )
		self.start_button.Disable()


		bSizer1.Add( bSizer5, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

	def onClose(self,event):
		self.Hide()

	def __del__( self ):
		pass

	def ShowPrintingMessage(self):
    		wx.MessageBox('Other print already in process, Please try again', 'Printer Busy!',wx.OK | wx.ICON_EXCLAMATION)

	def ShowMessage(self,message):
    		wx.MessageBox(message, 'Printer not Ready',wx.OK | wx.ICON_EXCLAMATION)

	def start_upload_file(self,event):
		'''
		Available only when the printer is Operational, will start sending the file on call
		'''
		# def start_upload_file(hostIP,octoPort,api_key,sendLoc,printBool,filename)
		hostIP = self.printer_list_class[self.printer_list.GetCurrentSelection()][1]
		octoPort = "80"
		api_key = self.printer_list_class[self.printer_list.GetCurrentSelection()][2]
		if self.storage_select.GetSelection() == 0:
			sendLoc = "sdcard"
		else:
			sendLoc = "local"

		if self.print_now.IsChecked():
			printBool = "yes"
		else:
			printBool = "no"

		file_name = self.filename_class
		bi = wx.BusyInfo("Uploading to " + sendLoc + " please wait", self)
		upload_file.start_upload_file(hostIP,octoPort,api_key,sendLoc,printBool,file_name)
		bi.Destroy()



	def onPrinterChoice(self,event):
		'''
		Called when the printer is selected from dropdown
		'''
		p_choice = self.printer_list.GetStringSelection()
		self.printer_ip.SetLabel(self.printer_list_class[self.printer_list.GetCurrentSelection()][1])
		# Ping printer here and display result!
		url = 'http://'+self.printer_list_class[self.printer_list.GetCurrentSelection()][1]+'/api/connection'
		headers = {'X-Api-Key':self.printer_list_class[self.printer_list.GetCurrentSelection()][2]}
		try:
			response = requests.get(url,headers=headers,timeout=3)
			temp=response.json()
		except requests.exceptions.Timeout:
			self.ShowMessage("Request timed out! Check your network connec")
		except requests.exceptions.RequestException as e:    # This is the correct syntax
			self.ShowMessage("Communication with the printer failed")
		# print temp
		self.printer_status.SetLabel(temp['current']['state'])
		if temp['current']['state']=="Printing":
			self.ShowMessage(temp['current']['state'])
		elif temp['current']['state']=="Operational":
			self.start_button.Enable()
		else:
			self.ShowMessage(temp['current']['state'])



def start(printer_list,filename):
	ex = wx.App()
	f1=uploadWindow(None,printer_list,filename)
	f1.Show()
	ex.MainLoop()
