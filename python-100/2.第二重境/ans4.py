# 4. 爬取数据：爬取京东商品信息（网上很多资源，例如：https://www.jianshu.com/p/b2d288e67fa3）
# https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8
import requests
from lxml import etree
import time
import csv
# https://blog.csdn.net/qq_42750240/article/details/87890330
#定义函数抓取每页前30条商品信息
class jd:
    def crow_first(self,n,keyword):
        #构造每一页的url变化
        url=f'https://search.jd.com/Search?keyword={keyword}&enc=utf-8&page='+str(2*n-1)
        # print(url)
        head = {
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
                }
        r = requests.get(url, headers=head)
        r.encoding = r.apparent_encoding
        # print(r.text)
        # #指定编码方式，不然会出现乱码 
        html1 = etree.HTML(r.text)
        print(html1)
        # #定位到每一个商品标签li
        datas=html1.xpath('//li[contains(@class,"gl-item")]') 
        # print(datas)
        #将抓取的结果保存到本地CSV文件中
        with open('JD_Phone.csv','a',newline='',encoding='utf-8')as f:
            write=csv.writer(f)
            for data in datas:
                # 价格
                p_price = data.xpath('div/div[@class="p-price"]/strong/i/text()')
                # print(p_price)
                # 商店
                p_shop = data.xpath('div/div[7]/span/a/text()')
                # print(p_shop)
                # 商品名
                p_name = data.xpath('div/div[@class="p-name p-name-type-2"]/a/em/text()')
                # print(p_name)
                #这个if判断用来处理那些价格可以动态切换的商品，比如上文提到的小米MIX2，他们的价格位置在属性中放了一个最低价
                if len(p_price) == 0:
                    p_price = data.xpath('div/div[@class="p-price"]/strong/@data-price')
                    #xpath('string(.)')用来解析混夹在几个标签中的文本
                write.writerow([p_name[0],p_price[0],p_shop[0]])
        f.close()
    #定义函数抓取每页后30条商品信息
    # def crow_last(self,n,keyword):
    #     #获取当前的Unix时间戳，并且保留小数点后5位
    #     a=time.time()
    #     b='%.5f'%a
    #     print(b)
    #     url='https://search.jd.com/s_new.php?keyword={keyword}&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq={keyword}&cid2=653&cid3=655&page='+str(2*n)+'&s='+str(48*n-20)+'&scrolling=y&log_id='+str(b)
    #     head = {
    #        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
    #            }
    #     r = requests.get(url, headers=head)
    #     r.encoding = 'utf-8'
    #     html1 = etree.HTML(r.text)
    #     datas = html1.xpath('//li[contains(@class,"gl-item")]')
    #     with open('JD_Phone.csv','a',newline='',encoding='utf-8')as f:
    #         write=csv.writer(f)
    #         for data in datas:
    #             p_price = data.xpath('div/div[@class="p-price"]/strong/i/text()')
    #             p_shop = data.xpath('div/div[7]/span/a/text()')
    #             p_name = data.xpath('div/div[@class="p-name p-name-type-2"]/a/em/text()')
    #             if len(p_price) == 0:
    #                 p_price = data.xpath('div/div[@class="p-price"]/strong/@data-price')
    #             write.writerow([p_name[0].xpath('string(.)'),p_price[0],p_comment[0]])
    #     f.close()
 
 
if __name__=='__main__':
    for i in range(1,2):
        value = input("搜索商品：")
        jingdong = jd()
        jingdong.crow_first(i,value)
        
        # # try:
        # #     print('   Last_Page:   ' + str(i))
        # jingdong.crow_last(i,value)
        # #     print('   Finish')
        # # except Exception as e:
        # #     print(e)
