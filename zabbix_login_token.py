# _*_ coding:utf-8 _*_

import requests

url = "http://192.168.32.27/zabbix/api_jsonrpc.php"

zabbix_login = requests.post(url,
                             headers={"Content-Type": "application/json-rpc"},
                             json={ 
                                    "jsonrpc": "2.0",
                                    "method": "user.login",
                                    "params": {
                                        "user": "Admin",
                                        "password": "zabbix"},
                                                               
                                     "id": 1,
                                     "auth": None
                                     }
                            
                             )
token_json = zabbix_login.json()
print(token_json["result"])

print(zabbix_login.text)