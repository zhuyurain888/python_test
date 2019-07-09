str_1='大王叫我来巡山，抓个和尚做晚餐'
#[开始：结束：步进]开始结束都是数组的下标值（index）
print(str_1[::-2])
print(str_1[::-1])
print(str_1[3:0:-1])
print(str_1[3:1:-1])
print(str_1[3:2:-1])


str_2='大王叫我来巡山，抓个和尚做晚餐'
#将字符串转换为list列表
lst=list(str_2)
#对列表进行反转操作,reverse()返回为None
lst.reverse()
print(''.join(lst))


str_3 ='一分辛苦一份才'
i= len(str_3)-1


str_list=[]
for s in range(len(str_3)):
    print(str_3[i])
    str_list.append(str_3[i])
    i-=1
print(str_list)
print('***'.join(str_list))#拼接字符串


str_4 = '如果人人都献出一点爱,世界将变成美好的人间'
i = len(str_4) - 1
str_list1 = []
while(i >= 0):
    str_list1.append(str_4[i])

    i = i - 1
print(''.join(str_list1))

