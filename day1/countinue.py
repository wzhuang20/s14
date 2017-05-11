oldboy = 56
count = 0
while count<3:
    age = int(input("input age: "))
    if age == oldboy:
        print("yes,you got it")
        break
    elif age > oldboy:
        print("think,smaller...")
    else:
        print("think bigger!")
    count +=1
    if count == 3:  # count+=1后此时count=3
        countinue_confim = input("do you want to keep gurssing..?")
        if countinue_confim != "n":
            count = 0  # 如果不是n，则使count归零，从而继续循环。
