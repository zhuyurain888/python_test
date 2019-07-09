def inp(filename):
    while True:
        str =input('请输入一段英文字母！')

        if str == 'exit':
            break
        else:
            with open(filename,'a',encoding='utf-8') as f:
                strda = str.upper()
                print(strda)
                f.write(strda+'\n')
def readd (filename):
    with open(filename, 'r', encoding='utf-8') as ff:
        print(ff.readlines())

inp('test02.txt')
readd('test02.txt')
