# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer_mainContent = wx.BoxSizer( wx.VERTICAL )


		self.SetSizer( bSizer_mainContent )
		self.Layout()
		self.m_statusBar1 = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )
		self.m_toolBar1 = self.CreateToolBar( wx.TB_VERTICAL, wx.ID_ANY )
		self.m_tool_extract = self.m_toolBar1.AddTool( wx.ID_ANY, u"tool", wx.ArtProvider.GetBitmap( wx.ART_NEW_DIR, wx.ART_TOOLBAR ), wx.NullBitmap, wx.ITEM_NORMAL, u"ExtractionTools", u"ExtractionTools", None )

		self.m_toolBar1.Realize()


		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_TOOL, self.ShowTool1, id = self.m_tool_extract.GetId() )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def ShowTool1( self, event ):
		event.Skip()


###########################################################################
## Class Panel_extractTools
###########################################################################

class Panel_extractTools ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		m_listBox1Choices = []
		self.m_listBox1 = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox1Choices, wx.LB_MULTIPLE )
		self.m_menu1 = wx.Menu()
		self.m_menuItem_clearList = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Clear List", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuItem_clearList.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_DELETE, wx.ART_MENU ) )
		self.m_menu1.Append( self.m_menuItem_clearList )

		self.m_menuItem_clearSelected = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Remove Selection", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.m_menuItem_clearSelected )

		self.m_listBox1.Bind( wx.EVT_RIGHT_DOWN, self.m_listBox1OnContextMenu )

		bSizer2.Add( self.m_listBox1, 1, wx.ALL|wx.EXPAND, 5 )

		m_radioBox1Choices = [ u"Extract in Same Folders", u"Extract in Subfolders" ]
		self.m_radioBox1 = wx.RadioBox( self, wx.ID_ANY, u"Options", wx.DefaultPosition, wx.DefaultSize, m_radioBox1Choices, 1, wx.RA_SPECIFY_COLS )
		self.m_radioBox1.SetSelection( 0 )
		bSizer2.Add( self.m_radioBox1, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button4 = wx.Button( self, wx.ID_ANY, u"Extract", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_button4, 0, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer2 )
		self.Layout()

		# Connect Events
		self.Bind( wx.EVT_MENU, self.ClearList, id = self.m_menuItem_clearList.GetId() )
		self.Bind( wx.EVT_MENU, self.ClearSelection, id = self.m_menuItem_clearSelected.GetId() )
		self.m_button4.Bind( wx.EVT_BUTTON, self.Extract )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def ClearList( self, event ):
		event.Skip()

	def ClearSelection( self, event ):
		event.Skip()

	def Extract( self, event ):
		event.Skip()

	def m_listBox1OnContextMenu( self, event ):
		self.m_listBox1.PopupMenu( self.m_menu1, event.GetPosition() )


###########################################################################
## Class MyDialog1
###########################################################################

class MyDialog1 ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )


		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


