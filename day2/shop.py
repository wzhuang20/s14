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
shopping_list = []
salary = input("please input your salary: ")
if salary.isdigit():
    salary = int(salary)
    while True:
        for index,i in enumerate(merchandise_list):
            print(index,i)
        user_choice = input("select merchandise >: ")
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice < len(merchandise_list) and user_choice>= 0:
                p_i = merchandise_list[user_choice]
                if p_i[1] <= salary:
                    shopping_list.append(p_i)
                    salary -= p_i[1]
                    print("\033[31;1m%s\033[0m添加入购物车，您的余额为\033[31;1m%s\033[0m" % (p_i[0], salary))
                else:
                    print("\033[41;2m您的余额只剩%s\033[0m" % salary)
            else:
                print("商品不存在,请重新选择")

        elif user_choice == 'q':
            print("-----以下是您购买的商品,谢谢，再见-----")
            for p in shopping_list:
                print(p)
            sys.exit()
elif salary == 'q':
    print("欢迎您下次光临，再见")
else:
    print('invalid option!')






