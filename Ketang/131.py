import unittest
import requests



class Interface_test(unittest.TestCase):
    def setUp(self):
        self.base_url='http://39.107.96.138:3000/api/v1/'
        accesstoken='f029f080-e51d-48b1-b27c-1e917991aa21'
        self.test_topic_id = '5d0f61c95d71cf52feab8719'
        body={
            'accesstoken': accesstoken
        }


    def test_topics_view(self):
        response_topics_view =requests.get(self.base_url + 'topic/'+self.test_topic_id)
        print(response_topics_view)




'''接收 get 参数
•mdrender String 当为 false 时，不渲染。默认为 true，渲染出现的所有 markdown 格式文本。
•accesstoken String 当需要知道一个主题是否被特定用户收藏以及对应评论是否被特定用户点赞时，才需要带此参数。
会影响返回值中的 is_collect 以及 replies 列表中的 is_uped 值。
示例：/api/v1/topic/5433d5e4e737cbe96dcef312
'''
        # ponse_topics_view = requests.get(self.base_url + 'topic/' + self.test_topic_id)
        # topics_view =ponse_topics_view.json()
        # self.assertEqual(True, topics_view['sussess'])


    def tearDown(self):
        pass
if __name__=="__main__":
    unittest.main()