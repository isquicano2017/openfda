import http.client
import json

headers = {'User-Agent': 'http-client'}

conn = http.client.HTTPSConnection("api.fda.gov")
conn.request("GET", "/drug/label.json?search=id&limit=10", None, headers)
r1 = conn.getresponse()
print(r1.status, r1.reason)
repos_raw = r1.read().decode("utf-8")
conn.close()

repos1 = json.loads(repos_raw)
repo=repos1['results']
drugs=json.loads["drugs_raw"]["results"]

for index in drugs:
print("These are another 10 drugs:", repo[0:10], ["id"])
    print(["spl_id"])
