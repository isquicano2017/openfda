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
        url="/drug/label.json?search=active_ingredient:" + drug + "&" + "limit=" + limit
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
        url = "/drug/label.json?search = manufacturer_name:" + drug + " & " + "limit = " + limit
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
        url = "/drug / label.json? "+"limit = " + limit
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
        for i in range(len(drugs1['results'][i])):
            if 'openfda' in drugs1['results'][i]:
                list1.append(drugs1['results'][i]['openfda']['manufacturer name'][0])
            else:
                list1.append('Unknown')
    def info_drugs1(self, drugs1, list1, limit=10):
        for i in range(len(drugs1['results'][i])):
            if 'openfda' in drugs1['results'][i]:
                list1.append(drugs1['results'][i]['openfda']['brand_name'][0])
            else:
                list1.append('Unknown')
    def info_companies1(self, drugs1, list1, limit=10):
        for i in range(len(drugs1['results'][i])):
            if 'openfda' in drugs1['results'][i]:
                list1.append(drugs1['results'][i]['openfda']['manufacturer_name'][0])
            else:
                list1.append('Unknown')
    def info_warnings(self, drugs1, list1, limit=10):
        for i in range(len(drugs1['results'][i])):
            if 'openfda' in drugs1['results'][i]:
                list1.append(drugs1['results'][i]['openfda']['warnings'][0])
            else:
                list1.append('Unknown')
class OpenFdaHTML():
    def new_html(self,json_list):
        file_html= "<ul>"
        for i in json_list:
            file_html+= "<li>"+ i + "</li>"
        file_html += "</ul>"
        print( "The corresponding HTML file has been created")
    def file_transmit(self,doc):
        with open(doc, "r") as f:
            content= f.read()
        print(doc, "is succesfully prepared to be sent")
        return
class testHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        client=OpenFDAClient()
        parser= OpenFDAParser
        HTML= OpenFdaHTML
        #code=False
        path= self.path
        if path!= "/favicon.ico":
            print("path is:%s..."%path)
        if path=="/":
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
            try:
                print("A request has been made by the client")
                active = path.split("=")[1].split("&")[0]
                try:
                    limit=path.split("=")[2]
            if "&" not in self.path:
                    limit = "10"
                    params = self.path.split("?")[1]
                    drug = params.split("&")[0].split("=")[1]

                    obj1 = Client.communicate_active(drug, limit)
                    Parser.extract_data_sdrugs(obj1, list1)


                elif "&" in self.path:
                    params = self.path.split("?")[1]
                    drug = params.split("&")[0].split("=")[1]
                    limit = params.split("&")[1].split("=")[1]
                    if not limit:
                        limit = "10"
                    obj2 = Client.communicate_active(drug, limit)
                    Parser.extract_data_sdrugs(obj2, list1)
        elif "searchCompany" in self.path:
            self.send_response(200)
            self.send_header('Type of content', 'text/html')
            self.end_headers()
            list1 = []
            try:
                print("A request has been made by the client")
                active = path.split("=")[1].split("&")[0]
                try:
                    limit=path.split("=")[2]
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







