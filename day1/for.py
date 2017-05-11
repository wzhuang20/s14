oldboy = 56
for i in range(3):
    age = int(input("input age: "))
    if age == oldboy:
        print("yes,you got it")
        break
    elif age > oldboy:
        print("think,smaller...")
    else:
        print("think bigger!")
else:
    print("you have tried too many times...fuck off!")