'''7.	请将s = 'aAsmr3idd4bgs7Dlsf9eAF'，字符串的数字取出，并输出成一个新的字符串'''

s = 'aAsmr3idd4bgs7Dlsf9eAF'
#字符串转化为列表
s_list=list(s)
print(s_list)
s_add=[]
i=0
for l in range(len(s_list)):
    if s_list[i].isdigit():
        s_add.append(s_list[i])
        print(s_list[i])
    i+=1

print(''.join(s_add))
