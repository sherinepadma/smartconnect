# *SmartConnect GUI *

import wx
import json


class MyWindow(wx.Frame):
        def __init__(self, *args, **kw):
                super(MyWindow,self).__init__(*args, **kw)
                self.InitUI()
                self.Centre()

        def InitUI(self):
                self.panel = wx.Panel(self)
                self.SetBackgroundColour(wx.WHITE)
                self.SetTitle("Test GUI")
                self.SetSize(900,600)
                self.Bind(wx.EVT_PAINT, self.OnPaint)
                
        def OnPaint(self,event):
                dc = wx.PaintDC(self)
                dc.Clear()
                dc.SetPen(wx.Pen(wx.BLUE, 0.5))
                vertical_lines = [(i*5,0,i*5,600) for i in range(181)]
                horizontal_lines = [(0,i*5,900,i*5) for i in range(121)]
                dc.DrawLineList(horizontal_lines+vertical_lines)
##                dc.SetBrush(wx.Brush('#95bce7', wx.CROSS_HATCH))
##                dc.DrawRectangle(0, 0, 900, 600)
##                dc.DrawLineList((0,0,0,600),wx.BLUE)
##                dc.DrawLines(0,0,0,600,xoffset=20,yoffset=20)
                dc.SetPen(wx.Pen(wx.BLACK,3))
                with open("testjson.json", "r") as f:
                        T = json.load(f)
##                print('JSON-DICTIONARY:\n',T)

##                print('T dictionary:\n')
                for room,dim in T.items():
                    for par,dim1 in dim.items():
##                        print("T[room][par] : \n",T[room][par])
                ##        print("dim1:",dim1)
                        if par == "topright_pos_y":
                                xx=int(T[room]["topright_pos_x"])
                                yy=int(T[room]["topright_pos_y"])
                                ll=int(T[room]["length"])
                                bb=int(T[room]["breadth"])
##                                print("================================")
##                                print(xx,yy,ll,bb)
##                                dc.DrawRectangle (xx, yy, ll, bb)
                                dc.DrawLine(xx,yy,xx+ll,yy)
                                dc.DrawLine(xx,yy,xx,yy+bb)
                                dc.DrawLine(xx+ll,yy,xx+ll,yy+bb)
                                dc.DrawLine(xx,yy+bb,xx+ll,yy+bb)
##                                print("dc.DrawLine..............................")
                        dc.SetPen(wx.Pen(wx.BLACK,3))    
                        if par=="Nodes":
                            for i in range(len(T[room]["Nodes"])):
##                                print("Listing Nodes: ",i)  #T[room][par][0]
##                                print(T[room][par][i])
                                
                                for node_par,node_val in T[room][par][i].items():
##                                    print("node_par : \n",node_par,"node_val : \n",node_val)
                                    if T[room][par][i]["type"] == "s":
                                            dc.SetBrush(wx.Brush('#ed0111'))
                                            dc.SetPen(wx.Pen('#ed0111',3))
##                                            dc.SetPen(wx.Pen(wx.RED,3))
                                            dc.DrawCircle(int(T[room][par][i]["node_pos_x"]),int(T[room][par][i]["node_pos_y"]),4)
                                    if T[room][par][i]["type"] == "p":
                                            dc.SetBrush(wx.Brush('#000000'))
                                            dc.SetPen(wx.Pen('#000000',3)) 
##                                            dc.SetPen(wx.Pen(wx.BLACK,3))
                                            dc.DrawRectangle(int(T[room][par][i]["node_pos_x"]),int(T[room][par][i]["node_pos_y"]),8,8)
                                    if T[room][par][i]["type"] == "k":
                                            dc.SetBrush(wx.Brush('#fdd816'))
                                            dc.SetPen(wx.Pen('#fdd816',3)) 
##                                            dc.SetPen(wx.Pen(wx.YELLOW,3))
                                            dc.DrawPolygon([(int(T[room][par][i]["node_pos_x"])-4,int(T[room][par][i]["node_pos_y"])-4),
                                                           (int(T[room][par][i]["node_pos_x"])+4,int(T[room][par][i]["node_pos_y"])-4),
                                                           (int(T[room][par][i]["node_pos_x"])+4,int(T[room][par][i]["node_pos_y"])+4),
                                                           (int(T[room][par][i]["node_pos_x"])-4,int(T[room][par][i]["node_pos_y"])+4)])
                                    if T[room][par][i]["type"] == "r":
                                            dc.SetBrush(wx.Brush('#29fdf7'))
                                            dc.SetPen(wx.Pen('#29fdf7',3)) 
##                                            dc.SetPen(wx.Pen(wx.BLUE,3))
                                            dc.DrawPolygon([(int(T[room][par][i]["node_pos_x"]),int(T[room][par][i]["node_pos_y"])-7),
                                                           (int(T[room][par][i]["node_pos_x"])-7,int(T[room][par][i]["node_pos_y"])+7),
                                                           (int(T[room][par][i]["node_pos_x"])+7,int(T[room][par][i]["node_pos_y"])+7)])
##                                    dc.DrawPoint(int(T[room][par][i]['node_pos_x']),int(T[room][par][i]['node_pos_y']))
##                                    dc.SetBrush(wx.Brush('#ed0111'))
##                                    dc.DrawCircle(int(T[room][par][i]['node_pos_x']),int(T[room][par][i]['node_pos_y']),3)
                    if room == "Blank_Area":
##                            dc.SetBrush(wx.Brush(wx.TAN, wx.SOLID))
                            dc.SetBrush(wx.Brush('#95bce7'))
                            dc.DrawPolygon([(int(T[room]['x1']),int(T[room]['y1'])),
                                            (int(T[room]['x2']),int(T[room]['y2'])),
                                            (int(T[room]['x3']),int(T[room]['y3'])),
                                            (int(T[room]['x4']),int(T[room]['y4'])),
                                            (int(T[room]['x5']),int(T[room]['y5'])),
                                            (int(T[room]['x6']),int(T[room]['y6'])),
                                            (int(T[room]['x7']),int(T[room]['y7'])),
                                            (int(T[room]['x8']),int(T[room]['y8'])),
                                            (int(T[room]['x9']),int(T[room]['y9'])),
                                            (int(T[room]['x10']),int(T[room]['y10'])),
                                            (int(T[room]['x11']),int(T[room]['y11']))])
##                            


def main():
        app = wx.App()
        win = MyWindow(None)
        win.Show()
        app.MainLoop()
        
if __name__ == '__main__':
        main()


