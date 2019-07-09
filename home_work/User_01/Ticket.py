'''按照一下要求定义一个游乐园门票类，并尝试计算2个人平日票价
    平日票价100元
    周末票价为平日票价120%
'''
class Ticket(object):
    def __init__(self, isweekemd=False):
        self.price = 100
        if isweekemd :
            self.ratoio =1 #价格率
        else:
            self.ratoio=1.2

    def computer(self, adultcount):

        print('当前价格是：{}'.format(self.ratoio*self.price*adultcount))
        return self.ratoio*self.price*adultcount

T=Ticket(isweekemd=False)
T.computer(10)


#     def __init__(self, workday=True, adult=True):
#         self.price = 100
#         if workday:
#             self.ratio = 1
#         else:
#             self.ratio = 1.2
#         if adult:
#             self.discount = 1
#         else:
#             self.discount = 0.5
#
#     def get_price(self, num):
#         return self.price * self.ratio * self.discount * num
#
#
# adult_1 = Ticket(workday=True, adult=True)
# child_1 = Ticket(workday=True, adult=False)
#
# print("2个成人+1个小孩平日票价为：%.2f" % (adult_1.get_price(2) + child_1.get_price(1)))
#
# adult_2 = Ticket(workday=False, adult=True)
# child_2 = Ticket(workday=False, adult=False)
#
# print("2个成人+1个小孩周末票价为：%.2f" % (adult_2.get_price(2) + child_2.get_price(1)))
# exit(1)


