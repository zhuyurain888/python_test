
'''
利用collections库的Counter方法统计字符串每个单词出现的次数"kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h"
三种方法
'''

from collections import Counter
a="kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h"
res =Counter(a)
print(res)


#统计字符个数
# str=input("请输入一串字符:")
# 字典直接赋值
resoult={}
for i in a:
    resoult[i]=a.count(i)
    print(a.count(i),'《》《》《》《》《》',i)
print(resoult)

b =[]
# a =list(a)

for i in a:
    if i not in  b :
        b.append(i)
        print(b)
for j in b:
    print(j,':',a.count(j))

    # else:
    #     i +=1

# print(a)
