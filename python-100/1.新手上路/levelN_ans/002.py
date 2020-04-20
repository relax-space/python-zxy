# 实例002：字符串构成
# 题目 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。

# 程序分析 利用 while 或 for 语句,条件为输入的字符不为 ‘\n’。


s = input("请输入一行字符：")
alpnum = 0
dignum = 0
spanum = 0
othnum = 0
for i in s:
    # print(i)
    if i.isalpha():
        alpnum +=1
    elif i.isdigit():
        dignum +=1
    elif i.isspace():
        spanum +=1
    else:
        othnum +=1

print("字母：",alpnum)
print("数字：",dignum)
print("空格：",spanum)
print("其他：",othnum)
    


















# string=input("输入字符串：")
# alp=0
# num=0
# spa=0
# oth=0
# for i in range(len(string)):
#     if string[i].isspace():
#         spa+=1
#     elif string[i].isdigit():
#         num+=1
#     elif string[i].isalpha():
#         alp+=1
#     else:
#         oth+=1
# print('space: ',spa)
# print('digit: ',num)
# print('alpha: ',alp)
# print('other: ',oth)