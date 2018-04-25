import generators
import MQ_tools

output_dict = { 'STEPS':generators.STEPS(),'TOTALDISTANCE':generators.TOTALDISTANCE(),
                'TOTALTIME':generators.TOTALTIME(),'LATLONG':generators.LATLONG(),'ELEVATION':generators.ELEVATION()}

def inp(if_condition:bool,error_str:str):
    '''generalized function for requesting input
    *Note* if_condition is a lambda functi
    on that returns a bool
    *Note* error_str is the message outputted when the if_condition fails
    '''
    while True:
        user_inp = input()     
        if if_condition(user_inp):
            return user_inp
        else:
            print(error_str)
            
def can_int(text:str)->bool:
    '''checks if a string can be converted to an int'''
    try:
        int(text)
    except ValueError:
        return False
    else:
        return True
    
def ask_num(comparison:bool,error_message:str)->int:
    "asks for the number of locations to get directions to"
    return int(inp(comparison,error_message))

def ask_str(condition:bool,error_message:str)->str:
    "asks for location and checks if it is a valid location"
    return inp(condition,error_message)

def valid_route(Json_text:dict)->bool:
    '''checks to see if the route information given is actually route directions'''
    if Json_text != None:
        return Json_text['route']['routeError']['errorCode'] != 0
    return False



if __name__ == '__main__':
    num_location = ask_num(lambda x:can_int(x) and int(x) >= 2, "please enter a number greater than 1")
    location_list = []
    
    for x in range(num_location):
        location_list.append(ask_str(lambda x: len(x) > 0,"please enter a location"))
    route_info = MQ_tools.get_data_from_URL(MQ_tools.to_URL(MQ_tools.BASE_MQ_DIRECTIONS_URL,MQ_tools.location_search_query(location_list)))
    if route_info != None and valid_route(route_info):
        num_outputs = ask_num(lambda x: can_int(x) and int(x) <= 5,'please enter a number between 1 and 5')
        generator_list = []
        for output in range(num_outputs):
            generator_list.append(ask_str(lambda x: x in output_dict,"sorry not a valid output, please try again"))
        print()
        for generator in generator_list:
            output_dict[generator].print_data(route_info)
        print('Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors')
    else:
        if route_info == None:
            print('\nMAPQUEST ERROR')
        else:
            print('\nNO ROUTE FOUND')
        

