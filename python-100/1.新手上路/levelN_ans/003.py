# 实例003：调用函数
# 题目 练习函数调用。


def hello():
    print('Hello World!')
def helloAgain():
    for i in range(2):
        hello()

if __name__=='__main__':
    helloAgain()
