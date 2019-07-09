import requests
import json

#连续新增多条数据在论坛中
title = []
content = []
for i in range(2):
    title.append('titlez'+str(i))
    content.append('contentz'+str(i))
    body = {
    "accesstoken": "d807b298-576d-47f4-8849-0c5052cc049c",
    "title": title[i],
    "tab": "ask",
    "content":content[i]
    }
    response = requests.post(url="http://39.107.96.138:3000/api/v1/topics",data=body)
    print(response)
    if response.status_code ==200:
        print(response.json())
    else:
        print("error")