import time
from lib.production_log import log
from conf.ATM_conf import url,money_url
def transfer_main(money):
    while True:
        tran=input('输入转账用户 : ')
        if tran == 'quit' or tran == 'exit':
            return
        tran_money=int(input('输入转账金额 : '))
        sure=input('转账用户为 : %s , 转账金额为 : %s ,是否确认转账? ' %(tran,tran_money))
        if sure == 'ok' or sure == 'yes':
            money=money-tran_money
            with open(money_url,'w',encoding='utf-8') as f:
                f.write(str(money))
                f.flush()
                info = time.strftime('%Y-%m-%d %X') + ' 转账用户为 : %s ,转账金额为 : %s, 余额为: %s,交易结果为: successful.' % (tran,tran_money,money)
                log(info)
        elif sure == 'no' or sure == 'quit':
            return
        else:
            print('请输入正确格式的选项.')

