#coding=utf-8
import urllib
import urllib2
import cookielib
import imagecrack

def setupUA(req=None):
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36')
    req.add_header('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8')
    req.add_header('Cache-Control','max-age=0')
    req.add_header('Connection','keep-alive')
    req.add_header('Accept-Encoding','gzip, deflate, sdch')
    req.add_header('Accept-Language','zh-CN,zh;q=0.8')
    req.add_header('Host','www.bjld.gov.cn')
    

def doLogin():
    cookie = cookielib.CookieJar()

    
    cookie.set_cookie(make_cookie('wdcid','2065690dc154718a'))
    cookie.set_cookie(make_cookie('wdlast','1420785731'))
    cookie.set_cookie(make_cookie('_gscu_541390372','207857307rup4f18'))
    cookie.set_cookie(make_cookie('AXM6mOFhT5','MDAwM2IyNTMxZjgwMDAwMDAwMDMwNBcxKhAxNDIxMzQwMTM2'))
    cookie.set_cookie(make_cookie('qx2nR3OHg7','MDAwM2IyNTMxZjgwMDAwMDAwMzIwTgpIHC0xNDIxMzQwMTM2'))
    cookie.set_cookie(make_cookie('mjrzMBJgZO','MDAwM2IyNTMxZjgwMDAwMDAwMzEwDXJVXBIxNDIxNDkwMDQ1'))
    cookie.set_cookie(make_cookie('JSESSIONID','EF7F50E4D4BBCEBCFF8C25A98ACBA721'))
    
    cookieProc = urllib2.HTTPCookieProcessor(cookie)
    opener = urllib2.build_opener(cookieProc)
    urllib2.install_opener(opener)
    
    url="http://www.bjld.gov.cn/csibiz/indinfo/login.jsp?flag=3"
    req = urllib2.Request(url)
    setupUA(req)
    r = urllib2.urlopen(req)

    
    print r.read()
    #print cookie






    
    req = urllib2.Request('http://www.bjld.gov.cn/csibiz/indinfo/js/effects.js')
    setupUA(req)
    urllib2.urlopen(req)
    
    req = urllib2.Request('http://www.bjld.gov.cn/csibiz/indinfo/images/login/spsp.gif')
    setupUA(req)
    urllib2.urlopen(req)
    
    req = urllib2.Request('http://www.bjld.gov.cn/csibiz/indinfo/css/login/home2_styles.css')
    setupUA(req)
    urllib2.urlopen(req)
    
    req = urllib2.Request('http://www.bjld.gov.cn/csibiz/indinfo/js/validation_cn.js')
    setupUA(req)
    urllib2.urlopen(req)
    
    req = urllib2.Request('http://www.bjld.gov.cn/csibiz/indinfo/css/style_min.css')
    setupUA(req)
    urllib2.urlopen(req)
    
    req = urllib2.Request('http://www.bjld.gov.cn/csibiz/indinfo/images/login/logo.gif')
    setupUA(req)
    urllib2.urlopen(req)
    
    req = urllib2.Request('http://www.bjld.gov.cn/csibiz/indinfo/js/prototype_for_validation.js')
    setupUA(req)
    urllib2.urlopen(req)

    safecodeurl="http://www.bjld.gov.cn/csibiz/indinfo/validationCodeServlet.do?d=1421143749000"
    path="./safecode/"
    req = urllib2.Request(safecodeurl)
    setupUA(req)
    socket=urllib2.urlopen(req)
    data = socket.read()
    with open(path+"safe.jpg", "wb") as jpg:
        jpg.write(data)
    socket.close()
    
    username = '110101198601011738'
    password = '212121212121'
    safecode = imagecrack.Pic_Reg(path+'safe.jpg')
    print('safecode:'+safecode)
    
    data = {'j_username':username, 'j_password':password,'safecode':safecode}
    data_handler = urllib.urlencode(data)
    
    
    req = urllib2.Request('http://www.bjld.gov.cn/csibiz/indinfo/login_check')
    setupUA(req)
    r = urllib2.urlopen(req,data_handler)

    #print responser.read()
    print r.read()


def make_cookie(name, value):
    return cookielib.Cookie(
        version=0,
        name=name,
        value=value,
        port=None,
        port_specified=False,
        domain='www.bjld.gov.cn',
        domain_specified=True,
        domain_initial_dot=False,
        path="/csibiz/indinfo",
        path_specified=True,
        secure=False,
        expires=None,
        discard=False,
        comment=None,
        comment_url=None,
        rest=None
    )
def test():
    #cookie = cookielib.CookieJar()
    filename='./cookie.txt'
    cookie = cookielib.MozillaCookieJar(filename)
    cookie.set_cookie(make_cookie('JSESSIONID','EF7F50E4D4BBCEBCFF8C25A98ACBA721'))
    cookie.set_cookie(make_cookie('wdcid','2065690dc154718a'))
    cookie.set_cookie(make_cookie('wdlast','1420785731'))
    cookie.set_cookie(make_cookie('_gscu_541390372','207857307rup4f18'))
    cookie.set_cookie(make_cookie('AXM6mOFhT5','MDAwM2IyNTMxZjgwMDAwMDAwMDMwNBcxKhAxNDIxMzQwMTM2'))
    cookie.set_cookie(make_cookie('qx2nR3OHg7','MDAwM2IyNTMxZjgwMDAwMDAwMzIwTgpIHC0xNDIxMzQwMTM2'))
    cookie.set_cookie(make_cookie('mjrzMBJgZO','MDAwM2IyNTMxZjgwMDAwMDAwMzEwDXJVXBIxNDIxNDkwMDQ1'))
    
    cookieProc = urllib2.HTTPCookieProcessor(cookie)
    opener = urllib2.build_opener(cookieProc)
    urllib2.install_opener(opener)
    
    url="http://www.bjld.gov.cn/csibiz/indinfo/login.jsp?flag=3"
    req = urllib2.Request(url)
    setupUA(req)
    r = urllib2.urlopen(req)
    urllib2.urlopen(req)
    
    #print r.read()
    for c in cookie:
       print c

       
def main():
    doLogin()
    


    
main()
