#using soket 
import socket
from urllib.parse import quote_plus
def geocode(address):
    sock=socket.socket()
    sock.connect(('maps.google.com',80))
    request=request_text.format(quote_plus(address))
    sock.sendall(request.encode('ascii'))
    raw_reply=b''
    while True:
        more=sock.recv(4096)
        if not more:
            break
        raw_reply+=more
    print(raw_reply.decode('utf-8'))

if __name__=='__main__':
    geocode('207 N.Defiance St,Archbold,OH')
