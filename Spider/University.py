import requests
from bs4 import BeautifulSoup
import bs4

#爬取相应url
def getHTMLText(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return ""

#解析HTML文件并填充
def fillUnivList(ulist,html):
    soup=BeautifulSoup(html,"html.parser")
    for tr in soup.find('tbody').children:          #soup.find方法，只找到第一个符合条件的标签
        if isinstance(tr,bs4.element.Tag):          #isinstance判断tr标签是否为Tag类型
            tds=tr('td')                            #此处为简写形式，实为find_all方法
            ulist.append([tds[0].string,tds[1].string,tds[2].string])            
    pass

#打印大学列表函数
def printUnivList(ulist,num):
    tplt="{0:^10}\t{1:{3}^10}\t{2:^10}"
    print(tplt.format("排名","大学名称","成绩",chr(12288)))
    for i in range(num):
        u=ulist[i]
        print(tplt.format(u[0],u[1],u[2],chr(12288)))



def main():
    uinfo=[]
    url='http://www.zuihaodaxue.com/zuihaodaxuepaiming2016.html'
    html=getHTMLText(url)
    fillUnivList(uinfo,html)
    printUnivList(uinfo,20)     #只显示20所大学信息

main()
