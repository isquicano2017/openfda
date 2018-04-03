# A simple web server using sockets
import socket

# Server configuration
IP = "10.10.105.138"
PORT = 9006
MAX_OPEN_REQUESTS = 5


def process_client(clientsocket):
    """Function for attending the client. It reads their request message and
       sends the response message back, with the requested html content"""

    # Read the request message. It comes from the socket
    # What are received are bytes. We will decode them into an UTF-8 string
    request_msg = clientsocket.recv(1024).decode("utf-8")

    # Split the message into lines and remove the \r character
    request_msg = request_msg.replace("\r", "").split("\n")

    # Get the request line
    request_line = request_msg[0]

    # Break the request line into its components
    request = request_line.split(" ")

    # Get the two component we need: request cmd and path
    req_cmd = request[0]
    path = request[1]

    print("")
    print("REQUEST: ")
    print("Command: {}".format(req_cmd))
    print("Path: {}".format(path))
    print("")

    # Read the html page to send, depending on the path
    if path == "/":
        filename = "index.html"
    else:
        if path == "/new":
            filename = "new.html"
        else:
            filename = "error.html"

    print("File to send: {}".format(filename))

    with open(filename, "r") as f:
        content = f.read()

    # Build the HTTP response message. It has the following lines
    # Status line
    # header
    # blank line
    # Body (content to send)

    # -- Everything is OK
    status_line = "HTTP/1.1 200 OK\n"

    # -- Build the header
    header = "Content-Type: text/html\n"
    header += "Content-Length: {}\n".format(len(str.encode(content)))

    # -- Busild the message by joining together all the parts
    response_msg = str.encode(status_line + header + "\n" + content)
    clientsocket.send(response_msg)


# -----------------------------------------------
# ------ The server start its executiong here
# -----------------------------------------------

# Create the server cocket, for receiving the connections
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


try:
    # Give the socket an IP address and a Port
    serversocket.bind((IP, PORT))

    # This is a server socket. It should be configured for listening
    serversocket.listen(MAX_OPEN_REQUESTS)

    # Server main loop. The server is doing nothing but listening for the
    # incoming connections from the clientes. When there is a new connection,
    # the systems gives the server the new client socket for communicating
    # with the client
    while True:
        # Wait for connections
        # When there is an incoming client, their IP address and socket
        # are returned
        print("Waiting for clients at IP: {}, Puerto: {}".format(IP, PORT))
        (clientsocket, address) = serversocket.accept()

        # Process the client request
        print("  Client request recgeived. IP: {}".format(address))
        print("Server socket: {}".format(serversocket))
        print("Client socket: {}".format(clientsocket))
        process_client(clientsocket)
        clientsocket.close()

except socket.error:
    print("Socket error. Problemas with the PORT {}".format(PORT))
    print("Launch it again in another port (and check the IP)")

#DRUGS: 10DRUGS

import http.client
import json

headers = {'User-Agent': 'http-client'}

conn = http.client.HTTPSConnection("api.fda.gov")
conn.request("GET", "/drug/label.json", None, headers)
r1 = conn.getresponse()
print(r1.status, r1.reason)
repos_raw = r1.read().decode("utf-8")
conn.close()

repos1 = json.loads(repos_raw)

repo=repos1 ['results']

print("The id of the drug is", repo[0]['id'])
print("The purpose of the drug is", repo[0]['purpose'])
print("The manufacture name of the drug is", repo[0]['openfda']['manufacturer_name'])

for index in drugs:
    print( "These are another 10 drugs:",repo[0:10]['id'])



#https://api.fda.gov/drug/label.json
PORT= 8000
with open ("search.html") as file_search:
           message= file_search.read()

           self.wfile.write(bytes(message, "utf8"))
           return
Handler= http.server.SimpleHTTPRequestHandler
Handler= testHTTPRequestHandler

httpd= socketserver.TCPServer(("",Port), Handler)
print("serving at port", PORT)
httpd.serve_forever()