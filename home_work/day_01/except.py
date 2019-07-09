def func(a, b):
    try:
        chu =a/b
        print(chu)
    except ZeroDivisionError:
        print("被除数不能为：0")
    except BaseException:
        print ( "其他异常" )
    else:
        print("如果没有异常执行这块代码")
if __name__ == '__main__':

    func(1,1)
