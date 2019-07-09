import requests
def get_result(url):
    response = requests.get(url)
    res = response.json()
    print(res)
    result = res["data"]["id"]
    # print(result)
    return result

# a = {'result': True, 'message': '', 'data': {'id': 6}}
# print(a["data"]["id"])
lst =[]
l=[1,2,3,4,5,6,100]
for _ in range(100):



    res =get_result("http://api.ceshi.hahohi.com/api/app/v1/draw?source=html")
    # print(assertIn(res,l))
    lst.append(res)
    print(lst)
print(lst)
a=lst.count(1)
b=lst.count(2)
c=lst.count(3)
d=lst.count(4)
e=lst.count(5)
f=lst.count(6)
g=lst.count(100)

print(str(a)+'%')
print(str(b)+'%')
print(str(c)+'%')
print(str(d)+'%')
print(str(e)+'%')
print(str(f)+'%')
print(str(g)+'%')
#
# with open("douban.html",'w',encoding='utf-8') as f:
#     f.write(res.json())
