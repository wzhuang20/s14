data = {
    '北京':{
        "昌平":{
            "沙河":["oldboy","test"],
            "天通苑":["链家地产","我爱我家"]
        },
        "朝阳":{
            "望京":["奔驰","陌陌"],
            "国贸":{"CICC","HP"},
            "东直门":{"Advent","飞信"},
        },
        "海淀":{},
    },
    '山东':{
        "德州":{},
        "青岛":{},
        "济南":{}
    },
    '广东':{
        "东莞":{},
        "常熟":{},
        "佛山":{},
    },
}

exit_flag = False

while not exit_flag:
    for i in data:
        print(i)
    choice = input("选择进入1>>: ")
    if choice in data:
        while not exit_flag:
            for i2 in data[choice]:
                print(i2)
            choice2 = input("选择进入2>>: ")
            if choice2 in data[choice]:
                while not exit_flag:
                    for i3 in data[choice][choice2]:
                        print(i3)
                    choice3 = input("选择进入3>>: ")
                    if choice3 in data[choice][choice2]:
                        while not exit_flag:
                            for i4 in data[choice][choice2][choice3]:
                                print(i4)
                            choice4 = input("已是最后一层，按b返回>>: ")
                            if choice4 == "b":
                                break
                    if choice3 == "b":
                        break
            if choice2 == "b":
                break
    if choice == "b":
        print("已经是第一层")








