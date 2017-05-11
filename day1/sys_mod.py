'''import os
cmd_res = os.system("dir")
print(cmd_res)'''

import os

names = ["huocheng","shenqiwei","liufeng","liufeng"]
names2 = [1,2,3]
names.append("wangz")
names.insert(2,"madanyang")
names[2] = "daxue"
#names.remove("liufeng")
#del names[3]
#names.pop()
names.extend(names2)
names.reverse()
print (names)