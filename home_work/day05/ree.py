import requests
import re

pattern = re.compile(r'\d+')  # 查找数字
result1 = pattern.findall('runoob 123 google 456')
result2 = pattern.findall('run88oob123google456', 0, 10)

print(result1)
print(result2)



a = "2n3r238y7@&#T&RF5D##N^&Dver*235X@eg(*XY@D^T6534@X^@FX*^F@S<@NXH"
a='348580620@qq.com'
# pattern  = re.compile('\w*？')
pattern  = re.compile("\w+@\w+\.com")
result = pattern.findall(a)
print(result)


# res = requests.get("http://api.ceshi.hahohi.com/api/app/v1/draw?source=html")
# print(res.json())
# with open("douban.html",'w',encoding='utf-8') as f:
# f.write(result)

# with open(r'C:\Users\Dell\Desktop\learn_python\douban.html','r',encoding='utf-8') as f:
# a = f.read()
# # print(a)
# pattern = re.compile('<li ><a href="(https*://\w+\.\w+\.\w+/.+)"')
# result = pattern.findall(a)
response = requests.get("https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=&start=0").json()

print(response,'打印1')

with open('aa.txt','a',encoding='utf8') as f:

    for i in response['data']:#response['data']，遍历字典中的数组{'data':[{a:1,b:2,c:3}]}
        f.write(i['url'] + '\n')
        print("222",i['url'])

with open ( 'aa.txt', 'r', encoding='utf-8' ) as ff:
    # pattern = re.compile ( 'href="https://\w+\.\w+\.\w+.*?"' )
    pattern = re.compile ( 'https://movie.douban.com/subject/\d+/')
    ss=pattern.findall(ff.read())
    for l in ss:
        print(str(l))
        if l =='https://movie.douban.com/subject/23232876/':

            print('True',l)
        else:
            pass

    print(ss,'3333')

    # for line in ff.readlines():
    #     print("111111111111111")
    #     if line =='https://movie.douban.com/subject/23232876/':
    #         print('True')
    #     else:
    #         pass






exit(1)
result = pattern.findall(response.text)
print(result,'哈哈哈\n')
str ='https://music.douban.com'
for i in result:
    print(i)
    if i == str :
        print(i,'sadasd')
        response = requests.get(i)
        print(response)
y = open("chart1.html","w",encoding="utf-8")
y.write(response.text)
y.close()


with open("chart1.html","r",encoding="utf-8") as f:


    pattern1 = re.compile('https://movie.douban.com/subject/\d+/', re.S)
    result1 = pattern1.findall(f.read())
    print(result1)

# import re
# a = "2533450204@qq.com"
# pattern = re.compile("(\w+)@\w+\.com")
# result = pattern.findall(a)
# print(result)
