# *SmartConnect GUI *

import wx
import json
from tkinter import *

class MyWindow(wx.Frame):
        def __init__(self, *args, **kw):
                super(MyWindow,self).__init__(*args, **kw)
                self.InitUI()
                self.Centre()

        def InitUI(self):
                self.panel = wx.Panel(self)
                self.SetTitle("Test GUI")
                self.SetSize(900,600)
                self.panel.SetBackgroundColour('white')
                with open('testjson.json', 'r') as f:
                        test_dict = json.load(f)
                print(test_dict)
                print('***************************************************')
                if 'Room A' in test_dict:
                        if 'length' in test_dict['Room A']:
                                print(test_dict['Room A']['length'])
                                print(test_dict['Room A']['Nodes'])
                print('***************************************************')
##                self.Bind(wx.EVT_PAINT, self.drawcanvas)
                self.drawcanvas()

        def drawcanvas(self):
                python_green = "#476042"
                master = Tk()
                w = Canvas(width = 900,height = 600)
                w.pack()
                points = [250,10,250,400,545,400,545,250,600,250,600,300,700,300,700,400,890,400,890,10]
                w.create_polygon(points,outline=python_green,fill='sky blue')

                points = [10,10,250,10]
                w.create_line(points)
                points=[10,10,10,590]
                w.create_line(points)
                points=[10,590,500,590]
                w.create_line(points)
                points=[560,590,890,590]
                w.create_line(points)
                points=[10,130,160,130]
                w.create_line(points)
                points=[10,180,160,180]
                w.create_line(points)
                points=[160,130,160,240]
                w.create_line(points)
                points=[10,240,250,240]
                w.create_line(points)
                points=[10,380,210,380]
                w.create_line(points)
                points=[210,240,210,475]
                w.create_line(points)
                points=[10,475,500,475]
                w.create_line(points)
                points=[500,475,500,590]
                w.create_line(points)
                points=[250,475,250,590]
                w.create_line(points)
                points=[375,475,375,590]
                w.create_line(points)
                points=[560,475,890,475]
                w.create_line(points)
                points=[560,475,560,590]
                w.create_line(points)
                points=[600,300,600,400]
                w.create_line(points)
                points=[600,400,700,400]
                w.create_line(points)
                points=[890,475,890,590]
                w.create_line(points)

def main():
        app = wx.App()
        win = MyWindow(None)
        win.Show()
        app.MainLoop()
        
if __name__ == '__main__':
        main()

