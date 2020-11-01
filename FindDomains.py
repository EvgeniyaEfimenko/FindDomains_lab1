# Вариант 3
import re
with open('address.txt', 'r') as file:
    strf = file.readlines()
newfile = open('domains.txt', 'w+')
flag = False
a=[]
for i in range(len(strf)):
    res = re.findall(r'@(\w+.\w+)', strf[i])
    res_str = res[0]
    for i in range(len(a)):
         if res[0] == a[i]:
            flag = True
    if not flag:
        a.insert(len(a),res_str)
        newfile.writelines("%s\n" %res[0])
    flag = False

file.close()
newfile.close()