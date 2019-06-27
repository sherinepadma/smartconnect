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
                self.SetTitle("Test GUI")
                self.SetSize(900,600)
                self.Bind(wx.EVT_PAINT, self.OnPaint)
                
        def OnPaint(self,event=None):
                dc = wx.PaintDC(self)
                dc.Clear()
                dc.SetPen(wx.Pen(wx.BLACK, 4))
                with open("testjson.json", "r") as f:
                        T = json.load(f)
                print('JSON-DICTIONARY:\n',T)

                print('T dictionary:\n')
                for room,dim in T.items():
                    for par,dim1 in dim.items():
                        print("T[room][par] : \n",T[room][par])
                ##        print("dim1:",dim1)
                        if par == "topright_pos_y":
                                xx=int(T[room]["topright_pos_x"])
                                yy=int(T[room]["topright_pos_y"])
                                ll=int(T[room]["length"])
                                bb=int(T[room]["breadth"])
                                print("================================")
                                print(xx,yy,ll,bb)
##                                dc.DrawRectangle (xx, yy, ll, bb)
                                dc.DrawLine(xx,yy,xx+ll,yy)
                                dc.DrawLine(xx,yy,xx,yy+bb)
                                dc.DrawLine(xx+ll,yy,xx+ll,yy+bb)
                                dc.DrawLine(xx,yy+bb,xx+ll,yy+bb)
                                print("dc.DrawLine..............................")
                                
                        if par=="Nodes":
                            for i in range(len(T[room]["Nodes"])):
                                print("Listing Nodes: ",i)  #T[room][par][0]
                                print(T[room][par][i])
                                for node_par,node_val in T[room][par][i].items():
                                    print("node_par : \n",node_par,"node_val : \n",node_val)
                                    dc.DrawPoint(int(T[room][par][i]['node_pos_x']),int(T[room][par][i]['node_pos_y']))
##                dc.DrawLine(10,10,250,10)--
##                dc.DrawLine(10,10,10,590)--
##                dc.DrawLine(10,590,500,590)--
##                dc.DrawLine(560,590,890,590)--
##                dc.DrawLine(10,130,160,130)
##                dc.DrawLine(10,180,160,180)
##                dc.DrawLine(160,130,160,240)
##                dc.DrawLine(10,240,250,240)
##                dc.DrawLine(10,380,210,380)
##                dc.DrawLine(210,240,210,475)
##                dc.DrawLine(10,475,500,475)
##                dc.DrawLine(500,475,500,590)
##                dc.DrawLine(250,475,250,590)
##                dc.DrawLine(375,475,375,590)
##                dc.DrawLine(560,475,890,475)
##                dc.DrawLine(560,475,560,590)
##                dc.DrawLine(600,300,600,400)
##                dc.DrawLine(600,400,700,400)
##                dc.DrawLine(890,475,890,590)
##                dc.DrawLine(250,10,250,400)
##                dc.DrawLine(250,400,545,400)
##                dc.DrawLine(545,400,545,250)
##                dc.DrawLine(545,250,600,250)
##                dc.DrawLine(600,250,600,300)
##                dc.DrawLine(600,300,700,300)
##                dc.DrawLine(700,300,700,400)
##                dc.DrawLine(700,400,890,400)
##                dc.DrawLine(890,400,890,10)
##                dc.DrawLine(890,10,250,10)

def main():
        app = wx.App()
        win = MyWindow(None)
        win.Show()
        app.MainLoop()
        
if __name__ == '__main__':
        main()


