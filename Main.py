import requests
import json

overpass_url = "http://overpass-api.de/api/interpreter"
overpass_query = """
    [out:json];
    (node( 51.332643 ,12.377827,51.33735,12.3683);
   <;
);
out skel;"""
    
proxy = {
    "http" : "http://proxy.cit.intern:3128",
    "https" : "https://proxy.cit.intern:3128"
}

response = requests.post(
    overpass_url,
    data=overpass_query,
    proxies=proxy,
    timeout=10
)

result = response.json()

out_file = open("testdaten1.json", "w")

json.dump(result, out_file,indent=2)

#print(response.text)
