import socket
import sys
import json
import geocoder

def getInfoFromServer(latlang):
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = ('172.30.136.211', 10000)

    sock.connect(server_address)

    try:

        # Send data
        message = latlang.encode('UTF-8')
        print('sending {!r}'.format(message))
        sock.sendall(message)

        # Look for the response
        amount_received = 0
        amount_expected = len(message)

        #Gets info from server
        data_json = sock.recv(4000)

        #turns bytes in json
        data = data_json.decode()


    finally:
        print('closing socket')
        sock.close()
        return(data)

def getLatLang():
    """
    Dynamically gets location and returns it in a usuable format
    """
    g = geocoder.ip('me')
    out = ''
    out = out + str(g.latlng[0]) + ',' + str(g.latlng[1])
    return out

def makeUseable(json_ob):
    return(json_ob)

print(makeUseable(getInfoFromServer(getLatLang())))
