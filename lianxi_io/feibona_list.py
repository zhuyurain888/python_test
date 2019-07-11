def fib(n):
    a, b = 1, 1

    for i in range ( n - 1 ):
        a, b = b, a + b
        # a=b
        # b= a+b

        print (a, b, a + b )
    return a

#其实很简单， a, b = b, a+b 这个表达式的意思就是说，先计算=号的右边b的值，a+b的值，
# 算好了，然后再分别赋值给a 和b就可以了。





def fib1(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    fibs = [1, 1]
    for i in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs


# 输出前 10 个斐波那契数列
print(fib ( 10 ))
# 输出了第10个斐波那契数列
print(fib1 ( 10 ))