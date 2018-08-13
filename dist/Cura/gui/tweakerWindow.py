
import wx
import wx.xrc

class tweakerWindow ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Beta testing disclaimer", pos = wx.DefaultPosition, size = wx.Size( 701,200 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.top1 = wx.StaticText( self, wx.ID_ANY, u"Automatically orient your model on the printing platform for best output! ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.top1.SetFont( wx.Font( 12, 70, 90, 92, False, "Arial" ) )
		self.top1.Wrap( -1 )
		bSizer1.Add( self.top1, 0, wx.ALL, 5 )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Works best with STL files under 10mb, Processing times depend on CPU specs. It usually takes 30-90 secs, the object will reload on the platform automatically", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( 420 )
		self.m_staticText4.SetFont( wx.Font( 12, 70, 90, 92, False, "Arial" ) )

		bSizer1.Add( self.m_staticText4, 0, wx.ALL, 5 )

		# self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Should you encounter any bugs, glitches, lack of functionality or other problems with the feature, please let us know immediately so we can rectify these accordingly. Your help in this regard is greatly appreciated.", wx.DefaultPosition, wx.DefaultSize, 0 )
		# self.m_staticText3.Wrap( 400 )
		# bSizer1.Add( self.m_staticText3, 0, wx.ALL, 5 )

		self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer1.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

		# self.m_checkBox1 = wx.CheckBox( self, wx.ID_ANY, u"Don't show this again", wx.DefaultPosition, wx.DefaultSize, 0 )
		# self.m_checkBox1.SetValue(True)
		# bSizer2.Add( self.m_checkBox1, 0, wx.ALL|wx.EXPAND, 5 )

		self.cancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cancel.Bind( wx.EVT_BUTTON, self.OnCancel )
		bSizer2.Add( self.cancel, 1, wx.ALL|wx.EXPAND, 5 )

		self.optimize = wx.Button( self, wx.ID_ANY, u"Optimize", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.optimize.SetFont( wx.Font( 12, 74, 90, 92, False, "Arial Black" ) )
		self.optimize.Bind( wx.EVT_BUTTON, self.OnOptimize )

		bSizer2.Add( self.optimize, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass

	def OnOptimize( self,e ):
         sceneView = self.GetParent()
         self.Destroy()
         sceneView.OniSliceOptimize()

	def OnCancel( self,e ):
         self.Destroy()
