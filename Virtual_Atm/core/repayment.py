import time
from lib.production_log import log
from conf.ATM_conf import money_url
def repay(money):
    while True:
        project=input('输入还款项目 : ')
        if project == 'quit' or project == 'exit':
            return
        repay_money=int(input('输入还款金额 : '))
        sure=input('还款项目为 : %s ,还款金额为 : %s 确认还款?' %(project,repay_money))
        if sure == 'yes' or sure == 'ok':
            money=money-repay_money
            with open(money_url,'w',encoding='utf-8') as f:
                f.write(str(money))
                f.flush()
                info = time.strftime('%Y-%m-%d %X') + ' 还款项目为 : %s ,还款金额为 : %s ,余额为: %s,交易结果为: successful.' %(project,repay_money,money)
                log(info)
        elif sure == 'no' or sure == 'quit':
            return
        else:
            print('请输入正确格式.')