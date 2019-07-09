import unittest
import re
class TestBaidu(unittest.TestCase):
    def setUp(self):
        pass
    def test_baidu(self):
        with open ( 'aa.txt', 'r', encoding='utf-8' ) as ff:
            zif = 'https://movie.douban.com/subject/23232876/101010'
            try:
                print (self.assertIn( zif, ff.readlines() ) )
                # print ( ss )
            except:
                print('不在这个里面')

            for line in ff.readlines ():
                if line == 'https://movie.douban.com/subject/23232876/':
                    print ( 'True' )
                else:
                    print ( 'FLASE' )

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
