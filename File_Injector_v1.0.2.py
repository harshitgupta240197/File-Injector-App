import wx
import shutil
import os

class FileInjector(wx.Frame):
    def __init__(self, parent, title):
        super(FileInjector, self).__init__(parent, title=title, size=(500, 300))

        self.InitUI()
        self.Centre()
        self.Show()

    def InitUI(self):
        panel = wx.Panel(self)

        vbox = wx.BoxSizer(wx.VERTICAL)

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        file_label = wx.StaticText(panel, label='Selected Files:')
        hbox1.Add(file_label, flag=wx.RIGHT, border=8)
        self.file_list = wx.ListBox(panel)
        hbox1.Add(self.file_list, proportion=1)
        vbox.Add(hbox1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        file_button = wx.Button(panel, label='Browse Files')
        hbox2.Add(file_button)
        vbox.Add(hbox2, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        folder_label = wx.StaticText(panel, label='Target Folders:')
        hbox3.Add(folder_label, flag=wx.RIGHT, border=8)
        self.folder_list = wx.ListBox(panel, style=wx.LB_MULTIPLE)
        hbox3.Add(self.folder_list, proportion=1)
        vbox.Add(hbox3, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        folder_button = wx.Button(panel, label='Browse Folders')
        hbox4.Add(folder_button)
        vbox.Add(hbox4, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

        hbox5 = wx.BoxSizer(wx.HORIZONTAL)
        inject_button = wx.Button(panel, label='Inject Files')
        hbox5.Add(inject_button)
        vbox.Add(hbox5, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

        hbox6 = wx.BoxSizer(wx.HORIZONTAL)
        self.status_label = wx.StaticText(panel, label='')
        hbox6.Add(self.status_label)
        vbox.Add(hbox6, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

        panel.SetSizer(vbox)

        file_button.Bind(wx.EVT_BUTTON, self.OnBrowseFiles)
        folder_button.Bind(wx.EVT_BUTTON, self.OnBrowseFolders)
        inject_button.Bind(wx.EVT_BUTTON, self.OnInjectFiles)

    def OnBrowseFiles(self, event):
        with wx.FileDialog(self, "Select file(s) to inject", wildcard="All files (*.*)|*.*", style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST | wx.FD_MULTIPLE) as fileDialog:
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return
            paths = fileDialog.GetPaths()
            for path in paths:
                self.file_list.Append(path)

    def OnBrowseFolders(self, event):
        with wx.DirDialog(self, "Select folder(s) to inject into", style=wx.DD_DEFAULT_STYLE | wx.DD_DIR_MUST_EXIST | wx.DD_MULTIPLE) as folderDialog:
            if folderDialog.ShowModal() == wx.ID_CANCEL:
                return
            paths = folderDialog.GetPaths(self)
            for path in paths:
                self.folder_list.Append(path)

    def OnInjectFiles(self, event):
        files_to_inject = self.file_list.GetStrings()
        target_folders = self.folder_list.GetStrings()

        for folder in target_folders:
            for file_path in files_to_inject:
                try:
                    shutil.copy(file_path, folder)
                    self.status_label.SetLabel("Files injected successfully!")
                    self.status_label.SetForegroundColour(wx.GREEN)
                except Exception as e:
                    self.status_label.SetLabel(f"Error: {e}")
                    self.status_label.SetForegroundColour(wx.RED)
                    return

if __name__ == '__main__':
    app = wx.App()
    FileInjector(None, title='File Injector')
    app.MainLoop()
