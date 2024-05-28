import requests
import json
import Drawing
from tkinter import Tk, Canvas, Frame, BOTH
import Settings

class Querrys:
    overpass_url = "http://overpass-api.de/api/interpreter"    
    proxy = {
        "http" : "http://proxy.cit.intern:3128",
        "https" : "http://proxy.cit.intern:3128"
    }
    """Querrys Api for all Nodes,Ways and Relations in given area Returns a Json"""
    def get_all_by_Aera(self,xcor1:float,ycor1:float,xcor2:float,ycor2:float) -> json:
            overpass_query = f"""
                [out:json];
                (node({xcor1},{ycor1},{xcor2},{ycor2});
                <;
                );
                out skel;"""
            response = requests.post(
            self.overpass_url,
            data=overpass_query,
            proxies=self.proxy,
            timeout=10
            )
            return  response.json()
    

if __name__=="__main__":
    client= Querrys()
    root = Tk()   
    frame= Drawing.Example()
    data =client.get_all_by_Aera(51.15,7.0,51.35,7.3)
    Settings.origin=  {
    "Latitude South" : 51.15,
    "Longitude West" : 7.0,
    "Latitude North" : 51.35,
    "Longitude East" : 7.3
    }
    root.geometry("800x800")
    frame.draw(data)
    root.mainloop()