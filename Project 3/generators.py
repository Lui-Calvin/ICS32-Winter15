import MQ_tools

BASE_MQ_ELEVATION_URL = 'http://open.mapquestapi.com/elevation/v1/profile?'

class STEPS:
    def print_data(self,Json_text:dict)->None:
        '''prints the directions for every step of the trip'''
        print("DIRECTIONS:")
        for legs in Json_text['route']['legs']:
            for direction in legs['maneuvers']:
                print(direction['narrative'])
        print()

class TOTALDISTANCE:
    def print_data(self,Json_text:dict)->None:
        '''print the total distance of the trip'''
        print("TOTAL DISTANCE: {} miles".format(round(int(Json_text['route']['distance'])))+ "\n")

class TOTALTIME:
    def print_data(self,Json_text:dict)->None:
        '''prints the total time of the trip'''
        print('TOTAL TIME: {} minutes'.format(round(int(Json_text['route']['time'])/60))+ '\n')
        
class LATLONG:
    def print_data(self,Json_text:dict)->None:
        '''prints the Latitudes and longitudes of the locations'''
        print('LATLONGS:')
        for location in Json_text['route']['locations']:
            lat = float(location['displayLatLng']['lat'])
            lng = float(location['displayLatLng']['lng'])
            lat_direction = 'N'
            lng_direction = 'E'
            if lat < 0:
                lat_direction = 'S'
                lat *= -1
            if lng < 0:
                lng_direction = 'W'
                lng *= -1
            print("{:.2f}{} {:.2f}{}".format(lat,lat_direction,lng,lng_direction))
        print()

class ELEVATION:
    def print_data(self,Json_text:dict):
        '''gets longitude and latitude information from the Json text and gets the elevation information off of mapquest'''
        print('ELEVATIONS:')
        for location in Json_text['route']['locations']:
            lat = float(location['displayLatLng']['lat'])
            lng = float(location['displayLatLng']['lng'])
            search_query = [('key',MQ_tools.MAPQUEST_KEY),('shapeFormat','raw'),('latLngCollection',str(lat) +","+str(lng))]
            URL = MQ_tools.to_URL(BASE_MQ_ELEVATION_URL,search_query)
            elevation_data = MQ_tools.get_data_from_URL(URL)
            print(elevation_data['elevationProfile'][0]['height'])
        print()
            
