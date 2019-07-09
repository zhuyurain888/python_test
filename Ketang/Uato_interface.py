import unittest
from typing import Any, Union

import requests
from requests import Response


class Interface_test(unittest.TestCase):
    def setUp(self):
        self.base_url = 'http://39.107.96.138:3000/api/v1/'
        self.accesstoken = '61016896-5eab-4f01-bd76-06e98f410c19'
        self.test_topic_id = '5d1af1d25d71cf52feabaabb'
        self.reply_id ='5d117e875d71cf52feab8a3d'
        self.body = {
            'accesstoken': self.accesstoken
        }

    # def test_topics(self):
    #     response = requests.get(self.base_url + 'topics')
    #     # print(response)#返回响应code
    #     topics_response = response.json()
    #     self.assertEqual(True, topics_response['success'])
    #
    # def test_topics_view(self):
    #     # get /topic/:id 主题详情
    #     # •mdrender String 当为 false 时，不渲染。默认为 true，渲染出现的所有 markdown 格式文本。
    #     # •accesstoken String 当需要知道一个主题是否被特定用户收藏以及对应评论是否被特定用户点赞时，才需要带此参数。会影响返回值中的 is_collect 以及 replies 列表中的 is_uped 值。
    #
    #     response_topics_view = requests.get(self.base_url + 'topic/' + self.test_topic_id)
    #     # print(response_topics_view)
    #     topics_view = response_topics_view.json()
    #     # print(topics_view)
    #     self.assertEqual(topics_view['success'], True)

    # def test_create_topics(self):
    #     new_body = self.body
    #     new_body.update({'title': '抓个和尚做晚餐', 'tab': 'ask', 'content': '这里的上水一样甜'})
    #     response_create_topics = requests.post(self.base_url + "topics", new_body)
    #     create_topocs = response_create_topics.json()
    #     self.assertEqual(True, create_topocs['success'])

    # post /topics/update 编辑主题

    # def test_update_topics(self):
    #
    #     update_new_body =self.body
    #     update_new_body.update({'topic_id': '5d0f61c95d71cf52feab8719','title':'抓个和尚做晚餐', 'tab':'ask', 'content':'这里的上水一样甜'})
    #     response_update_topics = requests.post(self.base_url + "topics/update", update_new_body)
    #     update_topics = response_update_topics.json()
    #     print(response_update_topics)
    #     self.assertEqual(update_topics['success'],True)

    # post /topic_collect/collect 收藏主题
    def test_topic_collect(self):
        collect_new_body = self.body
        collect_new_body.update({'topic_id': self.test_topic_id})
        response_topic_collect = requests.post(self.base_url + "topic_collect/collect", collect_new_body)
        print(response_topic_collect)
        topic_colltec = response_topic_collect.json()
        print(topic_colltec,'1111')
        self.assertEqual(True, topic_colltec['success'])
#
#     #     #post /topic_collect/de_collect 取消主题
    def test_de_collect(self):
        de_collect_new_body = self.body
        de_collect_new_body.update({'topic_id': self.test_topic_id})
        response_de_collect =requests.post(self.base_url +"topic_collect/de_collect",de_collect_new_body)
        de_collect =response_de_collect.json()
        print(de_collect)
        self.assertEqual(de_collect['success'],True)
#
# #get /topic_collect/:loginname 用户所收藏的主题
#
#     def test_get_topic_collect(self):
#         response_get_topic_collect = requests.get(self.base_url + '/topic_collect/user10')
#         # print(response)#返回响应code
#         get_user_topics = response_get_topic_collect.json()
#         print(get_user_topics,'333')
#         self.assertEqual(True, get_user_topics['success'])
#post /topic/:topic_id/replies 新建评论
    #
    # def test_create_replies(self):
    #     creat_replies_new_body =self.body
    #     creat_replies_new_body.update({'content':'真心英雄，是你吗？'})
    #     create_replies=requests.post(self.base_url + 'topic/'+ self.test_topic_id +'/replies',creat_replies_new_body)
    #     # print(create_replies)
    #     response_create_replies =create_replies.json()
    #     self.assertEqual(True, response_create_replies['success'])

#post /reply/:reply_id/ups 为评论点赞
    # def test_reply_ups(self):
    #     reply_ups_new_body =self.body
    #     # reply_ups_new_body.update(
    #     reply_ups =requests.post(self.base_url + 'reply/'+ self.reply_id +'/ups',reply_ups_new_body)
    #     response_reply_ups =reply_ups.json()
    #     print(response_reply_ups)
    #     self.assertEqual(True, response_reply_ups['success'])
    #
    # def test_verify_accesstoken(self):
    #     '''
    #     post /accesstoken 验证 accessToken 的正确性
    #     '''
    #     post_accesstoken_url = self.base_url + 'accesstoken'
    #     post_accesstoken_repsonse = requests.post(post_accesstoken_url, self.body)
    #     print(post_accesstoken_repsonse.json())
    #     self.assertEqual(post_accesstoken_repsonse.json()['success'], True)

    # def test_get_message_count(self):
    #     '''
    #     get /message/count 获取未读消息数
    #     '''
    #     get_message_count_url = self.base_url + 'message/count' + '?accesstoken=' +self.accesstoken
    #     print(get_message_count_url)
    #     # get_message_count_repsonse = requests.get("http://39.107.96.138:3000/api/v1/message/count?accesstoken=f029f080-e51d-48b1-b27c-1e917991aa21")
    #     get_message_count_repsonse = requests.get(get_message_count_url)
    #
    #     print(get_message_count_repsonse,"ssss")
    #     self.assertEqual(get_message_count_repsonse.json()['success'], True)
    #
    # def test_get_messages(self):
    #     '''
    #     get /messages 获取已读和未读消息
    #     '''
    #     get_messages_url = self.base_url + 'messages' + '?accesstoken=' +self.accesstoken
    #     print(get_messages_url)
    #     get_messages_response = requests.get(get_messages_url)
    #     print(get_messages_response,'wwwww')
    #     self.assertEqual(get_messages_response.json()['success'], True)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
