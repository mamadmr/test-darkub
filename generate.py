
#print("""thon3 /Users/trx/Documents/Projects/VPN_MANAGER/test-darkub/encode.py
#login 
#{'success': True, 'msg': '', 'obj': [{'id': 1, 'up': 35110290, 'down': 637896892, 'total': 0, 'remark': 'VPN', 'enable': True, 'expiryTime': 0, 'clientStats': [{'id': 1, 'inboundId': 1, 'enable': True, 'email': 'bcscbmt1b', 'up': 962636, 'down': 22730036, 'expiryTime': 0, 'total': 0, 'reset': 0}, {'id': 2, 'inboundId': 1, 'enable': True, 'email': 'somethingnew', 'up': 1427293, 'down': 22664951, 'expiryTime': 0, 'total': 0, 'reset': 0}, {'id': 3, 'inboundId': 1, 'enable': True, 'email': 'uyt', 'up': 13114022, 'down': 183485808, 'expiryTime': 0, 'total': 0, 'reset': 0}, {'id': 5, 'inboundId': 1, 'enable': True, 'email': 'test2', 'up': 0, 'down': 0, 'expiryTime': 0, 'total': 0, 'reset': 0}, {'id': 7, 'inboundId': 1, 'enable': True, 'email': 'samaneh', 'up': 17984946, 'down': 407928453, 'expiryTime': 0, 'total': 0, 'reset': 0}, {'id': 8, 'inboundId': 1, 'enable': True, 'email': 'test', 'up': 1211710, 'down': 971968, 'expiryTime': 0, 'total': 0, 'reset': 0}, {'id': 9, 'inboundId': 1, 'enable': True, 'email': 'hg', 'up': 0, 'down': 0, 'expiryTime': 0, 'total': 0, 'reset': 0}, {'id': 10, 'inboundId': 1, 'enable': True, 'email': 'hgg', 'up': 0, 'down': 0, 'expiryTime': 1705342334198, 'total': 11811160064, 'reset': 0}], 'listen': '', 'port': 54343, 'protocol': 'vless', 'settings': '{\n  "clients": [\n    {\n      "email": "bcscbmt1b",\n      "enable": true,\n      "expiryTime": 0,\n      "flow": "",\n      "id": "5ecdc251-92b0-43be-d7f4-d273cf224310",\n      "reset": 0,\n      "subId": "19n8hlu8ejne1nnx",\n      "tgId": "",\n      "totalGB": 0\n    },\n    {\n      "email": "somethingnew",\n      "enable": true,\n      "expiryTime": 0,\n      "flow": "",\n      "id": "5ecdc251-92b0-43be-d7f4-d273cf224310",\n      "reset": 0,\n      "subId": "19n8hlu8ejne1nnx",\n      "tgId": "",\n      "totalGB": 0\n    },\n    {\n      "email": "uyt",\n      "enable": true,\n      "expiryTime": 0,\n      "flow": "",\n      "id": "5ecdc251-92b0-43be-d7f4-d273cf224320",\n      "reset": 0,\n      "subId": "19n8hlu8ejne1nnx",\n      "tgId": "",\n      "totalGB": 0\n    },\n    {\n      "email": "test2",\n      "enable": true,\n      "expiryTime": 0,\n      "flow": "",\n      "id": "5ecdc251-92b0-43be-d7f4-d273cf224333",\n      "reset": 0,\n      "subId": "19n8hlu8ejne1nnx",\n      "tgId": "",\n      "totalGB": 0\n    },\n    {\n      "email": "samaneh",\n      "enable": true,\n      "expiryTime": 0,\n      "flow": "",\n      "id": "5ecdc251-92b0-43be-d7f4-d273cf224555",\n      "reset": 0,\n      "subId": "19n8hlu8ejne1nnx",\n      "tgId": "",\n      "totalGB": 0\n    },\n    {\n      "email": "test",\n      "enable": true,\n      "expiryTime": 0,\n      "flow": "",\n      "id": "5ecdc251-92b0-43be-d7f4-d273cf224666",\n      "reset": 0,\n      "subId": "19n8hlu8ejne1nnx",\n      "tgId": "",\n      "totalGB": 0\n    },\n    {\n      "email": "hg",\n      "enable": true,\n      "expiryTime": 0,\n      "flow": "",\n      "id": "5ecdc251-92b0-43be-d7f4-d273cf224888",\n      "reset": 0,\n      "subId": "19n8hlu8ejne1nnx",\n      "tgId": "",\n      "totalGB": 0\n    },\n    {\n      "email": "hgg",\n      "enable": true,\n      "expiryTime": 1705342334198,\n      "flow": "",\n      "id": "5ecdc251-92b0-43be-d7f4-d273cf224999",\n      "reset": 0,\n      "subId": "19n8hlu8ejne1nnx",\n      "tgId": "",\n      "totalGB": 11811160064\n    }\n  ],\n  "decryption": "none",\n  "fallbacks": []\n}', 'streamSettings': '{\n  "network": "ws",\n  "security": "none",\n  "externalProxy": [],\n  "wsSettings": {\n    "acceptProxyProtocol": false,\n    "path": "/",\n    "headers": {}\n  }\n}', 'tag': 'inbound-54343', 'sniffing': '{\n  "enabled": true,\n  "destOverride": [\n    "http",\n    "tls",\n    "quic",\n    "fakedns"\n  ]\n}'}]}""")
#exit()

