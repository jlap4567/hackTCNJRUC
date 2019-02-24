import socket
import sys
import restFinder
import json

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('172.30.136.211', 10000)
# Bind the socket to the port
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)
            # data = '40.7243,-74.0018'
            #print('received {!r}'.format(data))
            if data:
                data = format(data)
                data = data.replace('b', '')
                data = data[1:-1]
                print(data)
                print('sending data back to the client')
                out = restFinder.getinfo(data)
                out_json = json.dumps({'info': out})
                print(out_json)
                connection.sendall(bytes(out_json, 'utf-8'))
                # print(response)
            else:
                print('no data from', client_address)
                break

    finally:
        # Clean up the connection
        connection.close()
