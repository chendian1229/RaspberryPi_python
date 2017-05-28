import requests
import re

def getHTMLText(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()                    #查看页面返回值是否是200,不是则引出异常
        r.encoding=r.apparent_encoding          #将页面代码HTML格式的转化为utf-8编码
        return r.text
    except:
        return "getHTMLText error"


def parsePage(ilt,html):
    try:
        plt=re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
        tlt=re.findall(r'\"raw_title\"\:\".*?\"',html)
        for i in range(len(plt)):
            price=eval(plt[i].split(':')[1])
            title=eval(tlt[i].split(':')[1])
            ilt.append([price,title])
    except:
        print("parsePage error")


def printGoodsList(ilt):
    tplt="{:4}\t{:8}\t{:16}"
    print(tplt.format("序号","价格","商品名称"))
    count=0
    for g in ilt:
        count=count+1
        print(tplt.format(count,g[0],g[1]))

def main():
    goods='书包'                                   #检索关键字 
    depth=2                                        #爬取深度规定
    start_url="https://s.taobao.com/search?q="+goods     #爬取页面链接
    infoList=[]                                     #输入列表
    for i in range(depth):
        try:
            url=start_url+'&s='+str(44*i)           #淘宝页面以44个物品为一页
            html=getHTMLText(url)
            parsePage(infoList,html)
        except:
            continue
    printGoodsList(infoList)

if __name__=="__main__":
   main() 


