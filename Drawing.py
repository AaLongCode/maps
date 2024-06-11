from tkinter import *
from tkinter import messagebox
import json 
import Settings
import Querrys


def hash_nodes(data) -> dict:
    out = dict()
    for i in data['elements']:
        if i['type']=='node':
            #print(i)
            out[str(i['id'])+'lon']=i['lon']
            out[str(i['id'])+'lat']=i['lat']
    return out



class Example(Frame):
    cnavas=None
    def __init__(self):
        super().__init__()
        self.canvas = Canvas(self)
        self.pack(fill=BOTH, expand=1)
        self.canvas.pack(fill=BOTH, expand=1)
        

    def draw(self,data:json):
        self.canvas.delete("all")
        nodes=hash_nodes(data)
        
        conversion_longitude = Settings.WindowWidth/(Settings.zoomlevel*Settings.zoomstep_longitude)
        conversion_latitude = Settings.WindowHeigt/(Settings.zoomlevel*Settings.zoomstep_latitude)
        lastPointLon = None
        lastPointLat = None
        for i in data['elements']:
            # if i['type']=='node':
            #     print(i)
            #     xcor= round((-origin["Longitude West"] + i['lon'])*conversion_longitude)
            #     ycor= round((origin["Latitude North"] - i['lat'])*conversion_latitude)
            #     print(str(xcor)+' '+str(ycor))
            #     canvas.create_oval(xcor-1,ycor-1,xcor+1,ycor+1)
            if i['type']=='way':
                #print(i)
                for j in i['nodes']:
                    if lastPointLon!=None and lastPointLat!=None:
                        xcor= round((-Settings.origin["Longitude West"] + lastPointLon)*conversion_longitude)
                        ycor= round((Settings.origin["Latitude North"] - lastPointLat)*conversion_latitude)
                        newPointLon = None if nodes.get(str(j)+'lon') is None else float(nodes[str(j)+'lon'])
                        newPointLat = None if nodes.get(str(j)+'lat') is None else float(nodes[str(j)+'lat'])
                        #print(str(newPointLat)+' '+str(newPointLon))
                        if newPointLon!=None and newPointLat!=None:
                            xcor1= round((-Settings.origin["Longitude West"] + newPointLon)*conversion_longitude)
                            ycor1= round((Settings.origin["Latitude North"] - newPointLat)*conversion_latitude)
                            self.canvas.create_line(xcor,ycor,xcor1,ycor1)
                        lastPointLon = newPointLon
                        lastPointLat = newPointLat
                    else:
                        lastPointLon = None if nodes.get(str(j)+'lon') is None else float(nodes[str(j)+'lon'])
                        lastPointLat = None if nodes.get(str(j)+'lat') is None else float(nodes[str(j)+'lat'])
                    # for k in data['elements']:
                    #     if k['id']==j:
                    #         if lastPoint!=None:
                    #             xcor= round((-origin["Longitude West"] + lastPoint['lon'])*conversion_longitude)
                    #             ycor= round((origin["Latitude North"] - lastPoint['lat'])*conversion_latitude)
                    #             xcor1= round((-origin["Longitude West"] + k['lon'])*conversion_longitude)
                    #             ycor1= round((origin["Latitude North"] - k['lat'])*conversion_latitude)
                    #             canvas.create_line(xcor,ycor,xcor1,ycor1)
                    #             lastPoint=k
                    #         else:
                    #             lastPoint=k
            lastPointLon = None
            lastPointLat = None




        self.master.title("Map")
        



