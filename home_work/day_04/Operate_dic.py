class  Mydict(object):
    def __init__(self, mdict):
        self.mdict = mdict

    def get_mydict(self, key):
        if key not in self.mdict.keys():
            print(key,'aaaa')
            print('{} 未找到该内容'.format(key))
            return None
        else:
            # return self.mdict[key]
            return  self.mdict.get(key)

    def del_mydict(self, key):
        if key not in self.mdict.keys():
            print('{} 未找到该内容'.format(key))

        else:
            # del(self.mdict[key])
            s=self.mdict.pop(key)
            print(s,'aaaa')

    def get_value(self):
        return(self.mdict.keys(),self.mdict.items())


dishes = Mydict({'jack': 4098, 'guido': 4127, 'irv': 41260000})
print(dishes.get_mydict('irv'))
print(dishes.get_value())
print(dishes.del_mydict('irv'))
print(dishes.get_mydict('irv'))
print(dishes.get_value())