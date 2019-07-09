
'''定义一个函数read_file(f)，参数为文件对象，在函数中读取文件内容，
若读到的某行信息中包含error字符串时，抛出异常。在程序主流程中捕捉并处理该异常。'''
try:
    with open('new_file.txt','r',encoding='utf-8') as f:
        i=0
        for l in f.readlines():
            i += 1
            print("读取的数据为: %s" % (l))
            l = l.strip()  # 去掉每行头尾空白
            if 'error' in l:

                print('当前行有误！%d'%(i))
                exit()
        f.flush()  # 刷新缓冲区
except:
    print("文件不存在的“error”")


# def read_file(f: object) -> object:
#     try:
#         with open(f, 'r',encoding='utf-8') as fp:
#             temp_readline = fp.readlines()
#         fp.close()
#         for i in range(0, len(temp_readline)):
#             if 'error' in temp_readline[i]:
#                 raise AssertionError('此行中出现错误！行数为第{}行'.format(i + 1))
#
#
#     except (FileNotFoundError, FileExistsError):
#         print('文件不存在错误')
# # if __name__ == '__main__':
# read_file('new_file.txt')