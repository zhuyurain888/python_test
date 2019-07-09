stds_list= [
{"id": 1, "name": "小明", "c_s": 85, "python_s": 78},
{"id": 2, "name": "小花", "c_s": 69, "python_s": 88},
{"id": 3, "name": "小东", "c_s": 79, "python_s": 83},
]
'''
1)	显示学生信息：“学生id：学生姓名：小明，C语言成绩：85, Python成绩：78”。
2)	修改“小明”的Python成绩为90
3)	删除“小东”的信息
'''

print(stds_list[0])
stds_list[0]["python_s"]=90
print(stds_list,"修改之后的")
del stds_list[2]
print(stds_list,"删除之后的")
