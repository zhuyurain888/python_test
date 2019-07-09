class A(object):#python3可以不写object，python2要写，这里写上是为了在2或3中都可以执行
    def test(self):
        print('from A')
    pass
class B(A):
    def test3(self):
        print("from B")
    pass

class C(A):
    def test5(self):
        print("from C")
    pass
class D(B):
    def test2(self):
        print("from D")
    pass
class E(C):
    def test4(self):
        print("from E")
    pass
class F(D,E):
    def test1(self):
        print("from F")
    pass
f1=F()
f1.test()
print(F.mro())#F.__mro__与这个一致
# F->D->B->E->C->A->object报错