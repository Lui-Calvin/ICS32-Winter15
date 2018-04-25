#michaehm

import json
import urllib.parse
import urllib.request

MQ_KEY = "LLV4HIn3Egj8yYtCxWuAiYwq0LjQsGQf"
BASE_DIRECTIONS_URL= "http://open.mapquestapi.com/directions/v2/route?"

def build_URL_input(locations:list)-> str:
    "Creates route information URL link using desired locations"
    query_parameters = [('key', MQ_KEY), ('from', locations[0])]
    for location in locations[1:]:
        query_parameters.append(('to', location))
    URL = BASE_DIRECTIONS_URL + urllib.parse.urlencode(query_parameters)
    return URL


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


if __name__ == '__main__':
    print(build_URL_input(['Irvine, CA','Riverside, CA','Moreno Valley, CA']))
    L = ['Irvine, CA','Riverside, CA','Moreno Valley, CA']
    x = build_URL_input(L)
    y = get_result(x)
