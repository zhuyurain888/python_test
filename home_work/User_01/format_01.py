
# value = {"greet": "Hello world", "language": "Python"}
# # print("%(greet)s from %(language)s." % value)
#
# print("{} from {}".format(greet, language)

hash = {'name':'Bingo','age':18}
# print('my name is {name},age is {age}'.format(name='Bing1o',age=19))
print('my name is {},age is {}'.format('Bingo',19))

print('my name is {0},age is {1}'.format('Bingo',19))

print('my name is {name},age is {age}'.format(**hash))# 通过关键字，可用字典当关键字传入值时，在字典前加**即可