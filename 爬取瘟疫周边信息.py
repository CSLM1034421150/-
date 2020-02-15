from selenium import webdriver
from lxml import etree
import time
import datetime
from selenium.webdriver.common.keys import Keys
bai=str("\033[1;30m")
hong=str("\033[4;31m")
qing=str("\033[32m")
huang=str("\033[4;33m")
lan=str("\033[0;34m")
zi=str("\033[35m")
lv=str("\033[0;36m")
baik=str("\033[40m")
hongk=str("\033[1;41m")
qingk=str("\033[42m")
huangk=str("\033[43m")
lank=str("\033[44m")
zik=str("\033[45m")
lvk=str("\033[46m")
huik=str("\033[47m")
url='https://z.cbndata.com/2019-nCoV/index.html?from=timeline&isappinstalled=0'
#'https://z.cbndata.com/2019-nCoV/index.html?from=timeline&isappinstalled=0'
print(hong+">>>正在运行Python代码...\n>>>正在调用Chrome...")
try:
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    print(">>>成功调用谷歌浏览器...")
    # chrome = webdriver.Chrome("chromedriver")
    chrome = webdriver.Chrome(chrome_options=option)  # 隐藏浏览器
    print(">>>正在调试后台运行Chrome...")
    chrome.get(url)
    # chrome.find_element_by_xpath('//*[@id="page_body"]/div[2]/div[2]/a[2]').click()
    time.sleep(1)
    print(">>>正在定位您所在的位置...")
    htmls = etree.HTML(chrome.page_source)
    p1 = htmls.xpath('//*[@id="map"]/div[1]/div/div[2]/div/div[2]/div/div[1]/div/div/p[1]/text()')
    pids = htmls.xpath('//*[@id="map"]/div[1]/div/div[2]/div/div[2]/div/div[1]/div/div/p[1]/strong/text()')
    print(">>>瘟疫实时信息爬取成功...\n"+qing+">>>以下实时信息来自CBXDATA官网<<<")
    nowTime = datetime.datetime.now().strftime('%H:%M:%S')
    print(huang + '\n>>>WIFI定位周边疫情<<<', lan + '\n\n你所在的', hong + pids[0], lan + '目前已有', hong + pids[1],
          lan + '起新型冠状病毒肺炎确诊病例。\n离你最近的在', hong + pids[2], pids[3] + lan + " 米。\n只要做好自身防护，无需过分担心哦！")
    pt=htmls.xpath('//*[@id="map"]/div[1]/div/div[2]/div/div[2]/div/div[1]/div/div/p[4]/text()')
    print("\033[4;33m" +pt[0]+"\n"+hong+">>>您在"+nowTime+"信息成功爬取<<<")
    a = '你所在的', str(pids[0]), '目前已有', str(pids[1]), '起新型冠状病毒肺炎确诊病例。离你最近的在', str(pids[2]), str(pids[3]), str(
        "米。只要做好自身防护，无需过分担心哦！")
    #全国最新瘟疫数据获取
    url="http://sa.sogou.com/new-weball/page/sgs/epidemic?type_page=pcpop"
    chrome.get(url)
    htmls = etree.HTML(chrome.page_source)
    print("\033[0;33m\n"+"全国新型冠状病毒 肺炎疫情实时动态")
    p1 = htmls.xpath('//*[@id="async"]/div/div[1]/div[2]/div[1]/div[1]/ul/li[1]/em/text()')
    p2 = htmls.xpath('//*[@id="async"]/div/div[1]/div[2]/div[1]/div[1]/ul/li[2]/em/text()')
    p3 = htmls.xpath('//*[@id="async"]/div/div[1]/div[2]/div[1]/div[1]/ul/li[3]/em/text()')
    p4 = htmls.xpath('//*[@id="async"]/div/div[1]/div[2]/div[1]/div[1]/ul/li[4]/em/text()')
    p5 = htmls.xpath('//*[@id="async"]/div/div[1]/div[2]/div[1]/div[1]/ul/li[1]/span[2]/strong/span/text()')
    p6 = htmls.xpath('//*[@id="async"]/div/div[1]/div[2]/div[1]/div[1]/ul/li[2]/span/strong/span/text()')
    p7 = htmls.xpath('//*[@id="async"]/div/div[1]/div[2]/div[1]/div[1]/ul/li[3]/span[2]/strong/span/text()')
    p8 = htmls.xpath('//*[@id="async"]/div/div[1]/div[2]/div[1]/div[1]/ul/li[4]/span[2]/strong/span/text()')
    p9 = htmls.xpath('//*[@id="async"]/div/div[1]/div[2]/div[1]/div[1]/p/text()')
    print("确诊病例: "+p1[0]+"   昨日 ↑"+p5[0]+"\n"+"疑似病例: "+p2[0]+"    昨日 ↑"+p6[0]+"\n"+"治愈人数: "+p3[0]+"    昨日 ↑"+p7[0]+"\n"+"死亡人数: "+p4[0]+"    昨日 ↑"+p8[0]+"\n"+">>>"+p9[0]+"<<<")
    #最新新闻获取
    url="http://news.cctv.com/"
    chrome.get(url)
    htmls = etree.HTML(chrome.page_source)
    p1 = htmls.xpath('//*[@id="slide"]/div[1]/div[2]/h3/a/text()')
    p2 = htmls.xpath('//*[@id="slide"]/div[1]/div[2]/p/a/text()')
    p3 = htmls.xpath('//*[@id="slide"]/div[2]/div[2]/h3/a/text()')
    p4 = htmls.xpath('//*[@id="slide"]/div[2]/div[2]/p/a/text()')
    p5 = htmls.xpath('//*[@id="slide"]/div[3]/div[2]/h3/a/text()')
    p6 = htmls.xpath('//*[@id="slide"]/div[3]/div[2]/p/a/text()')
    print("\033[0;36m\n"+"最新瘟疫新闻:\n"+str(p1[0]))
    print(p2[0]+"\n")
    print(p3[0]+"\n"+p4[0]+"\n\n"+p5[0]+"\n"+p6[0])
    chrome.close()
except Exception as err:
    print(hongk+bai+">>>浏览器调用成功，信息爬取失败！The browser opened successfully, but the information retrieval failed!")
    print(huangk+"\033[1;36m"+">>>您可以重新尝试或检查URL: "+url+" 是否已更新！")
    chrome.close()
    quit()
