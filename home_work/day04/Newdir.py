import os
def rename_file(oldfilepath,newname):
    if os.path.exists(oldfilepath):
        try :
            newfilepath =os.path.join(os.path.dirname(os.path.abspath(oldfilepath)),newname)
            print(newfilepath,'abcd')

            print(oldfilepath,newname)

            os.rename(oldfilepath,newfilepath)
        except:
            print('出错了！')
        else:
            print('文件路径不存在')

rename_file('test01','test01')
b='abc/bbb'

tts =os.path.join(os.path.dirname(os.path.abspath('test01')),'Ketang')
print(tts)
print(os.getcwd())#获取文件的当前目录