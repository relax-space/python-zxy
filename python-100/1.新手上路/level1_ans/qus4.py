# 问题4
# 定义一个至少具有两个方法的类：getString：从控制台输入获取字符串 printString：以大写形式输出字符串。还请包括简单的测试功能来测试类方法。

# 提示：
# 使用__init__方法构造一些​​参数

class aaa(object):
    def __init__(self):
        self.n = ""
    def getString(self):
        self.n = input("输入字符串：")
    def printString(self):
        print('大写形式：',self.n.upper())
str = aaa()
str.getString()
str.printString()
        

