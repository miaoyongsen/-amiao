import requests
import json
from requests.auth import AuthBase
from requests.auth import HTTPBasicAuth

################      MQTT服务器EMQv2.0--HTTP接口api


url = 'http://xxx.xxx.xxx.xxx:8181/restconf/operations/strategy-manager:handle-block'
header = {
    'Content-Type': 'application/json'
}
data = {
    'input': {
        'policy-id': 'bab09cd7-4d1e-37c1-8fec-5aaa2f78f8e5',
        'policy-action': '1',
        'start-time': 1562733537,
        'end-time': 1562733637,
        'block-attributes': [
            {
            'node': 'acb09cd7-4d1e-37c1-8fec-5aaa2f78f8e6',
            'if-name': 'gigabitethernet0',
            'bind-direction': '1',
            'src-ip': '130.255.6.0',
            'src-mask': '0.0.0.255',
            'dst-ip': '12.63.0.2',
            'dst-mask': '0.0.0.0',
            'src-port': 80,
            'dst-port': 80,
            'protocol': 1
        }
        ]
    }
}
#response = requests.post(url,data=data,headers=header)
#MQTT服务器EMQv2.0--HTTP接口api    以下是格式
auth = HTTPBasicAuth('admin','admin')    #账号和密码
#格式别忘了   json
html = requests.post(url,auth=auth,headers=header,data=json.dumps(data))

print(html.status_code)
print(html.text)