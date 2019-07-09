import pymysql
import requests
import json

con =pymysql.connect(host='47.103.115.192',port=3306,user='prod',password='GateonDmp9Prod!',db ='zhuyutest')
cor =con.cursor()
cor.execute("select * from python_interface")

# cor.execute('select * from tabletest')s
a =cor.fetchall()
b=cor.fetchone()
print(b,'123')
print(a)
print(type(a))
for i in a:
    if i[0] == "post":
        response = requests.post(url=i[1], data=json.dumps(i[3]))
        print(response)
        try:
            success_result = str(response.json()["success"])
            if success_result == i[-1]:
                print("post接口测试成功")
            else:
                print(response.json())
        except:
            print("网络异常")

    if i[0] == 'get':
        response = requests.get(url=i[1], params=json.dumps(i[2]))
        try:
            success_result = str(response.json()["success"])
            if success_result == i[-1]:
                print("get接口测试成功")
            else:
                print("get接口测试失败，结果有问题:",response.json())
        except:
            print("网络异常")
con.close()