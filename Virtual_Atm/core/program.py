import json
import os
from conf import ATM_conf
from core.control import control_main
from core.do_log import log
from core.repayment import repay
from core.shop import shoping
from core.transfer import transfer_main
from core.withdrawals import withdraw
from conf.ATM_conf import userinfo,money_url
# def auth(func):
#     def inner(*args,**kwargs):
#         while True:
#             username=input('输入账户用户名 : ')
#             password=input('输入账户密码 : ')
#             with open(userinfo,'r',encoding='utf-8') as f:
#                 for info in f:
#                     info=json.loads(info)
#                     if username in info and password == info[username]:
#                         print('登录成功.')
#                         func(*args,**kwargs)
#                     else:
#                         print('账户名密码错误,请重试.')


main_dict={'1':shoping,
           '2':withdraw,
           '3':transfer_main,
           '4':repay,
           '5':log,
           '6':control_main,
           '7':exit
           }
# @auth
def main():
    while True:
        userinput = input('输入账户账号 : ')
        password = input('输入账户密码 : ')
        with open(userinfo,'r',encoding='utf-8') as f:
            for info in f:
                info=json.loads(info)
                if userinput in info and password == info[userinput]:
                    while True:
                        print(ATM_conf.main_str)
                        service = input('输入要办理的业务 : ')
                        if service in main_dict and service != '6' and service != '5':
                            with open(money_url,'r',encoding='utf-8') as f:
                                res=f.read()
                            res=json.loads(res)
                            main_dict[service](int(res))
                        else:
                            main_dict[service]()
                else:
                    print('用户名密码错误.')


