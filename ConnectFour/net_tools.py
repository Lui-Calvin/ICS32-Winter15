#Calvin Lui 84152100 & Nicholas sprague 49389270 lab section
import socket


def connect()->"list of socket info":
    """asks user for server and port, returns socket, socket input file, socket output file"""
    while True:
        host = input("Please type in a host address: ")
        port = input("Please type a port number: ")
        sock = socket.socket()
        try:
            sock.connect((host,int(port)))
            sock_inp = sock.makefile('r')
            sock_out = sock.makefile('w')
            return [sock, sock_inp, sock_out]
        except:
            print("Failed to connect to server. Please try again")
            

def receive_input(s:"list of socket info")->str:
    """returns response from server"""
    return s[1].readline()[:-1]

def send_output(s:"list of socket info",out:str)-> None:
    """sends output to server"""
    s[2].write(out + '\r\n')
    s[2].flush()

def close_connection(s:"list of socket info")->None:
    """closes the connection with the server"""
    s[1].close()
    s[2].close()
    s[0].close()
