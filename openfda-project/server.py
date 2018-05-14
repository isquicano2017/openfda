import http.server
import socketserver
import json
import http.client

IP = "10.10.108.135"
PORT = 8091
socketserver.TCPServer.allow_reuse_address = True


class OpenFDA_HTML():
    def visual_html(self, list1):
        intro = "<!doctype html>" + "\n" + "<html>" + "\n" + "<body>" + "\n" "<ul>" + "\n"
        final = "</ul>" + "\n" + "</body>" + "\n" + "</html>"

        with open("drug.html", "w") as f:
            f.write(intro)
            for elem in list1:
                elem_1 = "<li>" + elem + "</li>" + "\n"
                f.write(elem_1)
            f.write(final)


HTML = OpenFDA_HTML()


class OpenFDA_Client():
    def inform_drug(self, drug, limit):
        headers = {"User-Agent": "http-client"}
        conn = http.client.HTTPSConnection("api.fda.gov")
        url_inform_drug = "/drug/label.json?search=active_ingredient:" + drug + "&" + "limit=" + limit
        conn.request("GET", url_inform_drug, None, headers)
        r1 = conn.getresponse()
        drugs_raw = r1.read().decode("utf-8")
        conn.close()
        drug = json.loads(drugs_raw)
        drug_1 = drug
        return drug_1

    def inform_company(self, drug, limit):
        headers = {"User-Agent": "http-client"}
        conn = http.client.HTTPSConnection("api.fda.gov")
        url_inform_company = "/drug/label.json?search=manufacturer_name:" + drug + " & " + "limit = " + limit
        conn.request("GET", url_inform_company, None, headers)
        r1 = conn.getresponse()
        drug_raw = r1.read().decode("utf-8")
        conn.close()
        drug = json.loads(drug_raw)
        drug_1 = drug
        return drug_1

    def inform_lists(self, limit):
        headers = {"User-Agent": "http-client"}
        conn = http.client.HTTPSConnection("api.fda.gov")
        url_inform_lists = "/drug/label.json?" + "limit =" + limit
        conn.request("GET", url_inform_lists, None, headers)
        r1 = conn.getresponse()
        drug_raw = r1.read().decode("utf-8")
        conn.close()
        drug = json.loads(drug_raw)
        drug_1 = drug
        return drug_1


Client = OpenFDA_Client()


class OpenFDA_Parser():
    def info_drug(self, drug_1, list1):
        for i in range(len(drug_1["results"])):
            if 'active_ingredient' in drug_1["results"][i]:
                list1.append(drug_1["results"][i]["active_ingredient"][0])
            else:
                list1.append("Unknown")

    def info_companies(self, drug_1, list1):
        for i in range(len(drug_1["results"])):
            try:
                if 'openfda' in drug_1["results"][i]:
                    list1.append(drug_1["results"][i]["openfda"]["manufacturer name"][0])
            except KeyError:
                list1.append("Unknown")

    def info_drugs_1(self, drug_1, list1):
        for i in range(len(drug_1["results"])):
            try:
                if "openfda" in drug_1["results"][i]:
                    list1.append(drug_1["results"][i]["openfda"]["brand_name"][0])
            except KeyError:
                list1.append("Unknown")

    def info_companies1(self, drug_1, list1):
        for i in range(len(drug_1["results"])):
            try:
                if "openfda" in drug_1["results"][i]:
                    list1.append(drug_1["results"][i]["openfda"]["manufacturer_name"][0])
            except KeyError:
                list1.append('Unknown')

    def info_warnings(self, drug_1, list1):
        for i in range(len(drug_1["results"])):
            if "warnings" in drug_1["results"][i]:
                list1.append(drug_1["results"][i]["openfda"]["warnings"][0])
            else:
                list1.append('Unknown')


Parser = OpenFDA_Parser()


class testHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):

        try:

            if self.path == "/":
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                with open("search.html", "r")as f:
                    data = f.read()
                    self.wfile.write(bytes(data, "utf8"))
            elif "searchDrug" in self.path:
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                list1 = []

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

                HTML.visual_html(list1)

                with open("drug.html", "r") as f:
                    file = f.read()
                self.wfile.write(bytes(file, "utf8"))

            elif "searchCompany" in self.path:
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                list1 = []

                if "&" not in self.path:
                    limit = "10"
                    params = self.path.split("?")[1]
                    drug = params.split("&")[0].split("=")[1]

                    obj3 = Client.inform_company(drug, limit)
                    Parser.info_companies(obj3, list1)

                elif "&" in self.path:
                    params = self.path.split("?")[1]
                    drug = params.split("&")[0].split("=")[1]
                    limit = params.split("&")[1].split("=")[1]

                    if not limit:
                        limit = "10"

                    obj4 = Client.inform_company(drug, limit)
                    Parser.info_companies(obj4, list1)

                HTML.visual_html(list1)
                with open("drug.html", "r") as f:
                    f = f.read()
                self.wfile.write(bytes(f, "utf8"))

            elif "listDrugs" in self.path:
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                list1 = []
                params = self.path.split("?")[1]
                limit = params.split("=")[1]

                obj5 = Client.inform_lists(limit)
                Parser.info_drugs1(obj5, list1)

                HTML.visual_html(list1)
                with open("drug.html", "r") as f:
                    f = f.read()
                self.wfile.write(bytes(f, "utf8"))

            elif "listCompanies" in self.path:
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                list1 = []
                params = self.path.split("?")[1]
                limit = params.split("=")[1]

                obj6 = Client.inform_lists(limit)
                Parser.info_companies1(obj6, list1)

                HTML.visual_html(list1)
                with open("drug.html", "r") as f:
                    f = f.read()
                self.wfile.write(bytes(f, "utf8"))

            elif "listWarnings" in self.path:
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                list1 = []
                params = self.path.split("?")[1]
                limit = params.split("=")[1]

                obj7 = Client.inform_lists(limit)
                Parser.info_warnings(obj7, list1)

                HTML.visual_html(list1)
                with open("drug.html", "r") as f:
                    file = f.read()
                self.wfile.write(bytes(file, "utf8"))

            elif "secret" in self.path:
                self.send_response(401)
                self.send_header("WWW-Authenticate", "Basic realm='OpenFDA Private Zone")
                self.end_headers()

            elif "redirect" in self.path:
                self.send_response(302)
                self.send_header("Location", "http://localhost:8000/")
                self.end_headers()

            else:
                self.send_response(404)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                with open("error.html", "r") as f:
                    file = f.read()
                self.wfile.write(bytes(file, "utf8"))
        except KeyError:
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            with open("error.html", "r") as f:
                file = f.read()
            self.wfile.write(bytes(file, "utf8"))

        return


Handler = testHTTPRequestHandler

httpd = socketserver.TCPServer((IP, PORT), Handler)
print("Serving at port", PORT)

try:
    httpd.serve_forever()
except KeyboardInterrupt:
    pass

httpd.server_close()
