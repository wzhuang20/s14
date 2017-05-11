import sys,os

merchandise_list = [
    ('iphone',7200),
    ('basketball',240),
    ('banana',20),
    ('beer',110),
    ('shoe',560),
    ('television',5500),
    ('bed',3900),
    ('watch',12000),
]

salary = input("请输入薪水：")

if salary.isdigit():
    while True:
        for index,i in enumerate(merchandise_list):
            print(index,i)
        user_choice = input("请输入需要购买的商品：")
        if user_choice < len(merchandise_list) and user_choice >= 0:
            p_choice = merchandise_list[user_choice]
            if p_choice[1]

        else:("输入不正确")


        break



elif salary == 'q':
    print("谢谢，再见")

else:
    print("请输入数字")



