import io
import os

# str = input("请输入：")
# print ("你输入的内容是: ", str)

# 打开一个文件
fo = open("tt.txt", "w")
print( "文件名: ", fo.name)
print ("是否已关闭 : ", fo.closed)
print ("访问模式 : ", fo.mode)
# print ("末尾是否强制加空格 : ", fo.softspace)
# fo.close()

fo.write ( "www.runoob.com!\nVery good site!\n" )
fo.close()
fo = open("tt.txt", "w+")
str = fo.read()

print("读取的字符串是 : ", str)

print("问件的当前位置：",fo.tell)
fo.close()


# print("问件的当前位置：",fo.tell())
fo = open("tt.txt", "w+")
position = fo.seek(0, 0)
str = fo.read(10)
print ("重新读取字符串 : ", str)
# 关闭打开的文件
fo.close()

print("显示当前工作目录 : ",os.getcwd())