def main():
    client = Querrys.Querrys()
    data = client.get_all_by_Aera(Settings.origin['Latitude North']-(Settings.zoomlevel*Settings.zoomstep_latitude),Settings.origin['Longitude West'],Settings.origin['Latitude North'], Settings.origin['Longitude West']+(Settings.zoomlevel*Settings.zoomstep_longitude))
    root = Tk()
    ex = Example()
    ex.draw(data)
    def zoom_out():
        if (Settings.zoomlevel <5):
            Settings.zoomlevel += 1
            data = client.get_all_by_Aera(Settings.origin['Latitude North']-(Settings.zoomlevel*Settings.zoomstep_latitude),
                                          Settings.origin['Longitude West'],
                                          Settings.origin['Latitude North'], 
                                          Settings.origin['Longitude West']+(Settings.zoomlevel*Settings.zoomstep_longitude))
            ex.draw(data)
        else:
            messagebox.showwarning("Warnung", "Minimales Zoom-Level erreicht")
    def zoom_in():
        if (Settings.zoomlevel > 1):
            Settings.zoomlevel -=1
            data = client.get_all_by_Aera(Settings.origin['Latitude North']-(Settings.zoomlevel*Settings.zoomstep_latitude),
                                          Settings.origin['Longitude West'],
                                          Settings.origin['Latitude North'], 
                                          Settings.origin['Longitude West']+(Settings.zoomlevel*Settings.zoomstep_longitude))
            ex.draw(data)
        else:
            messagebox.showwarning("Warnung","Maximales Zoom-Level erreicht")

    def scroll_North():
        Settings.origin['Latitude North']+=(0.5*Settings.zoomstep_latitude*Settings.zoomlevel)
        data = client.get_all_by_Aera(Settings.origin['Latitude North']-(Settings.zoomlevel*Settings.zoomstep_latitude),
                                          Settings.origin['Longitude West'],
                                          Settings.origin['Latitude North'], 
                                          Settings.origin['Longitude West']+(Settings.zoomlevel*Settings.zoomstep_longitude))
        ex.draw(data)
    
    def scroll_South():
        Settings.origin['Latitude North']-=(0.5*Settings.zoomstep_latitude*Settings.zoomlevel)
        data = client.get_all_by_Aera(Settings.origin['Latitude North']-(Settings.zoomlevel*Settings.zoomstep_latitude),
                                          Settings.origin['Longitude West'],
                                          Settings.origin['Latitude North'], 
                                          Settings.origin['Longitude West']+(Settings.zoomlevel*Settings.zoomstep_longitude))
        ex.draw(data)
    def scroll_East():
        Settings.origin['Longitude West']+=(0.5*Settings.zoomstep_latitude*Settings.zoomlevel)
        data = client.get_all_by_Aera(Settings.origin['Latitude North']-(Settings.zoomlevel*Settings.zoomstep_latitude),
                                          Settings.origin['Longitude West'],
                                          Settings.origin['Latitude North'], 
                                          Settings.origin['Longitude West']+(Settings.zoomlevel*Settings.zoomstep_longitude))
        ex.draw(data)
    def scroll_West():
        Settings.origin['Longitude West']-=(0.5*Settings.zoomstep_latitude*Settings.zoomlevel)
        data = client.get_all_by_Aera(Settings.origin['Latitude North']-(Settings.zoomlevel*Settings.zoomstep_latitude),
                                          Settings.origin['Longitude West'],
                                          Settings.origin['Latitude North'], 
                                          Settings.origin['Longitude West']+(Settings.zoomlevel*Settings.zoomstep_longitude))
        ex.draw(data)
        
    root.geometry(f"{Settings.WindowWidth}x{Settings.WindowHeigt}")
    b_zoom_out = Button(root,text='-',command= zoom_out)
    b_zoom_in = Button(root,text='+',command= zoom_in) 
    b_zoom_out.place(x=50,y=50)
    b_zoom_in.place(x=50,y=100)
    b_scroll_north = Button(root,text='\u2191',command= scroll_North)
    b_scroll_south = Button(root,text='\u2193',command= scroll_South)
    b_scroll_east = Button(root,text='\u2192',command= scroll_East)
    b_scroll_west = Button(root,text='\u2190',command= scroll_West)
    b_scroll_north.place(x= 50,y= 150)
    b_scroll_south.place(x=50,y=200)
    b_scroll_east.place(x=75,y=175)
    b_scroll_west.place(x=25,y=175)
    root.mainloop()


if __name__ == '__main__':
    main()