class Employee:
    # name =''
    # job=''
    # pay=0
    # salary=null
    def __init__(self, name, job, pay ,salary):
            self.name=name
            self.job=job
            self.pay=pay
            self.salary=salary


    def giveraise(self,salary,percent):

        salary=salary+percent*salary

        # print(salary)
        return '加薪后的工资是：%d'%(self.salary)

    def __str__(self):
        return 'Person: %s,%s, %d, %d' % (self.name,  self.job , self.pay,self.salary)


class Manager(Employee):

    def giveraise(self, salary,percent, bonus):
        salary = salary + percent * salary+bonus * salary
        print(salary)
        return '加薪后的工资和奖金是：%d' % (self.salary)


tom=Manager('小米','工程师',10000,0.1)
tom.giveraise(10000,0.2,0.2)
print(tom)


'''class Person:
    def __init__(self,name,weigth):
        self.name = name
        self.weigth = weigth
    def __str__(self):
        return  "我的名字叫%s 体重是%。2f 公斤" %(self.name,self.weigth)
    def run(self):
        print("%s 爱跑步，跑步锻炼身体" %self.name)
        self.weigth -=0.5
    def eat(self):
        print ( "%s 是吃货，吃完了再减肥" % self.name )
        self.weigth += 1
    def currentWeigth(self):
        print ( "当前体重: %s " % self.weigth)

xiaoming = Person("小明",75.0)
xiaoming.run()
xiaoming.eat()
xiaoming.currentWeigth()'''