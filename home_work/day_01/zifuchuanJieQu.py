str = '0123456789'

print (str[0:])#截取字符串的全部字符
print (str[0:3]) #截取第一位到第三位的字符
print (str[:]) #截取字符串的全部字符
print (str[6:]) #截取第七个字符到结尾
print (str[:-3]) #截取从头开始到倒数第三个字符之前
print (str[2]) #截取第三个字符
print (str[-1]) #截取倒数第一个字符
print (str[::-1]) #创造一个与原字符串顺序相反的字符串
print (str[-3:-1])#截取倒数第三位与倒数第一位之前的字符
print (str[-3:])#截取倒数第三位到结尾
print (str[:-5:-3]) #逆序截取，具体啥意思没搞明白？
#[开始：结束：步进]开始结束都是数组的下标值（index）
'''定义字符串line='I am a beautiful girl'，变化为：girl beautiful a am I
进阶：如果句子尾端带有标点符号，例如I am a beautiful girl！带有叹号，则结果中的叹号也应该出现在句子的尾端girl beautiful a am I！
'''
line='I am a beautiful girl!'
# print(line[::-1])
l_add=line.strip().split(' ')
l_add1=l_add.reverse()
l_add2=l_add[::-1]
print(l_add,'第一次')
# print(''.join(l_add1))
print(l_add1,'第二次')
print(l_add2,'第三次')

content = 'I am a beautiful girl'
content1 = content.split ()
print(content1)
content1.reverse ()
print(content1,'1')
result = ' '.join ( content1 )
print ( result )
