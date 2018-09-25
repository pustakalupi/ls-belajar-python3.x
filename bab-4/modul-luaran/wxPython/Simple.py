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
        #1. inisialisasi parent
        wx.Frame.__init__( self, parent, -1, title, pos=(150, 150), size=(350, 200))

        #2. set ukuran window minimum jadi lebar=-1, dan tinggi=-1
        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        
        #3. membuat box sizer vertikal, itulah mengapa tombol disusun vertikal
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        
        #4. buat button ok dan set lebar minimum 1000 agar stretch ke parent window
        self.m_button1 = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
        self.m_button1.SetMinSize( wx.Size( 1000,-1 ) )
        
        #5 tambahkan button ok ke box sizer
        bSizer1.Add( self.m_button1, 0, wx.ALL, 5 )
        
        #6 sama dengan #4, tapi labelnya "Cancel"
        self.m_button2 = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_button2.SetMinSize( wx.Size( 1000,-1 ) )
        
        #7. tambahkan button Cancel ke box sizer
        bSizer1.Add( self.m_button2, 0, wx.ALL, 5 )
        
        #8. gunakan box sizer tadi
        self.SetSizer( bSizer1 )

        #9. ini tidak wajib
        self.Layout()
        
        #10. munculkan window di tengah layar
        self.Centre( wx.BOTH )

class MyApp(wx.App):
    def OnInit(self):
        #11. buat MyFrame
        frame = MyFrame(None, "wxPython Sederhana!")
        self.SetTopWindow(frame)
        frame.Show(True)
        return True

#12. buat app-nya dan jalankan GUI loop
app = MyApp(redirect=True)
app.MainLoop()