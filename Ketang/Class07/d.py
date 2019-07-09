d ={"cc":"11"}

k = input("请输入一个key")
v =input("请输入一个value")

d.update(dict({k:v}))
s=d
print(type({k:v}))

print(s)


#
# d = {}
# a = input("请输入姓名：")
# b = input("请输入：")
# # d.update({a:b})
# d.update(dict({a: b}))
# dd = d
# print(dd)
# print(type({a: b}))




# d[k]=v
# print(d)
# d[k]=2
# print(d)