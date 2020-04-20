# 问题10
# 编写一个接受句子并计算字母和数字数量的程序。
# 假设将以下输入提供给程序：
# hello world! 123
# Then, the output should be:
# 字母10
# 数字3

# 提示：
# 如果将输入数据提供给问题，则应假定它是控制台输入。
# coding=utf-8
num_count = 0
alp_count = 0
s= input("请输入句子：")
# print(type(s))
for i in s:
    # print(i)
    if i.isalpha():
        alp_count += 1
    elif i.isdigit():
        num_count +=1

print("字母：",alp_count,"数字：",num_count)



        
    
