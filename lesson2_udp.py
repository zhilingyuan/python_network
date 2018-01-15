import argparse
import socket


#udp broadcast
bufsize=65535
def server(interface,port):
    sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sock.bind(interface,port)#bind the socket to a public  host
    
    print('listening for datagrams at {}'.format(socket.getsockname()))
    while True:
        data,address=sock.recvfrom(bufsize)
        text=data.decode('ascii')
        print('the client at {} says :{!r}'.format(address,text))

def client(network,port):
    #create an INET,STEAMimg SOCKET that means the UDP sockets
    sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    #connect to eht web server on port 80- the normal http port
    #s.connect(('www.python.org',80))
    sock.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)
    text = 'Broadcast datagram!'
    sock.sendto(text.encode('ascii'), (network, port))

if __name__ == '__main__':
    choices = {'client': client, 'server': server}
    parser = argparse.ArgumentParser(description='Send, receive UDP broadcast')
    parser.add_argument('role', choices=choices, help='which role to take')
    parser.add_argument('host', help='interface the server listens at;'
                        ' network the client sends to')
    parser.add_argument('-p', metavar='port', type=int, default=1060,
                        help='UDP port (default 1060)')
    args = parser.parse_args()
    function = choices[args.role]
    function(args.host, args.p)
