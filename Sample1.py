#-*- coding: utf-8 -*-

import wx
import urllib2,sys
import json

APP_EXIT = 1
TEXT = 2
TEXT_T = 3
TEXT_C = 4
VAULE = ""

BOOK_title =""
B00K_summary=""
BOOK_publisher=""
BOOK_pubdate=""
BOOK_author=""
BOOK_price=""
BOOK_author_intro=""
BOOK_binding=""
BOOK_translator=""
BOOK_pages=""

BOOK_tags=""
author =""
translator =""
hd = {}
class Example(wx.Frame):

    def __init__(self,parent,title):
        super(Example,self).__init__(parent,title=title,size=(500,400))
        
        self.InitUI()

    def InitUI(self):
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        qmi = wx.MenuItem(fileMenu,APP_EXIT,'&Quit\tCtrl+Q')
        fileMenu.AppendItem(qmi)
        self.Bind(wx.EVT_MENU,self.OnQuit,id=APP_EXIT)
        menubar.Append(fileMenu,'&File')
        self.SetMenuBar(menubar)

        panel = wx.Panel(self)
        font = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)
        font.SetPointSize(9)

        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        st1 = wx.StaticText(panel, label='Book ID')
        st1.SetFont(font)
        hbox1.Add(st1, flag=wx.RIGHT, border=8)
        tc = wx.TextCtrl(panel,TEXT)
        
        hbox1.Add(tc, proportion=1)
        button = wx.Button(panel, label='Search',size=(80,20))

        button.Bind(wx.EVT_BUTTON,self.OnSearch)
        hbox1.Add(button,flag=wx.RIGHT,border=8)

        vbox.Add(hbox1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

        vbox.Add((-1, 10))
        
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        st2 = wx.StaticText(panel, label='Book Information')
        st2.SetFont(font)
        hbox2.Add(st2)
        vbox.Add(hbox2, flag=wx.LEFT | wx.TOP, border=10)

        vbox.Add((-1, 10))

        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        tc2 = wx.TextCtrl(panel, style=wx.TE_MULTILINE,id=TEXT_C)
        hbox3.Add(tc2, proportion=1, flag=wx.EXPAND)
        vbox.Add(hbox3, proportion=1, flag=wx.LEFT|wx.RIGHT|wx.EXPAND, 
            border=10)

        vbox.Add((-1, 25))

        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        st3 = wx.StaticText(panel, label='Book Summary')
        st3.SetFont(font)
        hbox4.Add(st3)
        vbox.Add(hbox4, flag=wx.LEFT | wx.TOP, border=10)

        vbox.Add((-1, 25))

        hbox5 = wx.BoxSizer(wx.HORIZONTAL)
        tc3 = wx.TextCtrl(panel, style=wx.TE_MULTILINE,id=TEXT_T)
        hbox5.Add(tc3, proportion=1, flag=wx.EXPAND)
        vbox.Add(hbox5, proportion=1, flag=wx.LEFT|wx.RIGHT|wx.EXPAND, 
            border=10)

        panel.SetSizer(vbox)
        
        self.Centre()
        self.Show(True)
        
    def OnQuit(self,e):
        self.Close()
    def OnSearch(self,e):
        VALUE = self.FindWindowById(TEXT).GetValue()
        req=urllib2.Request("https://api.douban.com/v2/book/"+VALUE)
        fd= urllib2.urlopen(req)
        while True:
              data=fd.read(1024*5)
              if not len(data): break
              hd=json.loads(data.decode('utf-8'))
        BOOK_title=hd['title']
        BOOK_author=hd['author']
        BOOK_translator=hd['translator']
        #for i in BOOK_translator:
        #    translator =i
        BOOK_publisher=hd['publisher']
        BOOK_pubdate=hd['pubdate']
        BOOK_price=hd['price']
        BOOK_pages=hd['pages']
        BOOK_author_intro=hd['author_intro']
        BOOK_binding=hd['binding']
        BOOK_summary=hd['summary']
        self.FindWindowById(TEXT_T).SetValue(BOOK_summary)
        self.FindWindowById(TEXT_C).SetValue("title: "+BOOK_title+"\nauthor: "+"".join(BOOK_author)+"\ntranslator: "+"".join(BOOK_translator)+
                                             "\npublisher: "+BOOK_publisher+"\npubdate:"+BOOK_pubdate+"\nprice: "+BOOK_price+"\npages: "+BOOK_pages+
                                             "\nbinding: "+BOOK_binding+"\nAuthor Information:\n"+BOOK_author_intro)
        
        
if __name__=='__main__':
    app = wx.App()
    Example(None,title='DouBan Book info')
    app.MainLoop()

