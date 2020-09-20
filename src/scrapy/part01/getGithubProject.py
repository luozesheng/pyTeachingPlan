import requests as req
import webbrowser as web
import time
api = 'https://api.github.com/repos/channelcat/sanic'
webPage = "https://github.com/channelcat/sanic";
ld = None
allinfo = req.get(api).json();
curdate = allinfo['updated_at']
flag = True
while flag:
    print(ld, curdate)
    flag = False
    web.open(webPage)
    time.sleep(6)
