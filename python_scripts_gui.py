import wx
import sys
import importlib
import scripts
import python_scripts_gui_wxUI
import winutils
import threading
from uuid import uuid4
#import all scripts from subfolder "scripts"
class ListDragDropTarget(wx.FileDropTarget):
    def __init__(self, object:wx.ListBox):
        wx.FileDropTarget.__init__(self)
        self.object = object

    def OnDropFiles(self, x, y, filenames):
        allitems=self.object.GetItems()+filenames
        uniques=list(set(allitems))
        self.object.Clear()
        self.object.InsertItems(uniques,0)

        return True

class MainWindow(python_scripts_gui_wxUI.MyFrame1):
    def __init__(self):
        super().__init__(None)
        self.Centre()
        self.SetSize(600,500)
        self.currentTool=None
        self.ShowTool1(None)

    def ShowTool1(self,event):
        #skip if tool is already shown
        if type(self.currentTool)==ExtractTools:
            return

        #put the panel for the tool1 in the boxsizer
        self.removeToolFromSizer()
        newpanel=ExtractTools(self,style=wx.ALL|wx.EXPAND)

        #initialize DragAndDropTarget
        dt = ListDragDropTarget(newpanel.m_listBox1)




        newpanel.m_listBox1.SetDropTarget(dt)

        self.currentTool=newpanel
        self.GetSizer().Add(newpanel,1,wx.EXPAND)
        self.Layout()

    def removeToolFromSizer(self):
        if self.currentTool is not None:
            self.GetSizer().Detach(self.currentTool)
            self.currentTool.Destroy()



class ExtractTools(python_scripts_gui_wxUI.Panel_extractTools):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.runningProcesses=[]

    def ClearList(self, event):
        self.m_listBox1.Clear()

    def ClearSelection(self, event):
        #delete selected items from the listbox
        for item in reversed( self.m_listBox1.GetSelections()):
            self.m_listBox1.Delete(item)

    def Extract(self,event):
        guid=uuid4()
        if self.m_radioBox1.Selection==0:
            scripts.extract_in_same_dir.extract(guid,self.m_listBox1.GetItems(),self.callbackhandler)
        else:
            scripts.extract_in_subfolder.extract(guid,self.m_listBox1.GetItems(),self.callbackhandler)

    def callbackhandler(self,msg:dict):
        if msg["status"]=="init":
            self.runningProcesses.append(msg["id"])
        if msg["status"]=="finished":
            self.runningProcesses.remove(msg["id"])

        if msg["status"]=="progress":
            self.updateProgress(msg["id"],msg["progress"],msg["total"])
        #     self.runningProcesses[msg["id"]].
        # id=msg["id"]
        # status=msg["status"]
        # progress=msg["progress"]
        # msg["total"]

    def updateProgress(self,id,progress:int,total:int):
        print(f"ProgressUpdate {id} - {progress}/{total}")


def main(args):
    app = wx.App()
    frame = MainWindow();
    frame.Show()
    app.MainLoop()

if __name__ == '__main__':
    main(sys.argv[1:])
