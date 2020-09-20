from selenium import webdriver
import time

# 运行前先下载 chrome driver,下载地址是：https://sites.google.com/a/chromium.org/chromedriver/downloads，点击【Latest Release: ChromeDriver x.xx】进入下载

url = 'https://weibo.com/5869525717/G2VASlH1o?from=page_1005055869525717_profile&wvr=6&mod=weibotime&type=comment' #可以替换成你想跟踪的单条微博链接
def start_chrome():
    driver = webdriver.Chrome(executable_path='./chromedriver')  # Windows 需写成'./chromedriver.exe'
    driver.start_client()
    return driver

def find_info():
    # css_selector
    sel   = 'span > span.line.S_line1 > span > em:nth-child(2)'
    elems = driver.find_elements_by_css_selector(sel)
    return [int(el.text) for el in elems[1:]]


while True:
    driver = start_chrome()
    driver.get(url)
    time.sleep(6) # wait loading
    info = find_info()
    #[123,456,789]
    rep,comm,like = info
    if rep > 30000:
        print('你关注的微博转发量已经过 '+str(rep))
        print(f'你喜欢的微博转发量已经超过{rep}') # f-string
        break
    else:
        print('Not happening')

    time.sleep(1200)

print('Done!')