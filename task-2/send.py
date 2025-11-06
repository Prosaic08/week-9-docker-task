import sys, http.client

message = sys.argv[1]
headers = {"Content-type": "application/x-www-form-urlencoded",
           "Accept": "text/plain"}
conn = http.client.HTTPConnection("listen", 8080)
conn.request("POST", "/", body=message, headers=headers)
response = conn.getresponse()
print(response.status, response.reason)

data = response.read()
print(data)

conn.close()
