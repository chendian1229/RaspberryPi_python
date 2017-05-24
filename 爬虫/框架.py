import requests

def getHTMLText(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()                #   200
        r.encoding=r.apparent_encoding      #   utf-8 encoding
        return r.text
    except:
        return "Error"


if __name__=="__main__":
    url="https://www.jd.com/robot.txt"
    print(getHTMLText(url))
    
