'''
install wxPython lebih dahulu:
pip3 install -U -f https://extras.wxpython.org/wxPython4/extras/linux/gtk3/ubuntu-18.04 wxPython

install pyinstaller:
pip3 install pyinstaller
'''

'''
done
'''
import wx

class MyFrame(wx.Frame):
    def __init__( self, parent, title ):
        wx.Frame.__init__( self, parent, -1, title, pos=(150, 150), size=(350, 200))
        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_button1 = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
        self.m_button1.SetMinSize( wx.Size( 1000,-1 ) )
        
        bSizer1.Add( self.m_button1, 0, wx.ALL, 5 )
        
        self.m_button2 = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_button2.SetMinSize( wx.Size( 1000,-1 ) )
        
        bSizer1.Add( self.m_button2, 0, wx.ALL, 5 )
        
        self.SetSizer( bSizer1 )
        self.Layout()
        
        self.Centre( wx.BOTH )

class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(None, "wxPython App yang Standalone!")
        self.SetTopWindow(frame)
        frame.Show(True)
        return True

app = MyApp(redirect=True)
app.MainLoop()