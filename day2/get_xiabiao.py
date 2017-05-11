merchandise_list = [
    ('iphone', 7200),
    ('basketball', 240),
    ('banana', 20),
    ('beer', 110),
    ('shoe', 560),
    ('television', 5500),
    ('bed', 3900),
    ('watch', 12000),
]

subscript = input("请输入下标：")
if subscript.isdigit():
    subscript = int(subscript)
kkk = merchandise_list[subscript]

print(kkk)
