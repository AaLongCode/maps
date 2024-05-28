from tkinter import Tk, Canvas, Frame, BOTH
import json 
import hashtable
import Settings

def hash_nodes(data) -> hashtable.HashTable:
    out =hashtable.HashTable(1000)
    for i in data['elements']:
        if i['type']=='node':
            print(i)
            out.set_val(str(i['id'])+'lon', i['lon'])
            out.set_val(str(i['id'])+'lat', i['lat'])
    return out



class Example(Frame):
    def __init__(self):
        super().__init__()

    def draw(self,data:json):
        nodes=hash_nodes(data)
        canvas = Canvas(self)
        conversion_longitude = 800/(Settings.origin["Longitude East"]-Settings.origin["Longitude West"])
        conversion_latitude = 800/(Settings.origin["Latitude North"]-Settings.origin["Latitude South"])
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
                print(i)
                for j in i['nodes']:
                    if lastPointLon!=None and lastPointLat!=None:
                        xcor= round((-Settings.origin["Longitude West"] + lastPointLon)*conversion_longitude)
                        ycor= round((Settings.origin["Latitude North"] - lastPointLat)*conversion_latitude)
                        newPointLon = None if nodes.get_val(str(j)+'lon') is None else float(nodes.get_val(str(j)+'lon'))
                        newPointLat = None if nodes.get_val(str(j)+'lat') is None else float(nodes.get_val(str(j)+'lat'))
                        #print(str(newPointLat)+' '+str(newPointLon))
                        if newPointLon!=None and newPointLat!=None:
                            xcor1= round((-Settings.origin["Longitude West"] + newPointLon)*conversion_longitude)
                            ycor1= round((Settings.origin["Latitude North"] - newPointLat)*conversion_latitude)
                            canvas.create_line(xcor,ycor,xcor1,ycor1)
                        lastPointLon = newPointLon
                        lastPointLat = newPointLat
                    else:
                        lastPointLon = None if nodes.get_val(str(j)+'lon') is None else float(nodes.get_val(str(j)+'lon'))
                        lastPointLat = None if nodes.get_val(str(j)+'lat') is None else float(nodes.get_val(str(j)+'lat'))
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
        self.pack(fill=BOTH, expand=1)

        canvas.pack(fill=BOTH, expand=1)


def main():
    f = open('testdaten_leipzig_skeleton.json')
    data = json.load(f)
    root = Tk()
    ex = Example()
    ex.draw(data,)
    root.geometry("800x800")
    root.mainloop()


if __name__ == '__main__':
    main()