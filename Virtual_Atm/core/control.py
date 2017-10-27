import json
import time
from lib.production_log import log
from conf.ATM_conf import control_list,userinfo,interface,change,userinfo_dict,money_url
def select():
    with open(money_url,'r',encoding='utf-8') as f:
        return f.read()
def update():
    return change()
def add():
    username=input('创建账户名 : ')
    password=input('创建密码 : ')
    userinfo_dict.setdefault(username,password)
    with open(userinfo, 'w', encoding='utf-8') as f:
        f.write(json.dumps(userinfo_dict))
        print('用户添加成功.')
        info = time.strftime('%Y-%m-%d %X') + ' 创建的用户名 : %s ,密码 : %s ,创建结果: successful.' % (username,password)
        log(info)
def frozen():
    delete=input('冻结账户名 : ')
    if delete in userinfo_dict:
        userinfo_dict[delete]=None
        with open(userinfo, 'w', encoding='utf-8') as f:
            f.write(json.dumps(userinfo_dict))
            print('用户冻结成功.')
            info = time.strftime('%Y-%m-%d %X') + ' 冻结的用户名 : %s , 冻结结果: successful.' % (delete)
            log(info)
    else:
        print('没有这个用户.')

def user_money():
    while True:
        print(interface)
        inter=input('选择额度业务 : ')
        if inter == 'exit' or inter == 'quit':
            return
        if inter in money_dict:
            res=money_dict[inter]()
            print(res)
        else:
            print('暂无此业务 : ')
control_dict = {'1': add,
                '2': frozen,
                '3': user_money
                }
money_dict={'1':select,
            '2':update
            }
def control_main():
    while True:
        print(control_list)
        con=input('选择管理业务 : ')
        if con == 'exit' or con == 'quit':
            return
        if con in control_dict:
            control_dict[con]()
        else:
            print('暂时不提供此服务.')