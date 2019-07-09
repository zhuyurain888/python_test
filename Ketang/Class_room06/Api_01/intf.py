import requests
import json

response = requests.get('http://39.107.96.138:3000/api/v1/topics')
# response = requests.get('https://cnodejs.org/api/v1/topics')
print(response,'aaa')
print(response.json())
js_data = response.json()
keys = js_data.keys()
print(keys, 'www')
#
# for k in js_data['data']:
#     print(str(k['id']))
#     response2 = requests.get('http://39.107.96.138:3000/api/v1/topic/'+k['id']+
#                                                                                 '?'+'accessToken=d807b298-576d-47f4-8849-0c5052cc049c&mdrender=false')
#     # response2 = requests.get('https://cnodejs.org/api/v1/topic/{}' . format(k['id']+
#     #                                                                         '?'+'accessToken=d807b298-576d-47f4-8849-0c5052cc049c&mdrender=false'))
#     print(response2.json())

# #get请求访问
# response = requests.get('https://cnodejs.org/api/v1/topics?')
# print(response.json())

#post 请求访问
# title=''
# content=''
# i=0
# for i in range(10):
#     body = {
#         'accesstoken':'d807b298-576d-47f4-8849-0c5052cc049c',
#         'title': title+str(i),
#         'tab': 'ask',
#         'content': content+str(i)
#     }
#     i += 1
#
#     response = requests.post(url="http://39.107.96.138:3000/api/v1/topics",data=body)
#     print(response)
# # response = requests.post(url='http://39.107.96.138:3000/api/v1/topics',data=dumps.body())
#     try:
#         if response.status_code == 200:
#             print(response.json())
#         else:
#             print('errors')
#
#     except:
#         print('访问失败')

'''
post /topics/update 编辑主题
接收 post 参数

accesstoken String 用户的 accessToken
topic_id String 主题id
title String 标题
tab String 目前有 ask share job
content String 主体内'''

body2 = {
        'accesstoken': 'd807b298-576d-47f4-8849-0c5052cc049c',
        'topic_id': '5d0f318b5d71cf52feab0438',
        'title':'修改标题为：666',
        'tab': 'ask',
        'content':'zhuyu'
    }
response2 = requests.post(url="http://39.107.96.138:3000/api/v1/topics/update",data=body2)
print(response2.json())

'''
url = "http://39.107.96.138:3000/api/v1/topic_collect/collect"
data = {
"accesstoken":"d807b298-576d-47f4-8849-0c5052cc049c",
"topic_id": "5d0f318b5d71cf52feab0438" 
}'''
#收藏
body3 = {
    "accesstoken":"d807b298-576d-47f4-8849-0c5052cc049c",
    "topic_id": "5d0f318b5d71cf52feab0438"
}

response3 = requests.post(url="http://39.107.96.138:3000/api/v1/topic_collect/collect",data=body3)
print(response3.text,'6666')

#取消收藏
body4 = {
    "accesstoken":"d807b298-576d-47f4-8849-0c5052cc049c",
    "topic_id": "5d0f318b5d71cf52feab0438"
}

response4 = requests.post(url="http://39.107.96.138:3000/api/v1/topic_collect/collect/de_collect",data=body4)
print(response4.text)
