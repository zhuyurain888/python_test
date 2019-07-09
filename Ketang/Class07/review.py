# url = "http://39.107.96.138:3000/api/v1/topics"
#
# import requests
#
# response = requests.get(url, params={"page": 2})
# response2 = requests.get(url+'?page=2')
#
# if response.status_code == 200:
#     print("ok")
# else:
#     print("网络访问异常")
#
#
# response = requests.post(url, data={"tab": "ask", "accesstoken": "d807b298-576d-47f4-8849-0c5052cc049c", "title": "I am IRON MAN", "content": "hello erveryone"})
# if response.status_code == 200:
#     print(response.text)
# else:
#     print("网络访问异常")
#
#
#
# import re
# pattern = re.compile('"topic_id":"(\w+)"')
# result = pattern.findall(response.text)
# print(result)
#
# # 匹配字符的
# # 代表匹配所有的字符   .
# # 代表匹配所有的字母，数字和_      \w        (\W代表的是\w取不到的所有值)
# # 代表匹配所有数字                 \d        (\D代表的是\d取不到的所有值)
# #
# #
# # 匹配位数的
# # *  0位或者很多位
# # +  1位或者很多位
# name = "John,john,tohn,pohn,cohn,kohn"
# pattern = re.compile('[Jj]ohn')
# result = pattern.findall(name)
# print(result)
#
# http = "http://www.baidu.com, https://www.sougou.com, httpss://www.kkk.com"
# pattern = re.compile('https{0,2}')
# result = pattern.findall(http)
# print(result)
# # [] 代表匹配一位中括号里面的内容
#
# # {} 代表匹配它前面那个字符的次数 {m,n} {,n}{m,}
#
#
with open("a.html", 'r') as f :
    content = f.read()
    # print(content)
    # pattern = re.compile('<[tT][iI][Tt][Ll][Ee]>.*([hH].+[Dd]).*</[tT][iI][Tt][Ll][Ee]>', re.S)
    pattern = re.compile("[Hh][Ee][Ll][Ll][Oo].[Ww][oO][Rr][Ll][Dd]")
    result = pattern.findall(content)
    print(result)