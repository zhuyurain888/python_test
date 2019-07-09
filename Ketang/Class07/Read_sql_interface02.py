import pymysql
import requests
import json

con = pymysql.connect(host ='47.103.115.192',port=3306,user ='prod',password ='GateonDmp9Prod!',db ='zhuyutest')

cor =con.cursor()
cor.execute("select * from python_interface")
# 返回多个元组，即返回多条记录(rows),如果没有结果,则返回 (cor.execute("select * from python_interface"))
a=cor.fetchall()


print(a)


for i in a:
    if i[0] == "post":
        response = requests.post(url=i[1],data=json.dumps(i[3]))
        try:
            success_result =response.json()["success"]
            if success_result == i[-1] :
                print("post接口成功")
            else:
                print(response.json())

            print(success_result)
        except:
            print("网络异常")

    if i[0] == "get":
        response =requests.post(url=i[1],data=json.dumps(i[2]))

        try:
            success_result = response.json()["success"]
            if success_result == i[-1]:
                print("get接口成功")
            else:
                print(response.json())

            print(success_result)
        except:
            print("网络异常")
cor.close()



























