import http.server
import socketserver
import json
import http.client

IP= "10.10.108.118"
PORT= 9006
socketserver.TCPServer.allow_reuse_address= True

class OpenFdaHTML():
    def new_html(self,list1):
        intro= "<!doctype html>" + "\n" + "<html>" + "\n" + "<body>" + "\n" + "<ul>" + "\n"
        final= "</ul>" + "\n" + "</body>" + "\n" + "</html>"
        with open ("drug.html", "w") as f:
            f.write(intro)
            for elem in list1:
                elem1= "<li>" +  elem + "</li>" + "\n"
HTML= OpenFdaHTML()

class OpenFDAClient():
    def inform_drug(self, drug, limit):
        headers= {'User_Agent': 'http_client'}
        conn= http.client.HTTPSConnection("api.fda.gov")
        url="/drug/label.json?search=active_ingredient:" + drug + "&" + "limit=" + limit
        conn.request("GET", url, None, headers)
        r1 = conn.getresponse()
        drugs_raw = r1.read().decode("utf-8")
        conn.close()
        drug = json.loads(drugs_raw)
        drugs1 = drug
        return drugs1
    def inform_company (self, drug, limit):
        headers = {'User-Agent': 'http-client'}
        conn = http.client.HTTPSConnection("api.fda.gov")
        url = "/drug/label.json?search = manufacturer_name:" + drug + " & " + "limit = " + limit
        conn.request("GET", url, None, headers)
        r1 = conn.getresponse()
        drugs_raw = r1.read().decode("utf-8")
        conn.close()
        drug = json.loads(drugs_raw)
        drugs1 = drug
        return drugs1
    def inform_lists (self, limit):
        headers = {'User-Agent': 'http-client'}
        conn = http.client.HTTPSConnection("api.fda.gov")
        url = "/drug/label.json?" + "limit =" + limit
        conn.request("GET", url, None, headers)
        r1 = conn.getresponse()
        drugs_raw = r1.read().decode("utf-8")
        conn.close()
        drug = json.loads(drugs_raw)
        drugs1 = drug
        return drugs1
client= OpenFDAClient()

class OpenFDAParser():
    def info_drugs (self,drugs1,list1):
        for i in range(len(drugs1["results"][i])):
            if 'active_ingredient' in drugs1["results"][i]:
                list1.append(drugs1["results"][i]["active_ingredient"][0])
            else:
                list1.append ("Unknown")
    def info_companies (self, drugs1, list1):
        for i in range(len(drugs1["results"][i])):
            try:
                if 'openfda' in drugs1["results"][i]:
                    list1.append(drugs1["results"][i]["openfda"]["manufacturer name"][0])
            except KeyError:
                list1.append("Unknown")
    def info_drugs1(self, drugs1, list1):
        for i in range(len(drugs1["results"][i])):
            if "openfda" in drugs1["results"][i]:
                list1.append(drugs1["results"][i]["openfda"]["brand_name"][0])
            except KeyError:
                list1.append("Unknown")
    def info_companies1(self, drugs1, list1):
        for i in range(len(drugs1["results"][i])):
            if "openfda" in drugs1["results"][i]:
                list1.append(drugs1["results"][i]["openfda"]["manufacturer_name"][0])
            except KeyError:
                list1.append('Unknown')
    def info_warnings(self, drugs1, list1):
        for i in range(len(drugs1["results"][i])):
            if "warnings" in drugs1["results"][i]:
                list1.append(drugs1["results"][i]["openfda"]["warnings"][0])
            else:
                list1.append('Unknown')
Parser= OpenFDAParser()

class testHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        try:

            if path=='/':
                self.send_response(200)
                self.send_header('Type of content', 'text/html')
                self.end_headers()
                with open("search_html", "r")as f:
                    content= f.read
                    self.wfile.write(bytes(content,"utf8"))
            elif "searchDrug" in self.path:
                self.send_response(200)
                self.send_header('Type of content', 'text/html')
                self.end_headers()
                list1=[]

                if "&" not in self.path:
                    limit = "10"
                    params = self.path.split("?")[1]
                    drug = params.split("&")[0].split("=")[1]

                    obj1 = Client.inform_drug(drug, limit)
                    Parser.info_drugs(obj1, list1)


                elif "&" in self.path:
                    params = self.path.split("?")[1]
                    drug = params.split("&")[0].split("=")[1]
                    limit = params.split("&")[1].split("=")[1]
                    if not limit:
                        limit = "10"
                    obj2 = Client.inform_drug(drug, limit)
                    Parser.info_drugs(obj2, list1)
                HTML.html_visual(list1)
                with open("drug.html", "r") as f:
                    f=f.read()
                self.wfile.write(bytes(f,"utf8"))
            elif "searchCompany" in self.path:
                self.send_response(200)
                self.send_header('Type of content', 'text/html')
                self.end_headers()
                list1 = []
                if "&" not in self.path:
                    limit = "10"
                    params = self.path.split("?")[1]
                    drug = params.split("&")[0].split("=")[1]

                    obj3 = Client.communicate_active(drug, limit)
                    Parser.extract_data_sdrugs(obj3, list1)

                elif "&" in self.path:
                    params = self.path.split("?")[1]
                    drug = params.split("&")[0].split("=")[1]
                    limit = params.split("&")[1].split("=")[1]
                    if not limit:
                        limit = "10"
                    obj4 = Client.communicate_active(drug, limit)
                    Parser.extract_data_sdrugs(obj4, list1)
        elif "listDrugs" in self.path:
            self.send_response(200)
            self.send_header('Type of content', 'text/html')
            self.end_headers()
            list1 = []
            try:
                print("A request has been made by the client")
                try:
                    limit=path.split("=")[1]

            obj5 = Client.communicate_list(limit)
            Parser.extract_data_ldrugs(obj5, list1)
        elif "listCompanies" in self.path:
            self.send_response(200)
            self.send_header('Type of content', 'text/html')
            self.end_headers()
            list1 = []
            try:
                print("A request has been made by the client")
                try:
                    limit = path.split("=")[1]
            obj6 = Client.communicate_list(limit)
            Parser.extract_data_ldrugs(obj6, list1)
        elif "listWarnings" in self.path:
            self.send_response(200)
            self.send_header('Type of content', 'text/html')
            self.end_headers()
            list1 = []
            try:
                print("A request has been made by the client")
                try:
                    limit = path.split("=")[1]
            obj7 = Client.communicate_list(limit)
            Parser.extract_data_ldrugs(obj7, list1)







