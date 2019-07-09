import requests
import json
response = requests.get("http://39.107.96.138:3000/api/v1/messages?accesstoken=f029f080-e51d-48b1-b27c-1e917991aa21&mdrender=true")
print(response)
get_data =response.json()
print(get_data)
'''
get /messages 获取已读和未读消息
接收 get 参数

accesstoken String
mdrender String 当为 false 时，不渲染。默认为 true，渲染出现的所有 markdown 格式文本。
------------------------------------
post /topic/:topic_id/replies 新建评论
接收 post 参数

accesstoken String 用户的 accessToken
content String 评论的主体
reply_id String 如果这个评论是对另一个评论的回复，请务必带上此字段。这样前端就可以构建出评论线索图。
返回值示例

{success: true, reply_id: '5433d5e4e737cbe96dcef312'}
'''
body={
    'accesstoken':'f029f080-e51d-48b1-b27c-1e917991aa21',
    'content':'天王盖地府',
    'reply_id':'5d0f6d265d71cf52feab872e'
}
response_newrelaies =requests.post(
    "http://39.107.96.138:3000/api/v1/topic/5d0f6bf85d71cf52feab872a/replies",data=body)
print(response_newrelaies)
get_newdata=response_newrelaies.json()




update_new_body=(
    {
     'accesstoken':'f029f080-e51d-48b1-b27c-1e917991aa21',
     'topic_id': '5d0f61c95d71cf52feab8719',
     'title': '抓个和尚做晚餐',
     'tab': 'ask',
     'content': '这里的上水一样甜'}
)
response_update_topics = requests.post('http://39.107.96.138:3000/api/v1/topics/update',data= update_new_body)
update_topics = response_update_topics.json()
print(response_update_topics)
print(update_topics)
# assertEqual(True, update_topics['success'])