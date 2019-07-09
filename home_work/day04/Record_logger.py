import time
import os
'''4.	向日志文件存储数据。日志文件中存储的数据如下：
      ID year-month-day hour:mintue:second
1) 若日志文件不存在则id从1开始，每隔一秒向文件写入一条信息并且向屏幕显示数据
2) 若日志文件已经存在则本次运行程序写入的内容中id值应该累加
第一次运行：
    1  2019-04-20  10:10:20
    2  2019-04-20  10:10:21
第二次运行：
    3  2019-04-20  10:20:19
    4  2019-04-20  10:20:20
'''
def record_logger(logfilepath,id):
    wrfp =open(logfilepath,'a',buffering=1)
    # while True:
    for _ in range(10):
        record_content =str(id)+''+time.strtime("%Y %m %d %H:%M:%S")+'\n'
        print(record_content)
        wrfp.write(record_content)
        time.sleep(1)
        id+=1
        wrfp.close()

class Logger(object):
    def __init__(self):
        today=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
        if not os.path.exists(LOGGER_DIRPARH):
            os.mkdir(LOGGER_DIRPARH)
            self.log_file_path =os.path.join(LOGGER_DIRPARH,'log_'+today+'.log')

    def get_logger(self):
        if not os.path.exists(self.log_file_path):
            id = 1
            record_logger(self.log_file_path, id)
        else:
            lgrdfp = open(self.log_file_path, 'r')
            idlist = lgrdfp.readlines()
            lgrdfp.close()
            id = int(idlist[len(idlist) - 1].split(' ')[0]) + 1

            record_logger(self.log_file_path, id)

if __name__ =='__main__':
    record_logger('D:/mengbaige_python/home_work/day04/','1')