import wx
import database_handler

class RecipePanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.recipes = {}

        self.list_ctrl = wx.ListCtrl(
            self, size = (-1, 100),
            style = wx.LC_REPORT | wx.BORDER_SUNKEN
        )
        self.list_ctrl.InsertColumn(0, 'Reteta', width = 200)
        self.list_ctrl.InsertColumn(1, 'Ingredient', width = 200)

        self.sizer.Add(self.list_ctrl, 0, wx.ALL | wx.EXPAND, 5)

        self.SetSizer(self.sizer)


class GUI(wx.Frame):    
    def __init__(self):
        super().__init__(parent=None, title='Ce Mananc')
        panel = RecipePanel(self)

        # my_sizer = wx.BoxSizer(wx.VERTICAL)  
        # self.text_retete = wx.TextCtrl(panel)
        # self.text_retete.Hint = "Locatie Retete"

        # self.text_db = wx.TextCtrl(panel)
        # self.text_db.Hint = "Locatie Retete Mancate"

        # my_btn = wx.Button(panel, label='Enter')
        # my_btn.Bind(wx.EVT_BUTTON, self.on_press)


        # my_sizer.Add(self.text_retete, 0, wx.ALL | wx.EXPAND, 5)
        # my_sizer.Add(self.text_db, 0, wx.ALL | wx.EXPAND, 5)
        # my_sizer.Add(my_btn, 0, wx.ALL | wx.CENTER, 5)

        # panel.SetSizer(my_sizer)

        self.Show()
    
    def on_press(self, event):
        locatie_retete = self.text_retete.GetValue()
        locatie_db = self.text_db.GetValue()
        if not locatie_retete or not locatie_db:
            print("Te rog scrie")
        else:
            print(f'Retete: "{locatie_retete}"')
            print(f'DB: "{locatie_db}"')
            self.text_retete.SetValue("")
            self.text_db.SetValue("")   

