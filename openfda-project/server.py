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
        return drugs1
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
        return drugs1
    def inform_lists (self, limit):
        headers = {'User-Agent': 'http-client'}
        conn = http.client.HTTPSConnection("api.fda.gov")
        url = / drug / label.json? + "limit = " + limit
        conn.request("GET", url, None, headers)
        r1 = conn.getresponse()
        drugs_raw = r1.read().decode("utf-8")
        conn.close()
        drug = json.loads(drugs_raw)
        drugs_1 = drug
        return drugs1

class OpenFDAParser():
    def info_drugs (self,drugs1,list1,limit=10):
        for i in range(len(drugs1['results'][i])):
            if 'active_ingredient' in drugs1['results'][i]:
                list1.append(drugs1['results'][i]['active_ingredient'][0])
            else:
                list1.append ('Unknown')
    def info_companies (self, drugs1, list1, limit=10):

