import json
from conf.ATM_conf import userinfo
def auth(func):
    def inner(*args,**kwargs):
        while True:
            username=input('输入账户用户名 : ')
            password=input('输入账户密码 : ')
            with open(userinfo,'r',encoding='utf-8') as f:
                for info in f:
                    info=json.loads(info)
                    if username in info and password == info[username]:
                        print('登录成功.')
                        func(*args,**kwargs)
                    else:
                        print('账户名密码错误,请重试.')
