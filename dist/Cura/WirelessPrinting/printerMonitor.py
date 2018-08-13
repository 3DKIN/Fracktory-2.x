
import wx
import wx.xrc

class PrinterMonitor ( wx.Dialog ):

	def __init__( self, parent,printer_list ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Printer Monitor", pos = wx.DefaultPosition, size = wx.Size( 760,587 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.printer_list_class = printer_list
		self.filename_class = filename
		printer_selectChoices = []
		for n in range(0,len(self.printer_list_class)):
			printer_selectChoices.append(self.printer_list_class[n][0])


		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		bSizer21 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText25 = wx.StaticText( self, wx.ID_ANY, u"Select Printer : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText25.Wrap( -1 )
		self.m_staticText25.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )

		bSizer21.Add( self.m_staticText25, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		printer_selectChoices = []
		self.printer_select = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, printer_selectChoices, 0 )
		self.printer_select.SetSelection( 0 )
		bSizer21.Add( self.printer_select, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticline2 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer21.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )


		bSizer1.Add( bSizer21, 0, wx.EXPAND, 5 )

		ConnectionSizer = wx.BoxSizer( wx.HORIZONTAL )

		connection_box = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Connection" ), wx.VERTICAL )

		self.m_staticText18 = wx.StaticText( connection_box.GetStaticBox(), wx.ID_ANY, u"Port", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )
		self.m_staticText18.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )

		connection_box.Add( self.m_staticText18, 0, wx.ALL, 5 )

		serial_port_choiceChoices = []
		self.serial_port_choice = wx.Choice( connection_box.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, serial_port_choiceChoices, 0 )
		self.serial_port_choice.SetSelection( 0 )
		connection_box.Add( self.serial_port_choice, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText19 = wx.StaticText( connection_box.GetStaticBox(), wx.ID_ANY, u"Baudrate", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )
		self.m_staticText19.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )

		connection_box.Add( self.m_staticText19, 0, wx.ALL, 5 )

		baudrate_choiceChoices = []
		self.baudrate_choice = wx.Choice( connection_box.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, baudrate_choiceChoices, 0 )
		self.baudrate_choice.SetSelection( 0 )
		connection_box.Add( self.baudrate_choice, 0, wx.ALL|wx.EXPAND, 5 )

		self.connect_button = wx.Button( connection_box.GetStaticBox(), wx.ID_ANY, u"Connect", wx.DefaultPosition, wx.DefaultSize, 0 )
		connection_box.Add( self.connect_button, 1, wx.ALL|wx.EXPAND, 5 )


		ConnectionSizer.Add( connection_box, 1, wx.EXPAND, 5 )

		state_box = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"State" ), wx.HORIZONTAL )

		bSizer8 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1 = wx.StaticText( state_box.GetStaticBox(), wx.ID_ANY, u"Status : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		self.m_staticText1.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )

		bSizer8.Add( self.m_staticText1, 0, wx.ALL, 5 )

		self.m_staticText8 = wx.StaticText( state_box.GetStaticBox(), wx.ID_ANY, u"File :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		self.m_staticText8.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )

		bSizer8.Add( self.m_staticText8, 0, wx.ALL, 5 )

		self.m_staticText9 = wx.StaticText( state_box.GetStaticBox(), wx.ID_ANY, u"Print Time :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )
		self.m_staticText9.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )

		bSizer8.Add( self.m_staticText9, 0, wx.ALL, 5 )

		self.m_staticText10 = wx.StaticText( state_box.GetStaticBox(), wx.ID_ANY, u"Time Left :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )
		self.m_staticText10.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )

		bSizer8.Add( self.m_staticText10, 0, wx.ALL, 5 )

		self.m_staticText16 = wx.StaticText( state_box.GetStaticBox(), wx.ID_ANY, u"Printed : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )
		self.m_staticText16.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )

		bSizer8.Add( self.m_staticText16, 0, wx.ALL, 5 )


		state_box.Add( bSizer8, 0, wx.EXPAND, 5 )

		bSizer9 = wx.BoxSizer( wx.VERTICAL )

		self.status_text = wx.StaticText( state_box.GetStaticBox(), wx.ID_ANY, u"~", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.status_text.Wrap( -1 )
		bSizer9.Add( self.status_text, 0, wx.ALL, 5 )

		self.file_text = wx.StaticText( state_box.GetStaticBox(), wx.ID_ANY, u"~", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.file_text.Wrap( -1 )
		bSizer9.Add( self.file_text, 0, wx.ALL, 5 )

		self.time_text = wx.StaticText( state_box.GetStaticBox(), wx.ID_ANY, u"~", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.time_text.Wrap( -1 )
		bSizer9.Add( self.time_text, 0, wx.ALL, 5 )

		self.time_left_text = wx.StaticText( state_box.GetStaticBox(), wx.ID_ANY, u"~", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.time_left_text.Wrap( -1 )
		bSizer9.Add( self.time_left_text, 0, wx.ALL, 5 )

		self.printed_text = wx.StaticText( state_box.GetStaticBox(), wx.ID_ANY, u"~", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.printed_text.Wrap( -1 )
		bSizer9.Add( self.printed_text, 0, wx.ALL, 5 )

		bSizer15 = wx.BoxSizer( wx.HORIZONTAL )

		self.pause_button = wx.Button( state_box.GetStaticBox(), wx.ID_ANY, u"Pause", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer15.Add( self.pause_button, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.stop_button = wx.Button( state_box.GetStaticBox(), wx.ID_ANY, u"Stop", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer15.Add( self.stop_button, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )


		bSizer9.Add( bSizer15, 0, 0, 5 )


		state_box.Add( bSizer9, 1, wx.EXPAND, 5 )


		ConnectionSizer.Add( state_box, 1, wx.EXPAND, 5 )


		bSizer1.Add( ConnectionSizer, 1, wx.EXPAND, 5 )

		FilesSizer = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Files" ), wx.HORIZONTAL )

		local_box = wx.StaticBoxSizer( wx.StaticBox( FilesSizer.GetStaticBox(), wx.ID_ANY, u"Printer Storage" ), wx.HORIZONTAL )

		local_textboxChoices = []
		self.local_textbox = wx.ListBox( local_box.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, local_textboxChoices, 0 )
		local_box.Add( self.local_textbox, 1, wx.ALL|wx.EXPAND, 5 )

		bSizer10 = wx.BoxSizer( wx.VERTICAL )

		self.local_print = wx.Button( local_box.GetStaticBox(), wx.ID_ANY, u"Print", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.local_print, 0, wx.ALL, 5 )

		self.local_refresh = wx.Button( local_box.GetStaticBox(), wx.ID_ANY, u"Refresh", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.local_refresh, 0, wx.ALL, 5 )


		local_box.Add( bSizer10, 0, wx.ALIGN_CENTER_VERTICAL, 5 )


		FilesSizer.Add( local_box, 1, wx.EXPAND, 5 )

		sd_box = wx.StaticBoxSizer( wx.StaticBox( FilesSizer.GetStaticBox(), wx.ID_ANY, u"Printer Storage" ), wx.HORIZONTAL )

		sd_textboxChoices = []
		self.sd_textbox = wx.ListBox( sd_box.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, sd_textboxChoices, 0 )
		sd_box.Add( self.sd_textbox, 1, wx.ALL|wx.EXPAND, 5 )

		bSizer101 = wx.BoxSizer( wx.VERTICAL )

		self.sd_print = wx.Button( sd_box.GetStaticBox(), wx.ID_ANY, u"Print", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer101.Add( self.sd_print, 0, wx.ALL, 5 )

		self.sd_refresh = wx.Button( sd_box.GetStaticBox(), wx.ID_ANY, u"Refresh", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer101.Add( self.sd_refresh, 0, wx.ALL, 5 )


		sd_box.Add( bSizer101, 0, wx.ALIGN_CENTER_VERTICAL, 5 )


		FilesSizer.Add( sd_box, 1, wx.EXPAND, 5 )


		bSizer1.Add( FilesSizer, 1, wx.EXPAND, 5 )

		TempSizer = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Temperature" ), wx.HORIZONTAL )

		nozzel_box = wx.StaticBoxSizer( wx.StaticBox( TempSizer.GetStaticBox(), wx.ID_ANY, u"Nozzel" ), wx.HORIZONTAL )

		bSizer12 = wx.BoxSizer( wx.VERTICAL )

		self.nozzel_temp = wx.StaticText( nozzel_box.GetStaticBox(), wx.ID_ANY, u"~", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.nozzel_temp.Wrap( -1 )
		self.nozzel_temp.SetFont( wx.Font( 48, 74, 90, 90, False, "Arial" ) )

		bSizer12.Add( self.nozzel_temp, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		nozzel_box.Add( bSizer12, 1, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )

		bSizer16 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText161 = wx.StaticText( nozzel_box.GetStaticBox(), wx.ID_ANY, u"Target Temp", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText161.Wrap( -1 )
		bSizer16.Add( self.m_staticText161, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.nozzel_set = wx.TextCtrl( nozzel_box.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer16.Add( self.nozzel_set, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.nozzel_btn = wx.Button( nozzel_box.GetStaticBox(), wx.ID_ANY, u"Set", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer16.Add( self.nozzel_btn, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		nozzel_box.Add( bSizer16, 1, wx.ALIGN_CENTER_VERTICAL, 5 )


		TempSizer.Add( nozzel_box, 1, wx.ALIGN_CENTER_VERTICAL, 5 )

		bed_box = wx.StaticBoxSizer( wx.StaticBox( TempSizer.GetStaticBox(), wx.ID_ANY, u"Bed" ), wx.HORIZONTAL )

		bSizer11 = wx.BoxSizer( wx.VERTICAL )

		self.bed_temp = wx.StaticText( bed_box.GetStaticBox(), wx.ID_ANY, u"~", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bed_temp.Wrap( -1 )
		self.bed_temp.SetFont( wx.Font( 48, 74, 90, 90, False, "Arial" ) )

		bSizer11.Add( self.bed_temp, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bed_box.Add( bSizer11, 1, wx.EXPAND, 5 )

		bSizer161 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText181 = wx.StaticText( bed_box.GetStaticBox(), wx.ID_ANY, u"Target Temp", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText181.Wrap( -1 )
		bSizer161.Add( self.m_staticText181, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.bed_set = wx.TextCtrl( bed_box.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer161.Add( self.bed_set, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.bed_btn = wx.Button( bed_box.GetStaticBox(), wx.ID_ANY, u"Set", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer161.Add( self.bed_btn, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bed_box.Add( bSizer161, 1, wx.ALIGN_CENTER_VERTICAL, 5 )


		TempSizer.Add( bed_box, 1, wx.EXPAND, 5 )


		bSizer1.Add( TempSizer, 0, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass
