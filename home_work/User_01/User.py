class User(object):
    count=0
    def __init__(self, first_name, last_name, age, gender='男'):
        '''对属性进行初始化'''
        self.first_name =first_name
        self.last_name=last_name
        self.age =age
        self.gender=gender
        User.count+=1

    def show_userinfo(self):
        '''显示用户信息'''
        # print("我的姓是:%s,名字是：%s,年龄是：%d"%(self.first_name,self.last_name,self.age))
        print("我的姓是:%s,名字是：%s,年龄是：%d，性别是：%s" % ( self.last_name,self.first_name, self.age,self.gender))
    def greet_user(self):
        '''根据用户性别，给出对应的问候 '''
        greet ='{}{}'.format(self.last_name,self.first_name)
        if self.gender =='男':
            greet=greet+'先生，你好！'
        elif self.gender =='女':
            greet = greet + '女士， 您好!'
        else:
            greet = greet + ' 您好'
        print(greet)

user=User("Tom","Kelis",18)
user.show_userinfo()
user.greet_user()
print(User.count)