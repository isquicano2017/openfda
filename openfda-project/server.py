import http.server
import socketserver
import json
import http.client

IP= "localhost"
PORT= 9006
socketserver.TCPServer.allow_reuse_address= True

class OpenFDAHTML():
    def html_visual(self, list_1):
        