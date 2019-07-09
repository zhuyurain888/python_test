#!/usr/bin/env python
#-*- coding:utf-8 -*-

import requests
import time
import threading

# 配置:模拟运行状态
THREAD_NUM = 40        	   # 并发线程总数
ONE_WORKER_NUM = 50        # 每个线程的循环次数
LOOP_SLEEP = 0.1           # 每次请求时间间隔(秒)

# 出错数
ERROR_NUM = 0

login_url = 'https://ds.gateon.com/sys/sysUser/login'
press_url = 'http://companytest.mengbaige.com/#/campaign-index'

def login(loging_url,count=0):
    '''登陆函数，用户登陆后才能请求到里面的页面内容'''
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    }
    session = requests.Session()
    session.headers = headers
    try:
        res = session.post(loging_url,data={'t': int(time.time() * 1000), 'userName': "18627990953", 'passWord': "123456m"})
    except Exception as e:
        count += 1
        login(loging_url,count=count)
        if count >= 4:
            exit(1)
    return session

def doWork(index,press_url=press_url,session=login(login_url)):
    '''具体的处理函数，负责处理单个任务'''
    t = threading.currentThread()
    try:
        html = session.get(press_url).content.decode('utf-8')
    except Exception as e:
        print(e)
        global ERROR_NUM
        ERROR_NUM += 1

def working():
    t = threading.currentThread()
    i = 0
    while i < ONE_WORKER_NUM:
        i += 1
        doWork(i)
        time.sleep(LOOP_SLEEP)

def main():
    '''主要处理函数的逻辑'''
    t1 = time.time()
    Threads = []
    # 创建线程
    for i in range(THREAD_NUM):
        t = threading.Thread(target=working,name="T"+str(i))
        t.setDaemon(True)
        Threads.append(t)

    for t in Threads:
        t.start()
    for t in Threads:
        t.join()
    t2 = time.time()

    print( "========================================" )
    print( "URL:", press_url)
    print( "任务数量:", THREAD_NUM, "*", ONE_WORKER_NUM, "=", THREAD_NUM*ONE_WORKER_NUM )
    print( "总耗时(秒):", t2-t1 )
    print( "每次请求耗时(秒):", (t2-t1) / (THREAD_NUM*ONE_WORKER_NUM) )
    print( "每秒承载请求数:", 1 / ((t2-t1) / (THREAD_NUM*ONE_WORKER_NUM)) )
    print( "错误数量:", ERROR_NUM )

if __name__ == "__main__":
    main()

