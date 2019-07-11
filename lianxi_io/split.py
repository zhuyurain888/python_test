import re
n =[]
a="not 404 fonud 张三，100 深圳"
list =a.split(" ")#转数组
s= '' .join(list)#转字符串
print('字符串S:%s'%(s))
for z in s:
    # print(z)
    n.append(z)#加到一个新的数组
print('n是个新的数组[]:',n)

sn =''.join(n)#转字符串
print('字符串Sn:%s'%(sn))

res =re.findall('[0-9]|[，a-zA-Z]|[a-zA-Z]*',sn)
print(res,'r')
for i in res:
    # print(i)
    if i in n:
        n.remove(i)

print(n)
