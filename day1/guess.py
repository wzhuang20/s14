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
else:
    print("you have tried too many times...fuck off!")