#michaehm

import MQ_Tools

class TOTALDISTANCE:
    def print_info(self, Json_text:dict):
        print("TOTAL DISTANCE: {} miles".format(round(int(Json_text['route']['distance']))))
        print()

class TOTALTIME:
    def print_info(self, Json_text:dict):
        print("TOTAL TIME: {} minutes".format(round(int(Json_text['route']['time'])/60)))
        print()

class STEPS:
    def print_info(self, Json_text:dict):
        print("DIRECTIONS")
        for legs in Json_text['route']['legs']:
            for steps in legs['maneuvers']:
                print(steps['narrative'])
        print()


class LATLONG:
    def print_info(self, Json_text:dict):
        print("LATLONGS")
        for coordinates in Json_text['route']['locations']:
            lng = float(coordinates['displayLatLng']['lng'])
            lat = float(coordinates['displayLatLng']['lat'])
            lng_direction = 'E'
            lat_direction = 'N'
            if lat < 0:
                        lat_direction = 'S'
                        lat = lat * -1
            if lng < 0:
                        lng_direction = 'W'
                        lng = lng * -1
            print ("{:.2f}{} {:.2f}{}".format(lat, lat_direction, lng, lng_direction))
        print()

class ELEVATION:
    def print_info(self,Json_text:dict):
        print("ELEVATION")
        for location in Json_text['route']['locations']:
            lat = float(location['displayLatLng']['lat'])
            lng = float(location['displayLatLng']['lng'])
            Elevation_data = MQ_Tools.get_result(MQ_Tools.Elevation_URL(lat,lng))
            if Elevation_data != None:
                print(Elevation_data['elevationProfile'][0]['height'])
            else:
                print('MAPQUEST ERROR')
        print()
        
if __name__ == '__main__':
    L = ['Irvine, CA','Riverside, CA','Moreno Valley, CA']
    x = MQ_Tools.Location_URL(L)
    y = MQ_Tools.get_result(x)

    outputs = [STEPS(), TOTALDISTANCE(), TOTALTIME(), LATLONG(),ELEVATION()]
    for x in outputs:
        x.print_info(y)









#print("Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors")
