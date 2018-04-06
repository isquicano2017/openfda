import http.server
import socketserver
import http.client
import json

socketserver.TCPServer.allow_reuse_address= True

PORT = 8094

# HTTPRequestHandler class
class testHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    # GET
    def do_GET(self):
        # Send response status code
        self.send_response(200)

        # Send headers
        self.send_header('Content-type','text/html')
        self.end_headers()

        f=open ('test-html.html', 'r')
        f.read(message)
        f.close

        headers = {'User-Agent': 'http-client'}

        conn = http.client.HTTPSConnection("api.fda.gov")
        conn.request("GET", "/drug/label.json", None, headers)
        r1 = conn.getresponse()
        print(r1.status, r1.reason)
        repos_raw = r1.read().decode("utf-8")
        conn.close()

        repos1 = json.loads(repos_raw)

        repos1 = json.loads(repos_raw)

        repo = repos1['results']
        for i in range [0,10]:
            message= ("The corresponding of the drug is:",repo[i]['id'])

        # Send message back to client
        message = "Hello world! " + self.path
        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))
        return

#Handler = http.server.SimpleHTTPRequestHandler
Handler = testHTTPRequestHandler

httpd = socketserver.TCPServer(("", PORT), Handler)
print("serving at port", PORT)
httpd.serve_forever()

# https://github.com/joshmaker/simple-python-webserver/blob/master/server.py