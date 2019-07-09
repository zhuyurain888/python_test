class Person:
    def __init__(self,name,weigth):
        self.name = name
        self.weigth = weigth
    def __str__(self):
        return  "我的名字叫%s 体重是%.2f 公斤" %(self.name,self.weigth)
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
xiaoming.currentWeigth()