import base64 
import json 



vmess = "vmess://eyJhZGQiOiJkaXJlY3QtZmQ1MzYyYWRiYS1yaHZwLXJlaXMuYXBwcy5pci10aHItYmExLmFydmFuY2Fhcy5pciIsImFpZCI6IjAiLCJhbHBuIjoiIiwiZnAiOiIiLCJob3N0IjoiIiwiaWQiOiI1ZWNkYzc2NS05MmIwLTQzYmUtZDdmNC1kMjczY2YyMjQ1NTUiLCJuZXQiOiJ3cyIsInBhdGgiOiIvYXBpIiwicG9ydCI6IjQ0MyIsInBzIjoiTWFuYWdlci1oZWxsbyBhcGkiLCJzY3kiOiJhdXRvIiwic25pIjoiIiwidGxzIjoidGxzIiwidHlwZSI6IiIsInYiOiIyIn0="


first = "vmess://eyJhZGQiOiJkaXJlY3QtZmQ1MzYyYWRiYS1yaHZwLXJlaXMuYXBwcy5pci10aHItYmExLmFydmFuY2Fhcy5pciIsImFpZCI6IjAiLCJhbHBuIjoiIiwiZnAiOiIiLCJob3N0IjoiIiwiaWQiOiJhMzZlNWZlYy1kMmE0LTRlN2MtYTczNC0xMmVmNmQ2YjYzZTIiLCJuZXQiOiJ3cyIsInBhdGgiOiIvYXBpIiwicG9ydCI6IjQ0MyIsInBzIjoidGVzdCIsInNjeSI6ImF1dG8iLCJzbmkiOiIiLCJ0bHMiOiJ0bHMiLCJ0eXBlIjoiIiwidiI6IjIifQ=="
secon = "vmess://eyJhZGQiOiJkaXJlY3QtZmQ1MzYyYWRiYS1yaHZwLXJlaXMuYXBwcy5pci10aHItYmExLmFydmFuY2Fhcy5pciIsImFpZCI6IjAiLCJhbHBuIjoiIiwiZnAiOiIiLCJob3N0IjoiIiwiaWQiOiJhMzZlNWZlYy1kMmE0LTRlN2MtYTczNC0xMmVmNmQ2YjYzZTIiLCJuZXQiOiJ3cyIsInBhdGgiOiIvYXBpIiwicG9ydCI6IjQ0MyIsInBzIjoidGVzdCIsInNjeSI6ImF1dG8iLCJzbmkiOiIiLCJ0bHMiOiJ0bHMiLCJ0eXBlIjoiIiwidiI6IjIifQ=="

vmess = secon[8:]
vmess = base64.b64decode(vmess)
vmess = vmess.decode('utf-8')

