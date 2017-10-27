import time
from lib.production_log import log
from conf.ATM_conf import money_url
def withdraw(money):
    while True:
        drwa=int(input('请输入提现金额 ; '))
        sure=input('本次提现金额为 : %s, 手续费为此次金额的5%,是否出票?')
        if sure == 'yes' or sure == 'ok':
            service=int(drwa*0.05)
            money=money-(service+drwa)
            with open(money_url,'w',encoding='utf-8') as f:
                f.write(str(money))
                f.flush()
                info=time.strftime('%Y-%m-%d %X')+' 提现金额为 : %s,手续费为 : %s,余额为: %s,交易结果为: successful.' %(drwa,service,money)
                log(info)
        elif sure == 'no' or sure == 'quit':
            return
        else:
            print('请输入正确的格式')