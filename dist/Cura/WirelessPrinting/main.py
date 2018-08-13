# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Feb 16 2016)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################
import time
from threading import *
import urllib2
import os
import wx
import filecmp
import wx.xrc
import json
import requests
import socket
from wx.lib.embeddedimage import PyEmbeddedImage
from wx.lib.pubsub import setuparg1
from wx.lib.pubsub import pub as Publisher
###########################################################################
## Class printer_settings_frame
###########################################################################
icon = PyEmbeddedImage("iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAADAFBMVEUAAAD/AAAA/wD//wAAAP//AP8A///////b29u2traSkpJtbW1JSUkkJCTbAAC2AACSAABtAABJAAAkAAAA2wAAtgAAkgAAbQAASQAAJADb2wC2tgCSkgBtbQBJSQAkJAAAANsAALYAAJIAAG0AAEkAACTbANu2ALaSAJJtAG1JAEkkACQA29sAtrYAkpIAbW0ASUkAJCT/29vbtra2kpKSbW1tSUlJJCT/trbbkpK2bW2SSUltJCT/kpLbbW22SUmSJCT/bW3bSUm2JCT/SUnbJCT/JCTb/9u227aStpJtkm1JbUkkSSS2/7aS25Jttm1JkkkkbSSS/5Jt221JtkkkkiRt/21J20kktiRJ/0kk2yQk/yTb2/+2ttuSkrZtbZJJSW0kJEm2tv+SktttbbZJSZIkJG2Skv9tbdtJSbYkJJJtbf9JSdskJLZJSf8kJNskJP///9vb27a2tpKSkm1tbUlJSST//7bb25K2tm2SkkltbST//5Lb2222tkmSkiT//23b20m2tiT//0nb2yT//yT/2//bttu2kraSbZJtSW1JJEn/tv/bktu2bbaSSZJtJG3/kv/bbdu2SbaSJJL/bf/bSdu2JLb/Sf/bJNv/JP/b//+229uStrZtkpJJbW0kSUm2//+S29tttrZJkpIkbW2S//9t29tJtrYkkpJt//9J29sktrZJ//8k29sk////27bbtpK2km2SbUltSSRJJAD/tpLbkm22bUmSSSRtJAD/ttvbkra2bZKSSW1tJElJACT/krbbbZK2SW2SJEltACTbtv+2ktuSbbZtSZJJJG0kAEm2kv+SbdttSbZJJJIkAG222/+SttttkrZJbZIkSW0AJEmStv9tkttJbbYkSZIAJG22/9uS27ZttpJJkm0kbUkASSSS/7Zt25JJtm0kkkkAbSTb/7a225KStm1tkklJbSQkSQC2/5KS221ttklJkiQkbQD/tgDbkgC2bQCSSQD/ALbbAJK2AG2SAEkAtv8AktsAbbYASZIAAAAAAADPKgIEAAAPwklEQVR42u2beZQcxX3HP9U93T3HzszOzF7SHjqQhBBIgC1sjLACCMRleMYG7OTFNubh4zl+mLyQhMRAcHDA9pOTBzbCYAMx4gZJ2AaDwMbmRuISCIFAx8orCa12tffs7sx0V/3yR89eQISOlRwHlV6/6Zmdqp76Vn2/v2/9qqSmTm4QPsLF4iNeDgJwEICDABwE4CNdIvuzcVW+wjcKlEJkJOqOvv9/B4AF5EVoFQlh6NqJ01fAizt4rofjOriui+t6iMifDYzI/up8sxFOdCL8YyJK3FJ0nnEGXdV1dL+7jc7OTjo7O2hva2PtW29TW11JMpnCGPOXD4AFbDDC5ak4F9fkqHYioH1EfILzzkXPnElQLFEqlSgWi7zxxhtc8x/f55WXXqCmtu6Ag6DG0wpbwA4RzvJcFjfVkbZtEAn5398LmWq47maYMnVMvY0bN3LRRRfy5prVJFPpA0qHcY0CGjDApTVZ0pGhzhO+VqSh/V248XoYHBxT75BDDuHqf/8+bR29B5wCdqYyddW4NARs1Iaf5NJ8JpMKOz06FIhALAGvPQ9N02DmYWPqNzY1kUgkuO/+pVTlMgdsFozLDFBAuwjnRF3Oz6aBUT9eypcCjIHqerjxv6B509g2lOIrX/kKC085ma7ODpRSfzkACJAHLqvJkHEiY/o/MgOGZDcCPR3w37+AYnFMOzU1NVx++RXs7Mr/5VDABjYaw6JMinOz6ZHRLpufXm0IANeyRtCKJeDlp+CQw2Ha9LFUaGwkHo9x/wPLDggVrH2d+j0iLHAi/E0uPdr3gaV4Nd/POWvf4qJ177C5WAyjAYAYyE2Exf8JW7eM/UGWxQUXXMBJJ55Ad3fXfqfCPgPQJsJl1RlqXWdE+FB0BQHf29zCE4Ml7unt50d/2kphOCoAERd2bIElt0EQjGm3traOK678N9o7evc7AHtNgdDwGC5LJvhqdQZbxgwjS1rbWLSzk+lOhKxl8djAAEd5LrMqEmU9EIhVwItPwswj3+cNGhsbcZwIS5c9uF+psNcAlIB6S/HjCdVUuaOETyle7+vjy82bmWArlFIoC1IRmycLAacnK8i6owyoE4W1a2D+iVCRHEOFQ6YewsqVz9Pa+i6u6/3foYANbNGGK3OVTI16YEZGp9+2Wdw7SB4XrW3y/UV6uvvJt/WxSUX4aXsXRW1GBNGLQvM6uPuOMEwCRgxBEFBfX893v3s5rW37Twv22ApbwLsinBd1uaGpjoRljSh/scDgoXPYdvGl4HmI1hijsSybV1e/ype+8EVKkxr4VW2Gs7PpEeCUgp3b4brbYN6nR8VXwfd9rrn2Gq65+ns0TWoa97XCHi+GdHkGfKc6S8KyR4RPAC9GbPULTNvZBvNPGFNvytSprL7sn7n2Bz/kKifCkfEYkzx3pH6yEn72E/J1E+j0PHo6whVjvq8PS4R0OvnnnwE2sN4YrqtMcXFtbkTMhmKCIjQ3VTWw+BaorQORcIIoRXPzJj571pm8vrOdf63KctWEapyhsGBZdA0OcEX/IM/05mnZsIWu9zy/Opsklc4gYg48AAroE2FOxObO+jpqHHs09cdEAHZsRX3tEtS3vzMS+8vlgQfu57zzzocpjayoqmRhOokYQRTcuLONK7du5NgZRzHrmOPJZTKkc1Wkczly2SzLly9nye23MnFi/bhRYbcpEMZ8uDSToiai8LUe9j0WKrT8IiAaqurgluuxjzse6+Nzx7Rzxhln8o2vf42bbvk5V9s2szyXBtflqb4eFve2McdWXDt1OtMv+xdMZSXKGETCqFBdXc3vf/8YpUKBiOMcuDBoAc0i/H3c48uVKcQIRgSRkMKP9XVRZUfwUBgBQZBAY7a9i33CSShvJIQ5jsPkKVNYftedvKmgFsXECPywYxvbtObS2kmcuLUZXT0RffhsdMnHDwJKpRLZbI6qqmqW3Hk3uez4eIPdAqAE1FiKa7NpqiwL3xiMCBEUawsDfKtrC7VicZgbRxuDMYJxo+iXn0KaphOZPed9i56aCfU8ePsdtCQTvNg/wOO+4jQ3yTfSlVjRCsyzf0Q+eRymtg4JfEQEYwyNjQ10d3ey8oXnSKVS+wzChwJgl0f/RxUJjo96lIxBRFBA3mhu6t1OUTRr/EFmWi51tkMwNEMSlQTPP4N7wsmoXA4dBBQLBQb7+4k6EVa/8iId3d00K5taZfP9yhQNto2PwhQGkNY25FPzEMdBjEZrjet6NDY18eijv8UYg2VZ+w+AIa9/jhPhmxUJbCQcXREsgT8MdvFIqYeMZQHCpmCQoyJxYqgQBKWw8r2s3/YuK7Zv54nly3j4rjtYfsMi7r/hB6zavB0lgo7HOdWJcF48FtLLGMSLIi8/g9RPxsw6HBMEiAhBEJDL5ajMZLnn3gf2mQq7BECAQCl+kIjTZFuUyulrS4RtusithR14gK0ETyk6xWdAC7PsGEMC0eu43PjKY6y4+2E2P/ss/dvexMvlSMw+jhNPOZ2amlo2rXmNtV6UjyvFJNsiEIMxBpNII889jRw7D1NdgwmC8HMxNDY00Na2gzdef5V4omJsEmY8ooAFtIhwiesw07YoBHrY8AXAitJOSmjiljX8eaUV4fpBoUEKnOi5BCKs8HfSXOEyb5rLF396H5WzjiAWi+FFPTzPo6WlhQ0bN7Buy2YWKcVUpai1LQIRlLKQ/jz84mbkiqsQz0XEoLUhnkjw1a9eyFNP/h6tg72mwv86AxTQrhQXODbTVVn4jGALrNF9rDCdxI1B/CIy4GO6fDZvL9EST7IW4a+UzTbJ86DuIGW7fGFHP9Nmz6Vm4anEYjFsy0JrQzaTobqmhiW3/pLWTJoKrTnashCRUFCjcczTTyDTZyKHzsToABEIAk2uKkcymWbZ8l+Ry1buFRV2CUAXME8pDlMhp5UI3SZgubRRtCO44pKccDi1sz5F06cX0LTwdFpbWljX10Mf8JopstJ4fIEUR6dr6b37LuyTFuBMmoT2fcQYjNE0NTYyODDAy48/zgvpNHNFaCzriBiDJNOYF55H5h0PmSwSBOHnCI0NjWzd2sLGDeuJxmLjB4AACWC7wLECFUbQBp6xulnbnudzn/8mX7rhdhZ86ULmf+5cjjvtDE46+WSSyRT3/nIJ7dlKngsszsTlfBUJxQ6hsHUr8QULUNEoRmu0Nriuw6RJk3j88cfQhQKblOJToogbKYuphWltxRSKqE8ei7EsxGiMNkSjUSZMrOfB5Q8Qi8fHVwQd4B3ANsJcgW1qgN9FOjjCifKJt1up/fy5pCZPxvU87EgoJ5MmT+ZPf2rmzZdWEUul+CegXgTfGCQex39+JXryZOIfOxqjNSD4fkA2myOby3HPHXfTnq2kQhvmlEVXjEEqKpA/PIWeNQs1fRoS6JAmWlNVU000GueR3z5CJrNnVPjQKJACngUmYXgrkqfduHwmyBBt2UJPVxeZhQuxRzk9z/Noamri5zfdhJVKUo8wU5fNkdZIqoLB3zyEd/oZuHV1IRVEMEbT2NhEx8423nlxJS8mkxxlDPXa4JepYOIx9Isvwfz5qHRluNwWQaFoaGhgw4b1bN++bY+SJ7vlBCuAP6JYYaJcVIoyo6Tx05UUn30OM2MGlUcdNeb79fX1ZHJVLL/rXtbkMhwdaOoCgy+CwUJ3dlIoFqmYPx8ikXA6GxOanMYmfv3gMhzbptlSfCIwxLQh0GBsG9OyBe062HOPQcrb7UZrEokENTW1LFt6P8lkanwBUOW8//lGOHvQL4+mAcej75FHSZx9FrGamjF1pk+fzob17/DamtX0VFQwt6TxdNnkJFOUnnsWjjiC+KzD0OX4HgQBVVVVpNKVLLt/KZ25DHExHF7S4YrRGCSZRD/9NObIOdhTpiA6QABjNLW1tYDFU08+QTq9e1TYbQAMkBb4WEHjBILWgrEjmJ4O8oUCVaecgj1qhRaLxZgyZQp33PwzWtJpckpx6KDGGIUxgiiHgZdWEj91IZFMtgxCuI3U2NjElpbNtK57k1eTSWYbYUJRCEyYNRNs9NvrsI6fh5WsgLI9t22b+voGXnnlFfL5PmzbHr+kqAesthRZFIfmw1kggUa8JIOrwtHMzp5d1g5BjDBx4gQy2Wp+fdc9PKeLfLIvT67QT1DoxwQF/O5uCqUSyXnHIZaNGEMQaGKxKPX19dx22+0M5nvY1J/nmMF+YuW6EhTRO9uJnLwAa2I9ovXwc9PpNK7r8dBvfrNbgrjHOcEeBdd0FDgsX8JXCqVAgiKSTXH080+TnTEjtKvGAEK+L8/SZUt58plnqA4CPut6RGNRVDSOisfBdciefhrR+nqCko8p22AxwsMPP8Q7b68jkkgwS1nMjjhILIryopDN4M2eg3Kdch6iPKK2TeuOVi65+O8YGBj40FmwRwAooF/BzEC4ZHsfFYHBAMq20bqH1Le+xdxFi7A8b9i3D5WBgX6CIMBSVghamVZGBO37GG2GgdPlKQ1hmENAi2CG9lpFEDGI7yNGxuw9KqUIdMCPFy3isUcfIpPN7XIW7JGBFqBCYFXE4g/ZKAaNQaO1D1aSzsWLaX7kEZRlDS9aAh3g+yUiEQfP87BsG4MKba4foEujOi/hJRI6RB1oxBi01qEF9n1MqYQpFZFSKeyYGrsJKwgRO0JlZZqS74//voABakW4L+7yTsJFMPgYAgnVeP23L6b9jTewPTccLSPDcT7syNA11FkZHlFjwuX2cB0pvy9nnwwjSVgZ3nYedSmF5TiUBgfYvn4DsWRy/ETwvaiVFHR4Dkf0F4mIQSNgOei+LtrffAtv2jSimSyW44TxunxGQt5zbECGRHP4tfxvOOU2lH6TYbUXMcPLbUb/zffxW3ew6t57WfL4o6RS6VH7leMkgmOSJUrxt/2DLGzrHlmNWzbGFEMX+ddfJHnkkdhelKBUKi9+wh8vxoTvdYAEGowJnaIYRBsov0q5Y4iEal+uhxEwugwA4f3ODrpXreJGKbK5to5YOSW/XwAYKnml+If2bmbk+wnKhFTKAjHocF58IHi7AnZfzir8LpfhznSSamN2K0WyT8fkFOAgLM2m+HqxSMYvobEQCQCFUjbKGn1ERL0/cyO7klx267sCOGJoTsT5daqC3G52fp8BECAq0GxbLK3J8rn2TjKl0rApQUDp99dRY/eTPrBd9QH3uyqdrstD2RSmrFG7C8C4nBNUZSo0asMxA4M0FEokdLCLb8uHAKtGBLIsoKhRAqqGIpKiZFm0uQ4vxaNssS1ismfZwXE7KKkAH+hVCguIjY7RezGzpAxUGDlGABkDRHmzFiApgrsXqdFxOyor5cZyIiN0lX1t8QPu5YOpI3v5uHE/K3ygDrmO13MO/o+RgwAcBOAgAAcBOAjAQQAOAvCRLf8DJLBGh5wahawAAAAASUVORK5CYII=")
ip=''
api_key=''
file_name=''
class printer_settings_frame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Printer Settings", pos = wx.DefaultPosition, size = wx.Size( 580,710 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetIcon(icon.GetIcon())
		Publisher.subscribe(self.connection_data, ("ip_api"))
		self.menu = wx.MenuBar( 0 )
		self.menu_file = wx.Menu()
		self.open_file_menu = wx.MenuItem( self.menu_file, wx.ID_ANY, u"Open...", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_file.AppendItem( self.open_file_menu )

		self.save_file_menu = wx.MenuItem( self.menu_file, wx.ID_ANY, u"Save", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_file.AppendItem( self.save_file_menu )

		self.recent_file_menu = wx.Menu()
		self.menu_file.AppendSubMenu( self.recent_file_menu, u"Recent Files" )

		self.menu_file.AppendSeparator()

		self.quit_file_menu = wx.MenuItem( self.menu_file, wx.ID_ANY, u"Quit", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_file.AppendItem( self.quit_file_menu )

		self.menu.Append( self.menu_file, u"File" )

		self.menu_settings = wx.Menu()
		self.slicing_settings_menu = wx.MenuItem( self.menu_settings, wx.ID_ANY, u"Slicing Options", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_settings.AppendItem( self.slicing_settings_menu )

		self.preferences_settings_menu = wx.MenuItem( self.menu_settings, wx.ID_ANY, u"Preferences", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_settings.AppendItem( self.preferences_settings_menu )

		self.menu.Append( self.menu_settings, u"Settings" )

		self.menu_help = wx.Menu()
		self.about_help_menu = wx.MenuItem( self.menu_help, wx.ID_ANY, u"About Fracktory", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_help.AppendItem( self.about_help_menu )

		self.menu.Append( self.menu_help, u"Help" )

		self.SetMenuBar( self.menu )

		Outer1 = wx.BoxSizer( wx.VERTICAL )

		Inner1 = wx.BoxSizer( wx.VERTICAL )

		Inner1.SetMinSize( wx.Size( 60,60 ) )
		SubInner11 = wx.FlexGridSizer( 0, 3, 0, 82 )
		SubInner11.SetFlexibleDirection( wx.HORIZONTAL )
		SubInner11.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		SubInner11.SetMinSize( wx.Size( 30,30 ) )
		self.printer_status_label = wx.StaticText( self, wx.ID_ANY, u"Printer Status:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.printer_status_label.Wrap( -1 )
		self.printer_status_label.SetFont( wx.Font( 11, 74, 90, 92, False, "Sans" ) )

		SubInner11.Add( self.printer_status_label, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.print_status_output = wx.StaticText( self, wx.ID_ANY, u"Not Connected", wx.DefaultPosition, wx.Size( 110,-1 ), 0 )
		self.print_status_output.Wrap( -1 )
		SubInner11.Add( self.print_status_output, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		connect_refresh = wx.FlexGridSizer( 1, 0, 0, 0 )
		connect_refresh.SetFlexibleDirection( wx.BOTH )
		connect_refresh.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.config_btn = wx.Button( self, wx.ID_ANY, u"Config", wx.DefaultPosition, wx.DefaultSize, 0 )
		connect_refresh.Add( self.config_btn, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		SubInner11.Add( connect_refresh, 1, wx.EXPAND, 5 )


		Inner1.Add( SubInner11, 1, wx.SHAPED, 2 )

		SubInner21 = wx.FlexGridSizer( 0, 3, 0, 60 )
		SubInner21.AddGrowableCol( 0 )
		SubInner21.AddGrowableRow( 0 )
		SubInner21.SetFlexibleDirection( wx.HORIZONTAL )
		SubInner21.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_ALL )

		SubInner21.SetMinSize( wx.Size( 30,30 ) )

		SubInner21.AddSpacer( ( 90, 0), 1, wx.SHAPED, 5 )

		serial_baudrate_Inner = wx.FlexGridSizer( 2, 0, 0, 0 )
		serial_baudrate_Inner.SetFlexibleDirection( wx.BOTH )
		serial_baudrate_Inner.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		serial_Inner = wx.FlexGridSizer( 0, 2, 0, 0 )
		serial_Inner.SetFlexibleDirection( wx.BOTH )
		serial_Inner.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.serial_label = wx.StaticText( self, wx.ID_ANY, u"Serial Port:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.serial_label.Wrap( -1 )
		serial_Inner.Add( self.serial_label, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		serial_choiceChoices = []
		self.serial_choice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, serial_choiceChoices, 0 )
		self.serial_choice.SetSelection( 0 )
		serial_Inner.Add( self.serial_choice, 0, wx.ALL, 5 )


		serial_baudrate_Inner.Add( serial_Inner, 1, wx.EXPAND, 5 )

		baudrate_Inner = wx.FlexGridSizer( 0, 2, 0, 0 )
		baudrate_Inner.SetFlexibleDirection( wx.BOTH )
		baudrate_Inner.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.baudrate_choice = wx.StaticText( self, wx.ID_ANY, u"Baudrate:  ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.baudrate_choice.Wrap( -1 )
		baudrate_Inner.Add( self.baudrate_choice, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		baudrate_choiceChoices = []
		self.baudrate_choice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, baudrate_choiceChoices, 0 )
		self.baudrate_choice.SetSelection( 0 )
		baudrate_Inner.Add( self.baudrate_choice, 0, wx.ALL, 5 )


		serial_baudrate_Inner.Add( baudrate_Inner, 1, wx.EXPAND, 5 )


		SubInner21.Add( serial_baudrate_Inner, 1, wx.SHAPED, 5 )

		self.connect_printer_btn = wx.Button( self, wx.ID_ANY, u"Connect", wx.DefaultPosition, wx.DefaultSize, 0 )
		SubInner21.Add( self.connect_printer_btn, 0, wx.ALL, 5 )


		Inner1.Add( SubInner21, 0, wx.SHAPED, 5 )


		Outer1.Add( Inner1, 1, wx.SHAPED, 4 )

		Inner2 = wx.BoxSizer( wx.VERTICAL )

		SubInner13 = wx.FlexGridSizer( 0, 3, 0, 85 )
		SubInner13.SetFlexibleDirection( wx.BOTH )
		SubInner13.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		SubInner13.SetMinSize( wx.Size( 100,-1 ) )
		self.load_file_label = wx.StaticText( self, wx.ID_ANY, u"Load File :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.load_file_label.Wrap( -1 )
		self.load_file_label.SetFont( wx.Font( 11, 74, 90, 92, False, "Sans" ) )

		SubInner13.Add( self.load_file_label, 0, wx.ALL, 5 )

		options_btn_Inner = wx.FlexGridSizer( 0, 2, 0, 45 )
		options_btn_Inner.SetFlexibleDirection( wx.BOTH )
		options_btn_Inner.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		optionInner = wx.FlexGridSizer( 2, 0, 0, 0 )
		optionInner.SetFlexibleDirection( wx.BOTH )
		optionInner.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		local_sd_inner = wx.FlexGridSizer( 0, 1, 0, 0 )
		local_sd_inner.SetFlexibleDirection( wx.BOTH )
		local_sd_inner.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		load_optionsChoices = [ u"Local", u"SD" ]
		self.load_options = wx.RadioBox( self, wx.ID_ANY, u"Options", wx.DefaultPosition, wx.Size( 180,-1 ), load_optionsChoices, 1, wx.RA_SPECIFY_COLS )
		self.load_options.SetSelection( 0 )
		local_sd_inner.Add( self.load_options, 0, wx.ALL, 5 )


		optionInner.Add( local_sd_inner, 1, wx.EXPAND, 5 )

		self.upload_file_picker = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.Size( 180,-1 ), wx.FLP_DEFAULT_STYLE )
		optionInner.Add( self.upload_file_picker, 0, wx.ALL, 5 )


		options_btn_Inner.Add( optionInner, 1, wx.EXPAND, 5 )

		self.upload_btn = wx.Button( self, wx.ID_ANY, u"Upload", wx.DefaultPosition, wx.DefaultSize, 0 )
		options_btn_Inner.Add( self.upload_btn, 0, wx.ALL, 5 )


		SubInner13.Add( options_btn_Inner, 1, wx.EXPAND, 5 )


		Inner2.Add( SubInner13, 0, wx.EXPAND, 5 )

		SubInner2 = wx.FlexGridSizer( 0, 3, 0, 70 )
		SubInner2.SetFlexibleDirection( wx.BOTH )
		SubInner2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.retrive_file_label = wx.StaticText( self, wx.ID_ANY, u"Retrive File:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.retrive_file_label.Wrap( -1 )
		self.retrive_file_label.SetFont( wx.Font( 11, 74, 90, 92, False, "Sans" ) )

		SubInner2.Add( self.retrive_file_label, 0, wx.ALL, 5 )

		options_list_Inner = wx.FlexGridSizer( 0, 2, 0, 45 )
		options_list_Inner.SetFlexibleDirection( wx.BOTH )
		options_list_Inner.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		sd_local_list_Inner = wx.FlexGridSizer( 2, 0, 0, 0 )
		sd_local_list_Inner.SetFlexibleDirection( wx.BOTH )
		sd_local_list_Inner.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		local_sd_Inner = wx.FlexGridSizer( 0, 2, 0, 0 )
		local_sd_Inner.SetFlexibleDirection( wx.BOTH )
		local_sd_Inner.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		retrive_optionsChoices = [ u"Local", u"SD" ]
		self.retrive_options = wx.RadioBox( self, wx.ID_ANY, u"Options", wx.DefaultPosition, wx.Size( 180,-1 ), retrive_optionsChoices, 1, wx.RA_SPECIFY_COLS )
		self.retrive_options.SetSelection( 0 )
		local_sd_Inner.Add( self.retrive_options, 0, wx.ALL, 5 )


		sd_local_list_Inner.Add( local_sd_Inner, 1, wx.EXPAND, 5 )

		files_listChoices = []
		self.files_list = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 180,-1 ), files_listChoices, 0 )
		sd_local_list_Inner.Add( self.files_list, 0, wx.ALL, 5 )


		options_list_Inner.Add( sd_local_list_Inner, 1, wx.EXPAND, 5 )

		retrive_download_Inner = wx.FlexGridSizer( 2, 0, 40, 0 )
		retrive_download_Inner.SetFlexibleDirection( wx.BOTH )
		retrive_download_Inner.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.retrive_btn = wx.Button( self, wx.ID_ANY, u"Retrive Files", wx.DefaultPosition, wx.DefaultSize, 0 )
		retrive_download_Inner.Add( self.retrive_btn, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.download_btn = wx.Button( self, wx.ID_ANY, u"Download File", wx.DefaultPosition, wx.DefaultSize, 0 )
		retrive_download_Inner.Add( self.download_btn, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		options_list_Inner.Add( retrive_download_Inner, 1, wx.EXPAND, 5 )


		SubInner2.Add( options_list_Inner, 1, wx.EXPAND, 5 )


		Inner2.Add( SubInner2, 0, wx.EXPAND, 5 )


		Outer1.Add( Inner2, 1, wx.EXPAND, 5 )

		Inner3 = wx.BoxSizer( wx.VERTICAL )

		SubInner15 = wx.FlexGridSizer( 0, 3, 0, 47 )
		SubInner15.SetFlexibleDirection( wx.BOTH )
		SubInner15.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.bed_temperature_label = wx.StaticText( self, wx.ID_ANY, u"Temperature :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bed_temperature_label.Wrap( -1 )
		self.bed_temperature_label.SetFont( wx.Font( 11, 74, 90, 92, False, "Sans" ) )

		SubInner15.Add( self.bed_temperature_label, 0, wx.ALL, 5 )

		temp_Inner = wx.FlexGridSizer( 3, 3, 0, 0 )
		temp_Inner.SetFlexibleDirection( wx.BOTH )
		temp_Inner.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		temp_Inner.AddSpacer( ( 40, 0), 1, wx.EXPAND, 5 )

		self.actual_label = wx.StaticText( self, wx.ID_ANY, u"Actual", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.actual_label.Wrap( -1 )
		temp_Inner.Add( self.actual_label, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.target_label = wx.StaticText( self, wx.ID_ANY, u"Target", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.target_label.Wrap( -1 )
		temp_Inner.Add( self.target_label, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.nozzle_label = wx.StaticText( self, wx.ID_ANY, u"Nozzle :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.nozzle_label.Wrap( -1 )
		temp_Inner.Add( self.nozzle_label, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.nozzle_actual_label = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30,30 ), 0 )
		self.nozzle_actual_label.Wrap( -1 )
		temp_Inner.Add( self.nozzle_actual_label, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM, 5 )

		self.nozzle_temp_input = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.nozzle_temp_input.SetMinSize( wx.Size( 30,30 ) )

		temp_Inner.Add( self.nozzle_temp_input, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.bed_label = wx.StaticText( self, wx.ID_ANY, u"Bed Label :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bed_label.Wrap( -1 )
		temp_Inner.Add( self.bed_label, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.bed_actual_label = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30,30 ), 0 )
		self.bed_actual_label.Wrap( -1 )
		temp_Inner.Add( self.bed_actual_label, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.bed_temp_input = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bed_temp_input.SetMinSize( wx.Size( 30,30 ) )

		temp_Inner.Add( self.bed_temp_input, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		SubInner15.Add( temp_Inner, 1, wx.EXPAND, 5 )

		retrive_set_btn = wx.FlexGridSizer( 2, 0, 0, 50 )
		retrive_set_btn.SetFlexibleDirection( wx.BOTH )
		retrive_set_btn.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.set_temperature_btn = wx.Button( self, wx.ID_ANY, u"Set", wx.DefaultPosition, wx.DefaultSize, 0 )
		retrive_set_btn.Add( self.set_temperature_btn, 0, wx.ALL, 5 )


		SubInner15.Add( retrive_set_btn, 1, wx.EXPAND, 5 )


		Inner3.Add( SubInner15, 1, wx.EXPAND, 5 )


		Outer1.Add( Inner3, 1, wx.EXPAND, 5 )

		Inner4 = wx.BoxSizer( wx.VERTICAL )

		SubInner2 = wx.FlexGridSizer( 0, 3, 0, 60 )
		SubInner2.SetFlexibleDirection( wx.BOTH )
		SubInner2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.recent_file_label = wx.StaticText( self, wx.ID_ANY, u"Recent File :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.recent_file_label.Wrap( -1 )
		self.recent_file_label.SetFont( wx.Font( 11, 74, 90, 92, False, "Sans" ) )

		SubInner2.Add( self.recent_file_label, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		recent_options = wx.FlexGridSizer( 0, 2, 0, 0 )
		recent_options.SetFlexibleDirection( wx.BOTH )
		recent_options.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		save_to_optionsChoices = [ u"Local", u"SD" ]
		self.save_to_options = wx.RadioBox( self, wx.ID_ANY, u"Save to", wx.DefaultPosition, wx.Size( 180,-1 ), save_to_optionsChoices, 1, wx.RA_SPECIFY_COLS )
		self.save_to_options.SetSelection( 0 )
		recent_options.Add( self.save_to_options, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		SubInner2.Add( recent_options, 1, wx.EXPAND, 5 )

		recent_filesChoices = []
		self.recent_files = wx.ComboBox( self, wx.ID_ANY, u"None", wx.DefaultPosition, wx.Size( 120,-1 ), recent_filesChoices, 0 )
		SubInner2.Add( self.recent_files, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )


		Inner4.Add( SubInner2, 1, wx.EXPAND, 5 )

		SubInner1 = wx.FlexGridSizer( 0, 4, 0, 25 )
		SubInner1.SetFlexibleDirection( wx.BOTH )
		SubInner1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		SubInner1.AddSpacer( ( 152, 0), 1, wx.EXPAND, 5 )

		self.print_btn = wx.Button( self, wx.ID_ANY, u"Print", wx.DefaultPosition, wx.DefaultSize, 0 )
		SubInner1.Add( self.print_btn, 0, wx.ALL, 5 )

		self.pause_btn = wx.Button( self, wx.ID_ANY, u"Pause", wx.DefaultPosition, wx.DefaultSize, 0 )
		SubInner1.Add( self.pause_btn, 0, wx.ALL, 5 )

		self.cancel_btn = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		SubInner1.Add( self.cancel_btn, 0, wx.ALL, 5 )


		Inner4.Add( SubInner1, 0, wx.EXPAND, 5 )


		Outer1.Add( Inner4, 0, wx.EXPAND, 5 )

		Inner5 = wx.BoxSizer( wx.VERTICAL )

		Printer_status_Inner = wx.FlexGridSizer( 0, 3, 0, 60 )
		Printer_status_Inner.SetFlexibleDirection( wx.BOTH )
		Printer_status_Inner.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		Printer_status_Inner.AddSpacer( ( 120, 0), 1, wx.EXPAND, 5 )

		self.percent_bar = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.Size( 180,-1 ), wx.GA_HORIZONTAL )
		self.percent_bar.SetValue( 0 )
		Printer_status_Inner.Add( self.percent_bar, 0, wx.ALL, 5 )

		self.percent_label = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.percent_label.Wrap( -1 )
		Printer_status_Inner.Add( self.percent_label, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		Inner5.Add( Printer_status_Inner, 1, wx.EXPAND, 5 )


		Outer1.Add( Inner5, 1, wx.SHAPED, 5 )


		self.SetSizer( Outer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_MENU, self.open_file_picker, id = self.open_file_menu.GetId() )
		self.Bind( wx.EVT_MENU, self.save_file, id = self.save_file_menu.GetId() )
		self.Bind( wx.EVT_MENU, self.quit, id = self.quit_file_menu.GetId() )
		self.Bind( wx.EVT_MENU, self.about_fracktory, id = self.about_help_menu.GetId() )
		self.config_btn.Bind( wx.EVT_BUTTON, self.config_printer )
		self.connect_printer_btn.Bind( wx.EVT_BUTTON, self.connect_printer )
		self.load_options.Bind( wx.EVT_RADIOBOX, self.load_option_sel )
		self.upload_btn.Bind( wx.EVT_BUTTON, self.upload_file )
		self.retrive_options.Bind( wx.EVT_RADIOBOX, self.retrive_option_sel )
		self.retrive_btn.Bind( wx.EVT_BUTTON, self.retrive_file )
		self.download_btn.Bind( wx.EVT_BUTTON, self.download_file )
		self.set_temperature_btn.Bind( wx.EVT_BUTTON, self.set_temperature )
		self.print_btn.Bind( wx.EVT_BUTTON, self.print_file )
		self.pause_btn.Bind( wx.EVT_BUTTON, self.pause_print )
		self.cancel_btn.Bind( wx.EVT_BUTTON, self.off_printer )

	def __del__( self ):
		# Disconnect Events
		self.Unbind( wx.EVT_MENU, id = self.open_file_menu.GetId() )
		self.Unbind( wx.EVT_MENU, id = self.save_file_menu.GetId() )
		self.Unbind( wx.EVT_MENU, id = self.quit_file_menu.GetId() )
		self.Unbind( wx.EVT_MENU, id = self.about_help_menu.GetId() )
		self.config_btn.Unbind( wx.EVT_BUTTON, None )
		self.connect_printer_btn.Unbind( wx.EVT_BUTTON, None )
		self.load_options.Unbind( wx.EVT_RADIOBOX, None )
		self.upload_btn.Unbind( wx.EVT_BUTTON, None )
		self.retrive_options.Unbind( wx.EVT_RADIOBOX, None )
		self.retrive_btn.Unbind( wx.EVT_BUTTON, None )
		self.download_btn.Unbind( wx.EVT_BUTTON, None )
		self.set_temperature_btn.Unbind( wx.EVT_BUTTON, None )
		self.print_btn.Unbind( wx.EVT_BUTTON, None )
		self.pause_btn.Unbind( wx.EVT_BUTTON, None )
		self.cancel_btn.Unbind( wx.EVT_BUTTON, None )


	# Virtual event handlers, overide them in your derived class
	def printer_status_update(self):
		while(True):
			url = 'http://'+ip+'/api/connection'
			headers = {'X-Api-Key':api_key}
			response = requests.get(url,headers=headers)
			temp=response.json()
			time.sleep(1)
			wx.CallAfter(self.print_status_output.SetLabel,temp['current']['state'])
			if temp['current']['state']!="Printing":
				wx.CallAfter(self.percent_bar.SetValue,0)
				wx.CallAfter(self.percent_label.SetLabel,'')
				wx.CallAfter(self.percent_bar.Hide)
				wx.CallAfter(self.percent_label.Hide)
			if temp['current']['state']=="Operational" or temp['current']['state']=="Printing":
				url = 'http://'+ip+'/api/printer'
				headers = {'X-Api-Key':api_key}
				response = requests.get(url,headers=headers)
				temp=response.json()
				time.sleep(1)
				wx.CallAfter(self.nozzle_actual_label.SetLabel,str(temp['temperature']['tool0']['actual']))
				wx.CallAfter(self.bed_actual_label.SetLabel,str(temp['temperature']['bed']['actual']))
				wx.CallAfter(self.nozzle_temp_input.SetValue,str(temp['temperature']['tool0']['target']))
				wx.CallAfter(self.bed_temp_input.SetValue,str(temp['temperature']['tool0']['target']))
			#self.set_temperature_input.SetValue(temp['current']['state']
	def connection_data(self,msg):
		global ip
		global api_key
		ip=msg.data[0]
		api_key=msg.data[1]
		url = 'http://'+ip+'/api/connection'
		headers={'X-Api-Key':api_key}
		response = requests.get(url,headers=headers)
		temp=response.json()
		#self.print_status_output.SetLabel(temp['current']['state'])
		self.serial_choice.SetItems(temp['options']['ports'])
		self.baudrate_choice.SetItems(map(str,temp['options']['baudrates']))
		t1=Thread(target=self.printer_status_update, args=())
		t1.start()
	def open_file_picker( self, event ):
		event.Skip()

	def save_file( self, event ):
		event.Skip()

	def quit( self, event ):
		self.Close()

	def about_fracktory( self, event ):
		event.Skip()

	def config_printer( self, event ):
		a = Connection_Settings(self).ShowModal()

	def connect_printer( self, event ):
		port=self.serial_choice.GetString(self.serial_choice.GetSelection())
		baudrate=int(self.baudrate_choice.GetString(self.baudrate_choice.GetSelection()))
		url = 'http://'+ip+'/api/connection'
		payload = {"command": "connect","port": port,"baudrate": baudrate}
		headers = {'content-type': 'application/json','X-Api-Key':api_key}
		response = requests.post(url,data=json.dumps(payload),headers=headers)

	def load_option_sel( self, event ):
		event.Skip()

	def upload_file( self, event ):
		if ip!='' and api_key!='':
			file_path=self.upload_file_picker.GetPath()
			if len(file_path)!=0:
				upload_file_name=os.path.basename(file_path)
				f=open(file_path,'r')
				data=f.read()
				f.close()
				#data=unicodedata.normalize('NFKD', d).encode('ascii', 'ignore')
				#data = unicode(d, "utf-8")
				if self.load_options.GetSelection()==0:

					#self.y_axis_input.SetValue(file_path)
					url = "http://"+ip+"/api/files/local"
					payload = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"select\"\r\n\r\ntrue\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"print\"\r\n\r\nfalse\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\""+upload_file_name+"\"\r\nContent-Type: application/octet-stream\r\n\r\n"+data+"\r\n-----011000010111000001101001--"
					headers = {
			    	'content-type': "multipart/form-data; boundary=---011000010111000001101001",
			    	'x-api-key': api_key,
			    	'cache-control': "no-cache",
			    	'postman-token': "6b44c087-7bf6-ebfb-980a-6e0188f08b1d"
			    	}
					response = requests.post(url, data=payload, headers=headers)
					result=response.json()
				else:
					url = "http://"+ip+"/api/files/sdcard"
					payload = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"select\"\r\n\r\ntrue\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"print\"\r\n\r\nfalse\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\""+upload_file_name+"\"\r\nContent-Type: application/octet-stream\r\n\r\n"+data+"\r\n-----011000010111000001101001--"
					headers = {
			    	'content-type': "multipart/form-data; boundary=---011000010111000001101001",
			    	'x-api-key': api_key,
			    	}
					response = requests.post(url, data=payload, headers=headers)
					result=response.json()
			else:
				msg_dialog = wx.MessageDialog(None,'No File Selected','Error',wx.OK | wx.ICON_ERROR)
				msg_dialog.ShowModal()
		else:
			msg_dialog = wx.MessageDialog(None,'Connection not Established','Error',wx.OK | wx.ICON_ERROR)
			msg_dialog.ShowModal()

	def retrive_option_sel( self, event ):
		event.Skip()

	def retrive_file( self, event ):
		if ip!='' and api_key!='':
			self.files_list.Clear()
			if self.retrive_options.GetSelection()==0:
				url='http://'+ip+'/api/files/local'
				response = requests.get(url, headers={'X-Api-Key':api_key})
				f=response.json()
				file_l=[]
				a=f["files"]
				#self.z_axis_input.SetValue()
				count=0
				for i in a:
					temp=i["name"]
					self.files_list.Insert(temp,count)
					count=count+1
			else:
				url='http://'+ip+'/api/files/sdcard'
				response = requests.get(url, headers={'X-Api-Key':api_key})
				f=response.json()
				file_l=[]
				a=f["files"]
				#self.z_axis_input.SetValue()
				count=0
				for i in a:
					temp=i["name"]
					self.files_list.Insert(temp,count)
					count=count+1
		else:
			msg_dialog = wx.MessageDialog(None,'Connection not Established','Error',wx.OK | wx.ICON_ERROR)
			msg_dialog.ShowModal()

	def download_file( self, event ):
		if self.files_list.GetSelection()==-1:
			msg_dialog = wx.MessageDialog(None,'No Files selected','Error',wx.OK | wx.ICON_ERROR)
			msg_dialog.ShowModal()
		elif self.retrive_options.GetSelection()==0:
			file_name=self.files_list.GetString(self.files_list.GetSelection())
			a=Download_dialog(self,file_name).ShowModal()
		else:
			msg_dialog = wx.MessageDialog(None,"Sorry! Can't Download from SD",'Error',wx.OK | wx.ICON_ERROR)
			msg_dialog.ShowModal()


	def set_temperature( self, event ):
		url = "http://"+ip+"/api/printer/tool"
		payload = "{\n  \"command\": \"target\",\n  \"targets\": {\n    \"tool0\": "+int(self.nozzle_temp_input.GetValue())+"\n  }\n}"
		headers = {
    	'x-api-key': api_key,
    	'content-type': "application/json",
    	'cache-control': "no-cache",
    	'postman-token': "16ba2da6-1952-e3e6-9833-16a7a815d0bd"
    	}
		response = requests.request("POST", url, data=payload, headers=headers)
		url = "http://"+ip+"/api/printer/bed"
		payload = "{\n  \"command\": \"target\",\n  \"target\": "+int(self.bed_temp_input.GetValue())+"\n}"
		headers = {
    	'x-api-key': api_key,
    	'content-type': "application/json",
    	'cache-control': "no-cache",
    	'postman-token': "6d951b61-e48a-4422-8ee7-1f437e6f8651"
    	}
		response = requests.request("POST", url, data=payload, headers=headers)

	def print_file( self, event,file_path="" ):
		if file_path!="":
			upload_file_name=os.path.basename(file_path)
			f=open(file_path,'r')
			data=f.read()
			f.close()
			if self.recent_options.GetSelection()==1:
				if os.path.getsize(file_path)>10000000:
					msg_dialog = wx.MessageDialog(None,'File greater than 10MB.Switch to Local?','Check',wx.YES_NO	 | wx.ICON_INFORMATION)
					ok=msg_dialog.ShowModal()
					if ok==wxID_YES:
						self.recent_options.SetSelection(0)
						url = "http://"+ip+"/api/files/local"
						payload = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"select\"\r\n\r\ntrue\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"print\"\r\n\r\ntrue\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\""+upload_file_name+"\"\r\nContent-Type: application/octet-stream\r\n\r\n"+data+"\r\n-----011000010111000001101001--"
						headers = {
			    		'content-type': "multipart/form-data; boundary=---011000010111000001101001",
			    		'x-api-key': api_key,
			    		}
						response = requests.post(url, data=payload, headers=headers)
						result=response.json()
						self.percent_bar.Show()
						self.percent_label.Show()
						Thread(target=self.printer_update, args=()).start()
					else:
						url = "http://"+ip+"/api/files/sdcard"
						payload = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"select\"\r\n\r\ntrue\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"print\"\r\n\r\ntrue\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\""+upload_file_name+"\"\r\nContent-Type: application/octet-stream\r\n\r\n"+data+"\r\n-----011000010111000001101001--"
						headers = {
			    		'content-type': "multipart/form-data; boundary=---011000010111000001101001",
			    		'x-api-key': api_key,
			    		}
						response = requests.post(url, data=payload, headers=headers)
						result=response.json()
						self.percent_bar.Show()
						self.percent_label.Show()
						Thread(target=self.printer_update, args=()).start()
				else:
					url = "http://"+ip+"/api/files/sdcard"
					payload = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"select\"\r\n\r\ntrue\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"print\"\r\n\r\ntrue\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\""+upload_file_name+"\"\r\nContent-Type: application/octet-stream\r\n\r\n"+data+"\r\n-----011000010111000001101001--"
					headers = {
					'content-type': "multipart/form-data; boundary=---011000010111000001101001",
					'x-api-key': api_key,
					}
					response = requests.post(url, data=payload, headers=headers)
					result=response.json()
					self.percent_bar.Show()
					self.percent_label.Show()
					Thread(target=self.printer_update, args=()).start()
			else:
				url = "http://"+ip+"/api/files/local"
				payload = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"select\"\r\n\r\ntrue\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"print\"\r\n\r\ntrue\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\""+upload_file_name+"\"\r\nContent-Type: application/octet-stream\r\n\r\n"+data+"\r\n-----011000010111000001101001--"
				headers = {
				'content-type': "multipart/form-data; boundary=---011000010111000001101001",
				'x-api-key': api_key,
				}
				response = requests.post(url, data=payload, headers=headers)
				result=response.json()
				self.percent_bar.Show()
				self.percent_label.Show()
				Thread(target=self.printer_update, args=()).start()

		else:
			if self.retrive_options.GetSelection()==0:
				url = 'http://'+ip+'/api/files/local/'+self.files_list.GetString(self.files_list.GetSelection())
				payload = {"command": "select"}
				headers = {'content-type': 'application/json','X-Api-Key':api_key}
				response = requests.post(url,data=json.dumps(payload),headers=headers)
				url = 'http://'+ip+'/api/job'
				payload = {"command": "start"}
				headers = {'content-type': 'application/json','X-Api-Key':api_key}
				response = requests.post(url,data=json.dumps(payload),headers=headers)
				self.percent_bar.Show()
				self.percent_label.Show()
				Thread(target=self.printer_update, args=()).start()
			else:
				url = 'http://'+ip+'/api/files/sdcard/'+self.files_list.GetString(self.files_list.GetSelection())
				payload = {"command": "select"}
				headers = {'content-type': 'application/json','X-Api-Key':api_key}
				response = requests.post(url,data=json.dumps(payload),headers=headers)
				url = 'http://'+ip+'/api/job'
				payload = {"command": "start"}
				headers = {'content-type': 'application/json','X-Api-Key':api_key}
				response = requests.post(url,data=json.dumps(payload),headers=headers)
				self.percent_bar.Show()
				self.percent_label.Show()
				Thread(target=self.printer_update, args=()).start()
	def printer_update(self):
		#i=0
		#i=i+1
		#self.y_axis_input.SetValue(str(i))
		url = 'http://'+ip+'/api/job'
		headers = {'X-Api-Key':api_key}
		response = requests.get(url,headers=headers)
		temp=response.json()
		wx.CallAfter(self.percent_bar.Show)
		wx.CallAfter(self.percent_label.Show)
		#self.y_axis_input.SetValue(temp['state'])
		while(temp['state']=='Printing'):
			time.sleep(5)
			wx.CallAfter(self.percent_bar.SetValue,((temp['progress']['completion'])))
			url = 'http://'+ip+'/api/job'
			headers = {'X-Api-Key':api_key}
			response = requests.get(url,headers=headers)
			temp=response.json()
			wx.CallAfter(self.percent_label.SetLabel,str(round(temp['progress']['completion'],2))+"% completed")
	def pause_print( self, event ):
		url = 'http://'+ip+'/api/job'
		payload = {"command": "pause"}
		headers = {'content-type': 'application/json','X-Api-Key':api_key}
		response = requests.post(url,data=json.dumps(payload),headers=headers)

	def off_printer( self, event ):
		url = 'http://'+ip+'/api/job'
		payload = {"command": "cancel"}
		headers = {'content-type': 'application/json','X-Api-Key':api_key}
		response = requests.post(url,data=json.dumps(payload),headers=headers)


###########################################################################
## Class Connection_Settings
###########################################################################

class Connection_Settings ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Connection Settings", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

		Outer1 = wx.BoxSizer( wx.VERTICAL )

		Inner1 = wx.BoxSizer( wx.VERTICAL )

		SubInner1 = wx.FlexGridSizer( 0, 2, 0, 10 )
		SubInner1.SetFlexibleDirection( wx.BOTH )
		SubInner1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.ip_label = wx.StaticText( self, wx.ID_ANY, u"Enter IP Address :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ip_label.Wrap( -1 )
		SubInner1.Add( self.ip_label, 0, wx.ALL, 5 )

		self.ip_input = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		self.ip_input.SetToolTipString( u" Format : X.X.X.X \nExample: 127.0.0.1" )

		SubInner1.Add( self.ip_input, 0, wx.ALL, 5 )


		Inner1.Add( SubInner1, 1, wx.EXPAND, 5 )


		Outer1.Add( Inner1, 1, wx.EXPAND, 5 )

		Inner2 = wx.BoxSizer( wx.VERTICAL )

		SubInner1 = wx.FlexGridSizer( 0, 2, 0, 32 )
		SubInner1.SetFlexibleDirection( wx.BOTH )
		SubInner1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.api_key_label = wx.StaticText( self, wx.ID_ANY, u"Enter API Key :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.api_key_label.Wrap( -1 )
		SubInner1.Add( self.api_key_label, 0, wx.ALL, 5 )

		self.api_input = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		self.api_input.SetToolTipString( u"alphanumeric unique key" )

		SubInner1.Add( self.api_input, 0, wx.ALL, 5 )


		Inner2.Add( SubInner1, 1, wx.EXPAND, 5 )


		Outer1.Add( Inner2, 1, wx.EXPAND, 5 )

		Inner3 = wx.BoxSizer( wx.VERTICAL )

		SubInner1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		SubInner1.SetFlexibleDirection( wx.BOTH )
		SubInner1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		SubInner1.AddSpacer( ( 135, 0), 1, wx.EXPAND, 5 )

		self.remember_config = wx.CheckBox( self, wx.ID_ANY, u"Remember Me", wx.DefaultPosition, wx.DefaultSize, 0 )
		SubInner1.Add( self.remember_config, 0, wx.ALL, 5 )


		Inner3.Add( SubInner1, 1, wx.EXPAND, 5 )


		Outer1.Add( Inner3, 1, wx.EXPAND, 5 )

		Inner4 = wx.BoxSizer( wx.VERTICAL )

		SubInner1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		SubInner1.SetFlexibleDirection( wx.BOTH )
		SubInner1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		SubInner1.AddSpacer( ( 140, 0), 1, wx.EXPAND, 5 )

		submit_reset_btn = wx.FlexGridSizer( 0, 2, 0, 20 )
		submit_reset_btn.SetFlexibleDirection( wx.BOTH )
		submit_reset_btn.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.submit_btn = wx.Button( self, wx.ID_ANY, u"Submit", wx.DefaultPosition, wx.DefaultSize, 0 )
		submit_reset_btn.Add( self.submit_btn, 0, wx.ALL, 5 )

		self.reset_btn = wx.Button( self, wx.ID_ANY, u"Reset", wx.DefaultPosition, wx.DefaultSize, 0 )
		submit_reset_btn.Add( self.reset_btn, 0, wx.ALL, 5 )


		SubInner1.Add( submit_reset_btn, 1, wx.EXPAND, 5 )


		Inner4.Add( SubInner1, 1, wx.EXPAND, 5 )


		Outer1.Add( Inner4, 1, wx.EXPAND, 5 )
		f=open('data.txt','r')
		data=f.read()
		if data=='':
			pass
		else:
			data=data.split('\n')
			self.ip_input.SetValue(data[0])
			self.api_input.SetValue(data[1])
		f.close()

		self.SetSizer( Outer1 )
		self.Layout()
		Outer1.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.submit_btn.Bind( wx.EVT_BUTTON, self.submit_connection )
		self.reset_btn.Bind( wx.EVT_BUTTON, self.reset_connection )

	def __del__( self ):
		# Disconnect Events
		self.submit_btn.Unbind( wx.EVT_BUTTON, None )
		self.reset_btn.Unbind( wx.EVT_BUTTON, None )


	# Virtual event handlers, overide them in your derived class
	def submit_connection( self, event ):
		flag_ip=0
		flag_api=0
		api_key=self.api_input.GetValue()
		ip = self.ip_input.GetValue()
		try:
			socket.inet_pton(socket.AF_INET, ip)
		except AttributeError:
			try:
				socket.inet_aton(ip)
			except socket.error:
				flag_ip=1
		except socket.error:  # not a valid address
			flag_ip=1
		if not api_key.isalnum():
				flag_api=1
		if flag_api and flag_ip:
			dial_both = wx.MessageDialog(None, 'Error:Invalid API Key and IP Address', 'Error',wx.OK | wx.ICON_ERROR)
			dial_both.ShowModal()
			dial_both.Destroy()
		elif flag_api:
			dial_api = wx.MessageDialog(None, 'Error:Invalid API Key', 'Error',wx.OK | wx.ICON_ERROR)
			dial_api.ShowModal()
		elif flag_ip:
			dial_ip = wx.MessageDialog(None, 'Error:Invalid IP Address', 'Error',wx.OK | wx.ICON_ERROR)
			dial_ip.ShowModal()
		else:
			if self.remember_config.IsChecked():
				f=open('data.txt','w')
				f.write(ip+'\n'+api_key)
				f.close()
			d=[]
			d.append(ip)
			d.append(api_key)
			Publisher.sendMessage(("ip_api"),d)
        	self.Close()
	def reset_connection( self, event ):
		self.ip_input.SetValue("")
		self.api_input.SetValue("")


###########################################################################
## Class Download_dialog
###########################################################################

class Download_dialog ( wx.Dialog ):

	def __init__( self, parent,download_file_name):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Download File", pos = wx.DefaultPosition, size = wx.Size( 400,200 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.file_name=download_file_name
		Inner1 = wx.BoxSizer( wx.VERTICAL )

		SubInner1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		SubInner1.SetFlexibleDirection( wx.BOTH )
		SubInner1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.select_directory_label = wx.StaticText( self, wx.ID_ANY, u"Select Directory :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.select_directory_label.Wrap( -1 )
		SubInner1.Add( self.select_directory_label, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.file_save_directory = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		SubInner1.Add( self.file_save_directory, 0, wx.ALL, 5 )


		Inner1.Add( SubInner1, 1, wx.EXPAND, 5 )

		SubInner2 = wx.FlexGridSizer( 0, 2, 0, 52 )
		SubInner2.SetFlexibleDirection( wx.BOTH )
		SubInner2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.file_path_label = wx.StaticText( self, wx.ID_ANY, u"File Path:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.file_path_label.Wrap( -1 )
		SubInner2.Add( self.file_path_label, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.save_file_path = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,-1 ), 0 )
		SubInner2.Add( self.save_file_path, 0, wx.ALL, 5 )


		Inner1.Add( SubInner2, 1, wx.EXPAND, 5 )

		SubInner3 = wx.FlexGridSizer( 0, 3, 0, 0 )
		SubInner3.SetFlexibleDirection( wx.BOTH )
		SubInner3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		SubInner3.AddSpacer( ( 125, 0), 1, wx.EXPAND, 5 )

		self.save_btn = wx.Button( self, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
		SubInner3.Add( self.save_btn, 0, wx.ALL, 5 )

		self.cancel_btn = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		SubInner3.Add( self.cancel_btn, 0, wx.ALL, 5 )


		Inner1.Add( SubInner3, 1, wx.EXPAND, 5 )


		self.SetSizer( Inner1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.file_save_directory.Bind( wx.EVT_DIRPICKER_CHANGED, self.dir_selected )
		self.save_btn.Bind( wx.EVT_BUTTON, self.save_file )
		self.cancel_btn.Bind( wx.EVT_BUTTON, self.cancel_file_save )

	def __del__( self ):
		# Disconnect Events
		self.file_save_directory.Unbind( wx.EVT_DIRPICKER_CHANGED, None )
		self.save_btn.Unbind( wx.EVT_BUTTON, None )
		self.cancel_btn.Unbind( wx.EVT_BUTTON, None )


	# Virtual event handlers, overide them in your derived class
	def dir_selected( self, event ):
		dir_path=self.file_save_directory.GetPath()
		self.file_path=dir_path+'/'+self.file_name
		self.save_file_path.SetValue(self.file_path)

	def save_file( self, event ):
		if self.save_file_path.GetValue!='':
			url='http://'+ip+'/api/files/local/'+self.file_name
			response = requests.get(url, headers={'X-Api-Key':api_key})
			temp=response.json()
			url=temp['refs']['download']
			webFile = urllib2.urlopen(url)
			localFile = open(self.file_path, 'w')
			localFile.write(webFile.read())
			localFile.close()
			msg_dialog= wx.MessageDialog(None,'File Saved','Success', wx.OK | wx.ICON_INFORMATION)
			msg_dialog.ShowModal()
			webFile.close()
			self.Close()
		else:
			msg_dialog = wx.MessageDialog(None,'Invalid File Path','Error',wx.OK | wx.ICON_ERROR)
			msg_dialog.ShowModal()

	def cancel_file_save( self, event ):
		self.Close()

def start():
	ex = wx.App()
	f1=printer_settings_frame(None)
	f1.Show()
	ex.MainLoop()
