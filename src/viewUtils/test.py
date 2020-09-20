##
# Tkinter： Tkinter 模块(Tk 接口)是 Python 的标准 Tk GUI 工具包的接口 .Tk 和 Tkinter 可以在大多数的 Unix 平台下使用,
# 同样可以应用在 Windows 和 Macintosh 系统里。Tk8.0 的后续版本可以实现本地窗口风格,并良好地运行在绝大多数平台中。
# ##
import tkinter as tk
# top = tk.Tk()
#进入消息循环
# top.mainloop()
# ===========================================================
# li = ['c', 'family', 'python']
# movie = ['radio', 'checkbox', 'love me forever']
# listb = tk.Listbox(top)
# list2 = tk.Listbox(top)
# for item in li:
#     listb.insert(0, item)
# for item in movie:
#     list2.insert(0, item)
# listb.pack()
# list2.pack()
# top.mainloop()
# ===========================================================
# 如何产生hash值之三个阶段
'''
import hashlib
# # ######## 256 ########
# # 1、造出hash工厂
hash = hashlib.sha256('898oaFs09f'.encode('utf8'))     #同一种hash算法得到的长度是固定的
# # 2、运送原材料
hash.update('alvin'.encode('utf8'))                     #工厂传入的原材料都是bytes类型
# # 3、产出hash值
print(hash.hexdigest())  # e79e68f070cdedcfe63eaf1a2e92c83b4cfb1b5c6bc452d214c1b7e77cdfd1c7
'''
'''
import hashlib
m=hashlib.md5()                               #括号内也可以传值，类型也要求是bytes类型
m.update('你好呀！'.encode('utf-8'))
print(m.hexdigest())                          #9e49eb8e75b9a87424e388b862ea5f83

# 与上述hash的结果一样
import hashlib
m=hashlib.md5('你'.encode('utf-8'))          #括号内也可以传值，类型也要求是bytes类型
m.update('好呀！'.encode('utf-8'))
print(m.hexdigest())
'''
# 三、校验文件的一致性（如何保证下载的文件过程中不丢包，保证下载数据的完整性）
# -----------文件一致校验----------------
'''可以拷贝一个文件放在两个不同的盘中，然后通过判断两个文件的hash值是否相等，判断两个文件是否是同一个文件'''
'''
import hashlib
m = hashlib.md5()
with open(r'G:/logging模块配图.png','rb') as f:
    for line in f:
        m.update(line)
print(m.hexdigest())          #47a6b079cc33a4f312786b46e61e0305

import hashlib
m = hashlib.md5()
with open(r'H:/logging模块配图.png','rb') as f:
    for line in f:
        m.update(line)
print(m.hexdigest()) 
'''
'''
# 五、破解用户注册的密码:模拟撞库破解密码
import hashlib
passwds=[                      #可以通过random实现对passwds中的内容
    'alex3714',
    'alex1313',
    'alex94139413',
    'alex123456',
    '123456alex',
    'a123lex',
    ]

def make_passwd_dic(passwds):                #通过明文密码列表，造出与之对应的hash值得字典
    dic={}
    for passwd in passwds:
        m=hashlib.md5()                      #使用md5算法，造了一个工厂
        m.update(passwd.encode('utf-8'))     #给工厂运送原材料(即我们要加密的内容)
        dic[passwd]=m.hexdigest()            #产出hash值（即最终的产品），将其加入到我们事先造好的空字典中，字典形式:{密码：hash值}
    return dic

def break_code(cryptograph,passwd_dic):      #判断拦截的hash值是否与字典中事先造好的hash值相等，相等则说明成功进行破解
    for k,v in passwd_dic.items():
        if v == cryptograph:
            print('密码是===>\033[46m%s\033[0m' %k)

cryptograph='aee949757a2e698417463d47acac93df'     #我们拦截拿到的密码，经过加密的hash值
break_code(cryptograph,make_passwd_dic(passwds))   #将要破解的密码hash值，和事先造好的hash的字典当做函数的实参传给对应的形参
'''
'''
# python 还有一个 hmac 模块，它内部对我们创建 key 和 内容 进行进一步的处理然后再加密
# hmac模块的加密方式，与hashlib类似
import hmac
h = hmac.new('天王盖地虎'.encode('utf8'))          #hmac必须要加盐
h.update('hello'.encode('utf8'))
print(h.hexdigest())                 #1abaae8f65f68f2695a8545c5bc8e738

#要想保证hmac最终结果一致，必须保证：
#1:hmac.new括号内指定的初始key一样
#2:无论update多少次，校验的内容累加到一起是一样的内容

# 下面单重方式得到的结果是一样的
import hmac
h1=hmac.new(b'tom')          #初始值必须保证一致，最终得到的结果就会不一样
h1.update(b'hello')
h1.update(b'world')
print(h1.hexdigest())

h2=hmac.new(b'tom')         #初始值必须保证一致，最终得到的结果就会不一样
h2.update(b'helloworld')
print(h2.hexdigest())

h3=hmac.new(b'tomhelloworld')   #初始值不一样，所以与上面两种的结果不一样
print(h3.hexdigest())
'''


