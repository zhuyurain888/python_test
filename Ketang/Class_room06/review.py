import time
t = (2009, 2, 17, 17, 3, 38, 1, 48, 0)
t = time.mktime(t)
print(t)
print(time.strftime("%b %d %Y %H:%M:%S", time.gmtime(t)))

print(time.strftime("%b %d %Y %H:%M:%S"))
print(time.localtime(time.time()))
# path.capitalize()
# path.center()
# path.endwith()
# path.index()
# path.find()#找不到下标不会报错


# list_empty=[]
# num =[2,3,4,5,6,7,8,9]
# list_empty=[i for i in num if i % 2==1]#列表生产式
# print(list_empty)
#
ids = [1,4,3,3,4,2,3,4,5,6,1]
print(list(set(ids)))

b=[]
a=[3,4,5,7,8,[9,5],4,2,2,6,[5],7,8]
print(a[:2:-1],'asdsadsa')
if isinstance(i,list):
b.append(i)
        b.sort()
        print(b)
# a = list(set(a))
# print(a)
# print(a.set())#去重
# for i in a:
#     # for k in b:
#     if i not in b:
#         b.append(i)
#         b.sort()
#         print(b)

# for i in a:
#     # if isinstance(i,list):
#     # if i.isdigit():
#         # for k in:
#         print(i)
#         b.extend(i)
#         print(b)
# for k in b:
#     print(k)
