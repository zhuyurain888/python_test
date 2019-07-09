class SchoolMember:
    def __init__(self,name,age):

        self.n=name
        self.a=age
    def print_info(self):
        print("我的名字是：%s，我的年龄是：%d" %(self.n,self.a))
if __name__ == '__main__':

    s=SchoolMember("haha",18)
    s.print_info()
            