# 问题6
# 编写一个程序，根据给定的公式计算并打印值：Q = [（2 * C * D）/ H]的平方根
# 以下是C和H的固定值：C为50。H为30。D是变量，其值应以逗号分隔的顺序输入到程序中。
# 例
# 让我们假设以下逗号分隔的输入序列已赋予程序：100,150,180
# 该程序的输出应为：18,22,24

# 提示：
# 如果收到的输出为十进制格式，则应四舍五入至最接近的值（例如，如果收到的输出为26.0，
# 则应将其打印为26）。
# 如果将输入数据提供给问题，则应假定它是控制台输入。
import math
a = input("输入d:")
b = a.split(',')
for i in b:
    d = int(i)
    c=50
    h=30
    q=math.sqrt((2*c*d)/h)
    print(int(q))
