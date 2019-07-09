from SchoolMember import SchoolMember

class Teacher(SchoolMember):
    def __init__(self,name,age,salary):
        super(Teacher,self).__init__(name,age)
        self.s = salary

    def print_info(self):
        print ( "我的名字是：%s，我的年龄是：%d,我的收入是%d" % (self.n, self.a,self.s) )


if __name__ == '__main__':



    s = Teacher ( "dd",38,10000 )
    s.print_info ()
