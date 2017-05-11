inname = "kaka"
inpassword = "123456"
count = 0
for i in range(3):
    name = input("please input username ")
    password = input("please input password ")
    if inname == name and inpassword == password:
        print("welcome!")
        break
    elif inname != name or inpassword != password:
        print("input error!")

else:
    print("input thrice error! 将被冻结 ")

