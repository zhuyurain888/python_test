f =open('test.txt','r',encoding='utf-8')
print(f.name)
# print(f.flush())
# f.truncate()

'''历遍文件'''
# print(f.readlines(),'as')

for line in f.readlines():                          #依次读取每行
    line = line.strip()                             #去掉每行头尾空白
    f.flush()                                       # 刷新缓冲区
    print ("读取的数据为: %s" % (line))



# a=f.readlines()
# b=f.readlines()
# print(b)
# print(f.tell(),'kkk')
# print(f.seek(4))
# num=0
# for i in f.readlines():
#     num+=1
#     if num==100:
#         i=''.join([i.strip(),'iii'])
#         # ''.join()：    连接字符串数组。将字符串、元组、列表中的元素以指定的字符(分隔符)连接生成一个新的字符串
#     print(i)


f.close()