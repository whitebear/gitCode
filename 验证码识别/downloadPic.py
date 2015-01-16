import urllib2
url="http://www.bjld.gov.cn/csibiz/indinfo/validationCodeServlet.do?d=1421143749"
path="./image/"
for i in range(100):
    socket = urllib2.urlopen(url)
    data = socket.read()
    with open(path+str(i)+".jpg", "wb") as jpg:
        jpg.write(data)
    socket.close()
