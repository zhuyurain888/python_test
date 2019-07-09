# class B:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#
# class A ( B ):
#     def __init__(self, a, b, c):
#         super ( A, self ).__init__ ( a, b )
#         self.c = c
#
#     def print_info(self):
#         print ( a, b, c )
#
#
# ss = A ( 1, 2, 3 )
# ss.print_info ()



class Bird:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        self.hungry = True

    def eat(self):
        if self.hungry:
            print ( '饿了' )
            self.hungry = False
        else:
            print ( '不饿' )


class SongBird ( Bird ):
    def __init__(self,a,b,c):
        super ( SongBird,self ).__init__ (a,b)
        self.c=c
        self.sound = '唱歌'

    def sing(self):
        print ( self.sound )


sb = SongBird (1,2,3)
sb.sing ()
sb.eat ()
