menu = {
    '北京':{
        '海淀':{
            '五道口':{
                'soho':{},
                '网易':{},
                'google':{}
            },
            '中关村':{
                '爱奇艺':{},
                '汽车之家':{},
                'youku':{},
            },
            '上地':{
                '百度':{},
            },
        },
        '昌平':{
            '沙河':{
                '老男孩':{},
                '北航':{},
            },
            '天通苑':{},
            '回龙观':{},
        },
        '朝阳':{},
        '东城':{},
    },
    '上海':{
        '闵行':{
            "人民广场":{
                '炸鸡店':{}
            }
        },
        '闸北':{
            '火车战':{
                '携程':{}
            }
        },
        '浦东':{},
    },
    '山东':{},
}



current_layer = menu #实现动态循环
parent_layers = [] #保存所有父级，最后一个元素永远都是父级
while True:
    for k in current_layer:
        print(k)
    choice = input(">>:").strip()
    # if len(choice) ==0 :continue
    if choice in current_layer:
        #在进入下一层之前，把当前层（也即是下一层父级）追加到下一次loop(循环）,
        #当前用户选择B的选择，就可以直接取列表的最后一个值就ok了
        print(parent_layers,'00000')
        parent_layers.append(current_layer)
        print(parent_layers,'111')
        print(current_layer,'当前层前')
        current_layer = current_layer[choice] #修改成了子层
        # print(current_layer[choice])
        print(current_layer, '当前层后')
    elif choice == "b":
        if parent_layers:
            #取出列表的最后一个值，因为他就是当前层的父级
            current_layer = parent_layers.pop()
            print(current_layer, 'dddel')
    elif choice == "q":
        break
    else:
        print("无此项")




'''
exit_flag = False
current_layer = menu

layers = [menu]

while not  exit_flag:
    for k in current_layer:
        print(k)
    choice = input(">>:").strip()
    if choice == "b":
        current_layer = layers[-1]
        #print("change to laster", current_layer)
        layers.pop()
    elif choice not  in current_layer:continue
    else:
        layers.append(current_layer)
        current_layer = current_layer[choice]
'''