first = {"add":"direct-fd5362adba-rhvp-reis.apps.ir-thr-ba1.arvancaas.ir","aid":"0","alpn":"","fp":"","host":"","id":"a36e5fec-d2a4-4e7c-a734-12ef6d6b63e2","net":"ws","path":"/api","port":"443","ps":"test","scy":"auto","sni":"","tls":"tls","type":"","v":"2"}
secon = {"add":"direct-fd5362adba-rhvp-reis.apps.ir-thr-ba1.arvancaas.ir","aid":"0","alpn":"","fp":"","host":"","id":"a36e5fec-d2a4-4e7c-a734-12ef6d6b63e2","net":"ws","path":"/api","port":"443","ps":"test","scy":"auto","sni":"","tls":"tls","type":"","v":"2"}

import requests 
import json
import datetime
import time

ip = "http://165.232.88.184"
port = '1381'
password = 'reisi'
username = 'reisi'


# login
url = f'{ip}:{port}/login'
data = {'username': username, 'password': password}
try:
    response = requests.post(url, json=data, timeout=5)
except:
    print("can't connect to server")
    exit()

coockie = response.cookies.copy()
#print(coockie)

print("login ")
# get all inbounds
#url = f'{ip}:{port}/xui/API/inbounds/'
#res = requests.get(url, cookies=response.cookies)
#data = res.json()
#print(data)
#exit()

email = 'Hashemi_alireza'
# generate UUID 
import uuid
id = str(uuid.uuid4()) 
name = 'Hashemi'

totalGB =   30
totalGB *= 1073741824
date = "2024-05-22 13:44:33"
date_format = "%Y-%m-%d %H:%M:%S"
date = datetime.datetime.strptime(date, date_format)
date = int(time.mktime(date.timetuple())) * 1000

x = {'id': 1, 'up': 231149859, 'down': 857697361, 'total': 0, 'remark': 'Manager', 'enable': True, 'expiryTime': 0, 'clientStats': [], 'listen': '', 'port': 50386, 'protocol': 'vmess', 'settings': '{\n  "clients": [\n    {\n      "id": "'+id+'",\n      "flow": "",\n      "email": "'+email+'",\n      "totalGB":'+str(totalGB)+',\n      "expiryTime": '+str(date)+',\n      "enable": true,\n      "tgId": "",\n      "subId": "19n8hlu8ejne1nnx",\n      "reset": 0\n    }\n  ],\n  "decryption": "none",\n  "fallbacks": []\n}', 'streamSettings': '{\n  "network": "ws",\n  "security": "none",\n  "externalProxy": [],\n  "wsSettings": {\n    "acceptProxyProtocol": false,\n    "path": "/api",\n    "headers": {}\n  }\n}', 'tag': 'inbound-50386', 'sniffing': '{\n  "enabled": true,\n  "destOverride": [\n    "http",\n    "tls" ]\n}'}

url = f'{ip}:{port}/xui/API/inbounds/addClient/'
res = requests.post(url, json=x, cookies=response.cookies)
print(res.text)

template = '{"add":"amssecond.darkube.app","aid":"0","alpn":"","fp":"","host":"","id":"'+id+'","net":"ws","path":"/api","port":"443","ps":"'+str(name)+'","scy":"auto","sni":"","tls":"tls","type":"","v":"2"}'
template2 = '{"add":"second-9e53c38923-direct.apps.ir-tbz-sh1.arvancaas.ir","aid":"0","alpn":"","fp":"","host":"","id":"'+id+'","net":"ws","path":"/api","port":"443","ps":"'+str(name)+'","scy":"auto","sni":"","tls":"tls","type":"","v":"2"}'

vmess = "vmess://"+base64.b64encode(template.encode('utf-8')).decode('utf-8')
print(vmess)
vmess = "vmess://"+base64.b64encode(template2.encode('utf-8')).decode('utf-8')
print()
print()
print(vmess)

#config = "vless://5ecdc251-92b0-43be-d7f4-d273cf224320@London.rtshyg.ir:443?path=%2F&security=tls&encryption=none&type=ws"
#temp_config = 'vless://' + id + config[43:] + '#' + name
# decode base64

#print(temp_config)