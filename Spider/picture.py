import urllib.request

response=urllib.request.urlopen('https://placekitten.com/g/1024/1024')
img=response.read()

with open('cat.jpg','wb') as f:
    f.write(img)
    
