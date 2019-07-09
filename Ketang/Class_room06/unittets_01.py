import unittest
import requests
import json

'''
<Response [200]> aaa
{'success': True, 'data': [{'id': '5d0f42a95d71cf52feab3b43', 'author_id': '5bdb225ad3dee53d612219ab', 'tab': 'ask', 'content': '<div class="markdown-text"><p>小何老师1111111111</p>\n</div>', 'title': '小何老师1111111111', 'last_reply_at': '2019-06-23T09:13:13.538Z', 'good': False, 'top': False, 'reply_count': 0, 'visit_count': 1, 'create_at': '2019-06-23T09:13:13.538Z', 'author': {'loginname': 'user2', 'avatar_url': '//gravatar.com/avatar/ad11bc82d27b89b08a69c6b3e812531f?size=48'}}, {'id': '5d0f42a95d71cf52feab3b3b', 'author_id': '5bdb2259d3dee53d612219aa', 'tab': 'ask', 'content': '<div class="markdown-text"><p>小何老师1111111111</p>\n</div>', 'title': '小何老师1111111111', 'last_reply_at': '2019-06-23T09:13:13.212Z', 'good': False, 'top': False, 'reply_count': 0, 'visit_count': 1, 'create_at': '2019-06-23T09:13:13.212Z', 'author': {'loginname': 'user1', 'avatar_url': '//gravatar.com/avatar/2bb54360661318946c0ee63a29c441cd?size=48'}}, {'id': '5d0f42a95d71cf52feab3b35', 'author_id': '5bdb2267d3dee53d612219b3', 'tab': 'ask', 'content': '<div class="markdown-text"><p>小何老师1111111111</p>\n</div>', 'title': '小何老师1111111111', 'last_reply_at': '2019-06-23T09:13:13.112Z', 'good': False, 'top': False, 'reply_count': 0, 'visit_count': 1, 'create_at': '2019-06-23T09:13:13.112Z', 'author': {'loginname': 'user10', 'avatar_url': '//gravatar.com/avatar/3bc661c19338ee0996a1ac10e4613f25?size=48'}}, {'id': '5d0f42a95d71cf52feab3b33', 'author_id': '5bdb2257d3dee53d612219a9', 'tab': 'ask', 'content': '<div class="markdown-text"><p>小何老师1111111111</p>\n</div>', 'title': '小何老师1111111111', 'last_reply_at': '2019-06-23T09:13:13.103Z', 'good': False, 'top': False, 'reply_count': 0, 'visit_count': 1, 'create_at': '2019-06-23T09:13:13.103Z', 'author': {'loginname': 'user0', 'avatar_url': '//gravatar.com/avatar/707e452e6674f89339f417394def009f?size=48'}}, {'id': '5d0f42a95d71cf52feab3b31', 'author_id': '5bdb2261d3dee53d612219af', 'tab': 'ask', 'content': '<div class="markdown-text"><p>小何老师你可拉倒吧</p>\n</div>', 'title': '小何老师真帅', 'last_reply_at': '2019-06-23T09:13:13.095Z', 'good': False, 'top': False, 'reply_count': 0, 'visit_count': 1, 'create_at': '2019-06-23T09:13:13.095Z', 'author': {'loginname': 'user6', 'avatar_url': '//gravatar.com/avatar/e4f22e7ee76d3e531c0a58002fcb2ad7?size=48'}}, {'id': '5d0f35055d71cf52feab0512', 'author_id': '5bdb225ad3dee53d612219ab', 'tab': 'ask', 'content': '<div class="markdown-text"><p>hhhhllllllllllllllllllllll</p>\n</div>', 'title': 'hhhhhhhhhhhhhhhkkkkkk', 'last_reply_at': '2019-06-23T09:13:13.056Z', 'good': False, 'top': False, 'reply_count': 6, 'visit_count': 1, 'create_at': '2019-06-23T08:15:01.513Z', 'author': {'loginname': 'user2', 'avatar_url': '//gravatar.com/avatar/ad11bc82d27b89b08a69c6b3e812531f?size=48'}}, {'id': '5d0f42a85d71cf52feab3b2e', 'author_id': '5bdb225ad3dee53d612219ab', 'tab': 'ask', 'content': '<div class="markdown-text"><p>小何老师1111111111</p>\n</div>', 'title': '小何老师1111111111', 'last_reply_at': '2019-06-23T09:13:12.907Z', 'good': False, 'top': False, 'reply_count': 0, 'visit_count': 1, 'create_at': '2019-06-23T09:13:12.907Z', 'author': {'loginname': 'user2', 'avatar_url': '//gravatar.com/avatar/ad11bc82d27b89b08a69c6b3e812531f?size=48'}}, {'id': '5d0f42a85d71cf52feab3b27', 'author_id': '5bdb2261d3dee53d612219af', 'tab': 'ask', 'content': '<div class="markdown-text"><p>小何老师1111111111</p>\n</div>', 'title': '小何老师1111111111', 'last_reply_at': '2019-06-23T09:13:12.103Z', 'good': False, 'top': False, 'reply_count': 0, 'visit_count': 1, 'create_at': '2019-06-23T09:13:12.103Z', 'author': {'loginname': 'user6', 'avatar_url': '//gravatar.com/avatar/e4f22e7ee76d3e531c0a58002fcb2ad7?size=48'}}, {'id': '5d0f42a75d71cf52feab3b1c', 'author_id': '5bdb225cd3dee53d612219ac', 'tab': 'ask', 'content': '<div class="markdown-text"><p>小何老师你可拉倒吧</p>\n</div>', 'title': '小何老师真帅', 'last_reply_at': '2019-06-23T09:13:11.794Z', 'good': False, 'top': False, 'reply_count': 0, 'visit_count': 3, 'create_at': '2019-06-23T09:13:11.794Z', 'author': {'loginname': 'user3', 'avatar_url': '//gravatar.com/avatar/dc608c983d193a7f30be98935dbe2aac?size=48'}}, {'id': '5d0f42a75d71cf52feab3b1b', 'author_id': '5bdb2267d3dee53d612219b3', 'tab': 'ask', 'content': '<div class="markdown-text"><p>小何老师1111111111</p>\n</div>', 'title': '小何老师1111111111', 'last_reply_at': '2019-06-23T09:13:11.782Z', 'good': False, 'top': False, 'reply_count': 0, 'visit_count': 1, 'create_at': '2019-06-23T09:13:11.782Z', 'author': {'loginname': 'user10', 'avatar_url': '//gravatar.com/avatar/3bc661c19338ee0996a1ac10e4613f25?size=48'}}, {'id': '5d0f42a75d71cf52feab3b1a', 'author_id': '5bdb225ad3dee53d612219ab', 'tab': 'ask', 'content': '<div class="markdown-text"><p>小何老师1111111111</p>\n</div>', 'title': '小何老师1111111111', 'last_reply_at': '2019-06-23T09:13:11.780Z', 'good': False, 'top': False, 'reply_count': 0, 'visit_count': 1, 'create_at': '2019-06-23T09:13:11.780Z', 'author': {'loginname': 'user2', 'avatar_url': '//gravatar.com/avatar/ad11bc82d27b89b08a69c6b3e812531f?size=48'}}, {'id': '5d0f42a75d71cf52feab3b15', 'author_id': '5bdb2257d3dee53d612219a9', 'tab': 'ask', 'content': '<div class="markdown-text"><p>小何老师1111111111</p>\n</div>', 'title': '小何老师1111111111', 'last_reply_at': '2019-06-23T09:13:11.739Z', 'good': False, 'top': False, 'reply_count': 0, 'visit_count': 1, 'create_at': '2019-06-23T09:13:11.739Z', 'author': {'loginname': 'user0', 'avatar_url': '//gravatar.com/avatar/707e452e6674f89339f417394def009f?size=48'}}, {'id': '5d0f42a75d71cf52feab3b12', 'author_id': '5bdb2261d3dee53d612219af', 'tab': 'ask', 'content': '<div class="markdown-text"><p>小何老师1111111111</p>\n</div>', 'title': '小何老师1111111111', 'last_reply_at': '2019-06-23T09:13:11.728Z', 'good': False, 'top': False, 'reply_count': 0, 'visit_count': 1, 'create_at': '2019-06-23T09:13:11.728Z', 'author': {'loginname': 'user6', 'avatar_url': '//gravatar.com/avatar/e4f22e7ee76d3e531c0a58002fcb2ad7?size=48'}}, {'id': '5d0f42a75d71cf52feab3b0e', 'author_id': '5bdb2260d3dee53d612219ae', 'tab': 'ask', 'content': '<div class="markdown-text"><p>小何老师你可拉倒吧</p>\n</div>', 'title': '小何老师真帅', 'last_reply_at': '2019-06-23T09:13:11.255Z', 'good': False, 'top': False, 'reply_count': 0, 'visit_count': 4, 'create_at': '2019-06-23T09:13:11.255Z', 'author': {'loginname': 'user5', 'avatar_url': '//gravatar.com/avatar/7540ae6ab98e723238d131f06f5a8e20?size=48'}}, {'id': '5d0f42a65d71cf52feab3b0a', 'author_id': '5bdb225cd3dee53d612219ac', 'tab': 'ask', 'content': '<div class="markdown-text"><p>小何老师1111111111</p>\n</div>', 'title': '小何老师1111111111', 'last_reply_at': '2019-06-23T09:13:10.384Z', 'good': False, 'top': False, 'reply_count': 0, 'visit_count': 1, 'create_at': '2019-06-23T09:13:10.384Z', 'author': {'loginname': 'user3', 'avatar_url': '//gravatar.com/avatar/dc608c983d193a7f30be98935dbe2aac?size=48'}}, {'id': '5d0f42a55d71cf52feab3b05', 'author_id': '5bdb2260d3dee53d612219ae', 'tab': 'ask', 'content': '<div class="markdown-text"><p>小何老师1111111111</p>\n</div>', 'title': '小何老师1111111111', 'last_reply_at': '2019-06-23T09:13:09.633Z', 'good': False, 'top': False, 'reply_count': 0, 'visit_count': 1, 'create_at': '2019-06-23T09:13:09.633Z', 'author': {'loginname': 'user5', 'avatar_url': '//gravatar.com/avatar/7540ae6ab98e723238d131f06f5a8e20?size=48'}}, {'id': '5d0f42a55d71cf52feab3afa', 'author_id': '5bdb225cd3dee53d612219ac', 'tab': 'ask', 'content': '<div class="markdown-text"><p>小何老师1111111111</p>\n</div>', 'title': '小何老师1111111111', 'last_reply_at': '2019-06-23T09:13:09.136Z', 'good': False, 'top': False, 'reply_count': 0, 'visit_count': 1, 'create_at': '2019-06-23T09:13:09.136Z', 'author': {'loginname': 'user3', 'avatar_url': '//gravatar.com/avatar/dc608c983d193a7f30be98935dbe2aac?size=48'}}, {'id': '5d0f42a55d71cf52feab3af9', 'author_id': '5bdb2260d3dee53d612219ae', 'tab': 'ask', 'content': '<div class="markdown-text"><p>小何老师1111111111</p>\n</div>', 'title': '小何老师1111111111', 'last_reply_at': '2019-06-23T09:13:09.134Z', 'good': False, 'top': False, 'reply_count': 0, 'visit_count': 1, 'create_at': '2019-06-23T09:13:09.134Z', 'author': {'loginname': 'user5', 'avatar_url': '//gravatar.com/avatar/7540ae6ab98e723238d131f06f5a8e20?size=48'}}, {'id': '5d0f42a25d71cf52feab3ae4', 'author_id': '5bdb225ed3dee53d612219ad', 'tab': 'ask', 'content': '<div class="markdown-text"><p>小何老师你可拉倒吧</p>\n</div>', 'title': '小何老师真帅', 'last_reply_at': '2019-06-23T09:13:06.741Z', 'good': False, 'top': False, 'reply_count': 0, 'visit_count': 4, 'create_at': '2019-06-23T09:13:06.741Z', 'author': {'loginname': 'user4', 'avatar_url': '//gravatar.com/avatar/45fb1f72c75e81addeeb580021d251ff?size=48'}}, {'id': '5d0f42a15d71cf52feab3ad5', 'author_id': '5bdb225ed3dee53d612219ad', 'tab': 'ask', 'content': '<div class="markdown-text"><p>小何老师1111111111</p>\n</div>', 'title': '小何老师1111111111', 'last_reply_at': '2019-06-23T09:13:05.807Z', 'good': False, 'top': False, 'reply_count': 0, 'visit_count': 1, 'create_at': '2019-06-23T09:13:05.807Z', 'author': {'loginname': 'user4', 'avatar_url': '//gravatar.com/avatar/45fb1f72c75e81addeeb580021d251ff?size=48'}}]}
dict_keys(['success', 'data']) www
'''
class test (unittest.TestCase):
    def setUp(self):
        pass
    # def test_Login(self):
    #     response = requests.get('http://39.107.96.138:3000/api/v1/topic_collect/?user18')
    #     r5 = response.json()
    #
    #     # self.assertIn(True,response1['success'])
    #     self.assertEquals(True, r5['success'])

    def test_Topics(self):
        response = requests.get('http://39.107.96.138:3000/api/v1/topics')
        r1=response.json()

        # self.assertIn(True,response1['success'])
        self.assertEquals(True,r1['success'])

    def test_TopicsView(self):
        response2 = requests.get('http://39.107.96.138:3000/api/v1/topics/?accesstoken=d807b298-576d-47f4-8849-0c5052cc049&5d0f318b5d71cf52feab0438')
        r2 = response2.json()

        # self.assertIn(True,response1['success'])
        self.assertEquals(True, r2['success'])
    def test_CreatTopics(self):
        body = {
            'accesstoken': 'd807b298-576d-47f4-8849-0c5052cc049c',
            'title': '天王盖地府',
            'tab': 'ask',
            'content': '宝塔镇河妖'
        }


        response3 = requests.post(url="http://39.107.96.138:3000/api/v1/topics", data=body)
        r3= response3.json()
        print(r3,'333')
        self.assertEquals(True, r3['success'])

    def test_CreatTopicUpdate(self):
        body2 = {
            'accesstoken': 'd807b298-576d-47f4-8849-0c5052cc049c',
            'topic_id': '5d0f318b5d71cf52feab0438',
            'title': '修改标题为：666',
            'tab': 'ask',
            'content': 'zhuyu'
        }

        response4 = requests.post(url="http://39.107.96.138:3000/api/v1/topics/update", data=body2)
        r4= response4.json()
        print(r4,'444')
        self.assertEquals(True, r4['success'])
    # def test_Colloct(self):
    #     body3 = {
    #         'accesstoken': 'd807b298-576d-47f4-8849-0c5052cc049c',
    #         'topic_id': '5d0f318b5d71cf52feab0438'
    #     }
    #
    #     response5 = requests.post(url="http://39.107.96.138:3000/api/v1/topic_collect/collect", data=body3)
    #     r5=response5.json()
    #     print(r5, '555')
    #     self.assertEquals('true', r5['success'])

    # def test_Login(self):
    #     response = requests.get('http://39.107.96.138:3000/api/v1/topic_collect/?user18')
    #     r5 = response.json()
    #
    #     # self.assertIn(True,response1['success'])
    #     self.assertEquals(True, r5['success'])
    def test_Replies(self):
        body22 = {
                'accesstoken':'f029f080-e51d-48b1-b27c-1e917991aa21',
                'content':'天王盖地府',
                'reply_id':'5d0f6d265d71cf52feab872e'
        }
        response6 = requests.post('http://39.107.96.138:3000/api/v1/topic/5d0f6bf85d71cf52feab872a/replies',data=body22)
        r6 = response6.json()

        self.assertEquals(True, r6['success'])
    def test_Getmessages(self):
        responseq = requests.get(
            "http://39.107.96.138:3000/api/v1/messages?accesstoken=f029f080-e51d-48b1-b27c-1e917991aa21&mdrender=true")
        print(responseq)
        get_data = responseq.json()
        print(get_data,'qqq')
        self.assertEquals(True, get_data['success'])
    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()  # 运行所有的测试用例