import requests
import re

lst=[1,2,3,4,5,6,7]
o=open('test.txt','a',encoding='utf-8')
for s in range(len(lst)):
    o.write(str(s)+'\n')
    print(s)


o.close()
with open('test.txt','r',encoding='utf-8') as f :
    # ff=f.read()
    # print(ff)
    pattern = re.compile("\w+")
    ss=pattern.findall(f.read())
    print(ss)


# f=open('test.txt','r',encoding='utf-8')
# ff=f.read()
# print(ff)
# pattern = re.compile("\d+")
# ss=pattern.findall(ff)
# print(ss)
# f.close()