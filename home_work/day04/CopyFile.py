import os
import time


'''3.	实现文件的复制（三种方法实现文件复制：read()、readline()、readlines()。'''
# def copy_file(oldfilepathname,newfilepathname):
#     if os.path.exists(oldfilepathname):
#         rfp =open(oldfilepathname,'r')
#         wrtcontent =rfp.read()
#         rfp.close()
#
#         wfp =open(newfilepathname,'w')
#         wfp.write(wrtcontent)
#         wfp.close()


# def copy2_file(oldfilepathname,newfilepathname):
#     if os.path.exists(oldfilepathname):
#         rfp =open(oldfilepathname,'r')
#         wrtcontent =rfp.readlines()
#         print(wrtcontent,'wwwwww001')
#         rfp.close()
#
#         wfp =open(newfilepathname,'w')
#         for wrt in wrtcontent:
#             wfp.write(wrt)
#         wfp.close()

def copy3_file(oldfilepathname,newfilepathname):
    if os.path.exists(oldfilepathname):
        rfp =open(oldfilepathname,'r')
        wfp = open(newfilepathname,'w')
        content='abc'
        print(content)
        while content !='':
            time.sleep(2)
            content =rfp.readline()
            print(content)
            time.sleep(2)
            wfp.write(content)
        rfp.close()
        wfp.close()


copy3_file('test01.txt','test333.txt')