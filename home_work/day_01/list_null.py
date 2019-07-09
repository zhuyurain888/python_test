'''义一个空列表，用于保存5个学生信息，一个学生信息包括三个属性：id、姓名、年龄
提示：列表元素是字典、向列表中添加数据用append()'''



lst=[]
lst.append("{'id': 1, 'name': '小明', 'age': 18, 'python_s': 78}")
lst.append("{'id': 2, 'name': '小花', 'age': 19, 'python_s': 88}")
lst.append("{'id': 2, 'name': '小聪', 'age': 20, 'python_s': 98}")
print(lst)

str1=input("请输入一个字符")
'''1.	从键盘上获取信息，判断是否可转换为数字，如果是，转换为整数。'''
try:
    if str1.isdigit():
        try:
            str1=int(str1)
            print(str1)
        except:
            print ( "请输入不是小数的字符" )
    else:
        print("不是数字")
except:
    print("请输入不是是小数的字符")
print(str1)