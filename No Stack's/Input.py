#michaelhm
import MQ_Outputs
import MQ_Tools

outputs = {'LATLONG':MQ_Outputs.LATLONG(),'ELEVATION':MQ_Outputs.ELEVATION(),
           'STEPS':MQ_Outputs.STEPS(),'TOTALTIME':MQ_Outputs.TOTALTIME(),
           'TOTALDISTANCE':MQ_Outputs.TOTALDISTANCE()}

def ask_location()->str:
    while True:
        ret_str = input()
        if ret_str != "":
            return ret_str
        else:
            print("please enter a location")

def ask_number(lamb:bool)->int:
    while True:
        num = input()
        try:
            num = int(num)
            if lamb(num):
                return num
            else:
                print('sorry, invalid number')
        except ValueError:
            print('sorry, please enter a number')

def ask_output():
    while True:
        inp = input()
        if inp in outputs:
            return inp
        else:
            print('sorry not valid output')
    

if __name__ == '__main__':
    num_loc = ask_number(lambda x: x >= 2)
    locations = []
    for x in range(num_loc):
        locations.append(ask_location())
    route_data = MQ_Tools.get_result(MQ_Tools.Location_URL(locations))
    if route_data != None and route_data['route']['routeError']['errorCode'] != 0:
        num_outputs = ask_number(lambda x: x > 0 and x < 6)
        out = []
        for x in range(num_outputs):
            out.append(ask_output())
        for item in out:
            outputs[item].print_info(route_data)
    else:
        print('MAPQUEST ERROR')
    


    
