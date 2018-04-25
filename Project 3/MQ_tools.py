#Calvin Lui 84152100
import json
import urllib.parse
import urllib.request

DEBUG_BOOL = False

MAPQUEST_KEY = "FFsi4hJpJoy9BusFVgflYljz1DEB4TOR"
BASE_MQ_DIRECTIONS_URL = "http://open.mapquestapi.com/directions/v2/route?"

def location_search_query(locations:list)->list:
    '''builds a search query for the target locations to route'''
    search_query = [('key',MAPQUEST_KEY),('from',locations[0])]
    for location in locations[1:]:
        search_query.append(('to',location))
    return search_query

def to_URL(Base_URL:str,search_query:list)->str:
    '''Takes two locations and creates a URL link for getting route information'''
    URL = Base_URL + urllib.parse.urlencode(search_query)
    
    if DEBUG_BOOL:
        print("~~~~~~~~~~~~~~URL created:~~~~~~~~~~~~~~\n" + URL + "\n\n")     
    return URL

def get_data_from_URL(URL:str)->dict:
    """takes a URL, gathers the JSON text, and then converts it into a readable format"""
    content = None
    try:
        content = urllib.request.urlopen(URL)
        return_info = json.loads(content.read().decode(encoding = 'utf-8'))
        if DEBUG_BOOL:
            print("~~~~~~~~~~~~~~Route information formatted:~~~~~~~~~~~~~~~~~~~")
            print(JSON_pretty_print(return_info)+ "\n\n")
        return return_info
    except:
        return content
    finally:
        if content != None:
            content.close()

def JSON_pretty_print(text:str)->str:
    """Converts Json text into a readable str"""
    return json.dumps(text,sort_keys = True,indent=2)


    
    
          
    
    
