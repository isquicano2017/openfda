import http.server
import socketserver
import json
import http.client

IP= "localhost"
PORT= 9006
socketserver.TCPServer.allow_reuse_address= True

class OpenFDAClient():
    def inform_communication(self, drug, limit):
        headers= {'User-Agent': 'http-client'}
        conn= http.client.HTTPSConnection("api.fda.gov")
        url=/drug/label.json?search=active_ingredient:" + drug + "&" + "limit=" + limit
        conn.request("GET", url, None, headers)
        r1 = conn.getresponse()
        drugs_raw = r1.read().decode("utf-8")
        conn.close()
        drug = json.loads(drugs_raw)
        drugs_1 = drug
        return drugs_1
    def inform_company (self, drug, limit):
        headers = {'User-Agent': 'http-client'}
        conn = http.client.HTTPSConnection("api.fda.gov")
        url = / drug / label.json?search = manufacturer_name:" + drug + " & " + "
        limit = " + limit
        conn.request("GET", url, None, headers)
        r1 = conn.getresponse()
        drugs_raw = r1.read().decode("utf-8")
        conn.close()
        drug = json.loads(drugs_raw)
        drugs_1 = drug
        return drugs_1
