'''
2.	输入一行字符,统计其中有多少个单词，每两个单词之间以空格隔开。如输入: This is a Python program. 输出：There are 5 words in the line
3.	计算字符串最后一个单词的长度，单词以空格隔开。（使用input()输入一个句子）
4.	从键盘输入一句话，输入的信息两端有空白字符。“  Life is short, you need python!   ”除去两端的空白字符，查找其中的python，将其替换为python3。
'''
#2
# Word = 1
# lstr=input("请输入一段英文语句:")
#
# for l in lstr:
#     if l.isspace() :
#         Word +=1
# print("There are %s words in the line"% (Word) )

#3
s_list1 = input("请输入一段英文语句:")
def lengthOfLastWord(s: str) -> int:
    s_list = s.strip().split(' ')#strip()是除去字符串前后的空格或换行,split('')方法切片返回的是一个数组
    print(s_list)
    print(s_list[-1].isalpha())
    if s_list[-1].isalpha() == False:

        print(s_list1,'12121')
        return 0
    return len(s_list[-1])

res=lengthOfLastWord(s_list1)
print(res)
#4
# s_list2 = input("请输入一段英文语句:")
# def lengthOfLastWord2(s: str) -> int:
#     s_list = s.strip().split(' ')#strip()是除去字符串前后的空格或换行
#     print(s_list)
#     if s_list[-1].isalpha() == True:
#
#         s_list[-1]='python3'
#     return s_list[-1]
#
# res=lengthOfLastWord2(s_list2)
# print(res)
