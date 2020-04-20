# 3. 正则匹配：从这个地址中取出fruits,地址可能是 /v1/fruits?name=1，或者/v1/fruits/1,或者/v1/fruits

import re

def fetch(contents):
    f = re.findall(r'/v1/(.+?)(\?|\/|$)',contents)
    # print(f)
    return f[0][0]


print(fetch("/v1/fruits?name=1"))
print(fetch("/v1/fruits/1"))
print(fetch("/v1/fruits"))
