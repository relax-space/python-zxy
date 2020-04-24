# 5. 爬取数据：爬取自己账号下的，dooray 担当业务箱的内容


import requests
class DorDownloader:
    
    def fetchPost(self,sessionId):
        url =f"https://pangpang.dooray.com/v2/wapi/projects/*/posts?order=-createdAt&toMemberIds=2444924209700626009" 
        cookies_jar = requests.cookies.RequestsCookieJar()
        cookies_jar.set('SESSION', sessionId, domain='.dooray.com', path='/')
        # print(cookies_jar)
        resp = requests.get(url,cookies=cookies_jar)
        post = resp.json()
        totalCount = post["result"]["totalCount"]
        #问题：仅返回20条数据
        for i in range(0,20):
            contents = post["result"]["contents"][i]["subject"] # result.contents[""0""].subject
            print(contents)
        


if __name__ == "__main__":
    # stackprinter.set_excepthook()
    sessionId = input("请输入dooray的sessionId：")
    m = DorDownloader()
    m.fetchPost(sessionId)