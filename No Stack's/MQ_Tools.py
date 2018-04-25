#michaehm

import json
import urllib.parse
import urllib.request

MQ_KEY = "LLV4HIn3Egj8yYtCxWuAiYwq0LjQsGQf"
BASE_DIRECTIONS_URL= "http://open.mapquestapi.com/directions/v2/route?"
BASE_ELEVATION_URL = 'http://open.mapquestapi.com/elevation/v1/profile?'

def build_URL_input(Base_URL:str,query:list)-> str:
    "Creates URL by taking in a Base URL and a Search Query."
    return Base_URL + urllib.parse.urlencode(query)

def Location_URL(Locations:list)->str:
    "takes a list of locations and builds a URL to get route information"
    search_query = [('key', MQ_KEY), ('from', Locations[0])]
    for location in Locations[1:]:
        search_query.append(('to', location))
    return build_URL_input(BASE_DIRECTIONS_URL,search_query)

def Elevation_URL(lat:float,lng:float)->str:
    '''takes a latitude and longitude and creates a URL to get Elevation information'''
    search_query = [('key',MQ_KEY),('shapeFormat','raw'),('latLngCollection',str(lat) + "," + str(lng))]
    return build_URL_input(BASE_ELEVATION_URL,search_query)
    
def get_result(URL: str) -> 'json':
    '''
    This function takes a URL and returns a Python object representing the
    parsed JSON response.
    '''
    response = None

    try:
        response = urllib.request.urlopen(URL)
        json_text = response.read().decode(encoding = 'utf-8')
        return json.loads(json_text)

    finally:
        if response != None:
            response.close()
        else:
            return response


if __name__ == '__main__':
    print(build_URL_input(['Irvine, CA','Riverside, CA','Moreno Valley, CA']))
    L = ['Irvine, CA','Riverside, CA','Moreno Valley, CA']
    x = build_URL_input(L)
    y = get_result(x)
