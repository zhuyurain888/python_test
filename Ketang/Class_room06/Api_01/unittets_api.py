import unittest
class test (unittest.TestCase):
    def setUp(self):
        pass
    def test_A(self):
        a=1
        b=1
        a=b

        print(self.assertEqual(a,b))
        print(self.assertIs(a, b))

    def tearDown(self):
        pass

if __name__ =="__main__"