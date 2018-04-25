from collections import namedtuple
import socket

PollingConnection = namedtuple('PollingConnection',['socket','input','output'])

def connect(host:str,port:int)->PollingConnection:
    polling_socket = socket.socket()
    polling_socket.connect((host,port))
    polling_socket_in = polling_socket.makefile('r')
    polling_socket_out = polling_socket.makefile('w')
    return PollingConnection(socket = polling_socket,input = polling_socket_in,output = polling_socket_out)
def close(connection:PollingConnection)->None:
    connection.input.close()
    connection.output.close()
    connection.socket.close()

h = input('enter host')
p = int(input('enter port'))
new = connect(h,p)
new.output.write("I32CFSP_HELLO Calvin"+'\r\n')
new.output.flush()
print(new.input.readline()[:-1])
print('successful')
close(new)

