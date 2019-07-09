class Stu:
    count = 0
    name = ''
    No=0

    def __init__(self, name, No):

        self.name =name
        self.No =No
        Stu.count+=1

    # def __str__(self):
    #
    #     return "名字是：%s,学号是：%d" %(self.name,self.No)

    def work(self):

        print("%s在学习"%(self.name))

    def myNo(self):

        print("我叫%s，学号是：%d"%(self.name,self.No))


s1=Stu("lily",1)
s2=Stu("tom",10)
print(s1.name)
s1.work()
s2.myNo()
print(Stu.count)



