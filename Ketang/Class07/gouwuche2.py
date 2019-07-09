product_list=[
    ('Mac',9000),
    ('kindle',800),
    ('tesla',900000),
    ('python book',105),
    ('bike',2000),

]
choice_goods_car=[]
choice_goods_car_cf={}

saved_money= input('请输入你的金额！')
if saved_money.isdigit():
    saved_money=int(saved_money)
#     遍历这个数组的元组
for k,v in enumerate(product_list,1):
    print(k,'>>>>>>>',v)


while True:

    # 引导用户选择商品
    choice = input('选择购买商品编号[退出：q]：')

    if choice.isdigit():
        choice = int(choice)
        # 判断是否在商品的最大值
        if choice > 0 and choice <= len(product_list):
            # 打印选择的商品
            print(product_list[choice-1])
            # 判断你的余额是否能够支付起这个商品
            if saved_money >= product_list[choice-1][1]:
                choice_goods_car.append(product_list[choice - 1])

                # 当前的购物车商品
                print('当前的购物车商品',choice_goods_car)
                # 当前的购物车选中的商品数量
                currenr_goods_count =choice_goods_car.count(product_list[choice - 1])
                print('当前商品的数据是：',currenr_goods_count,"当前选择的商品是",product_list[choice - 1])
                k =currenr_goods_count
                v=product_list[choice - 1]
                # choice_goods_car_cf [v]= k

                choice_goods_car_cf.update({v: k})

                print(choice_goods_car_cf,'111111111111')
                # 用序列解包的方法遍历字典中的元素，输出的样式有所变化
                for keys, values in choice_goods_car_cf.items():
                    print(keys, values)

                # print(choice_goods_car_cf11.items())

                # 去除购物车重复的商品

                choice_goods_car_quchong=list(set(choice_goods_car))

                # 支付后剩余的余额

                saved_money -=product_list[choice-1][1]
                print('你当前的余额是：%d'%(saved_money))
            else:
                print('你的余额不足%d'%(saved_money))
                print('你当前的购物车的商品是：',"...............")
                print(choice_goods_car)

    elif choice =='q' or choice =='Q':
        print('你当前的购物车的商品是：')
        print("==========>",choice_goods_car)
        print("<========",choice_goods_car_cf)

        # 用序列解包的方法遍历字典中的元素，输出的样式有所变化
        for keys, values in choice_goods_car_cf.items():
            print(keys, values)
        print(choice_goods_car_quchong)
        break
    else:
        print('请输入正确的商品选项！')








