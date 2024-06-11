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
    def get_all_by_Aera(self,latitude_south:float,longitude_west:float,latitude_norht:float,longitude_east:float) -> json:
            overpass_query = f"""
                [out:json];
                (node({latitude_south},{longitude_west},{latitude_norht},{longitude_east});
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
    def get_all_motorway_Germany(self) -> json:
         overpass_query = f"""
            [out:json];
            area[name="Deutschland"]->.searchArea;
            (
            way["highway"="motorway"](area.searchArea)->.searchArea;
            way["boundary"="administrative"]["admin_level"= "4"](area.searchArea)->.searchArea;
            .searchArea>;
            );
            out skel;
         """
         response = requests.post(
            self.overpass_url,
            data=overpass_query,
            proxies=self.proxy,
            timeout=500
            )
         return response.json()
    def get_all_nodes(self) -> json:
        overpass_query = f"""
        [out:json];
        area[name="Bremen"]->.searchArea;
        (
        node(area.searchArea)->.searchArea;
        );
        out skel;
        """
        response = requests.post(
            self.overpass_url,
            data=overpass_query,
            proxies=self.proxy,
            timeout=500
            )
        return response.json() 
    

if __name__=="__main__":
    client= Querrys()
    #root = Tk()   
    frame= Drawing.Example()
    data =client.get_all_nodes()
    Settings.origin=  {
    "Latitude South" : 47.270111,
    "Longitude West" : 5.866342,
    "Latitude North" : 55.058347,
    "Longitude East" : 15.041896
    }
    print(json.dumps(data,indent=2))
    #root.geometry("800x800")
    #frame.draw(data)
    #root.mainloop()