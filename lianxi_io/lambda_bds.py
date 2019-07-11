'''字典根据键从小到大排序dict={"name":"zs","age":18,"city":"深圳","tel":"1362626627"}'''
dict={"name":"zs","age":18,"city":"深圳","tel":"1362626627"}
# 获取已经排序的字典，返回是数组
print(dict['age'])
list =sorted(dict.items())
print(list)
# print(list[0])
# print(list[0][1])
# s=list[0][0]
# print(type(s))
# print(dict[s])
print(type(len(list)))
print(type(list))
print(len(list))
for k in range(len(list)):
    print(k)
    print(dict[list[k][0]])





# list1 =sorted(dict.items(),key=lambda i:i[0],reverse=False)
# print(list1)
# new_dict={}
# for i in list:
#     print(i[0],":",i[1])
#
#     new_dict[i[0]]=i[1]
# print("新字典",new_dict)