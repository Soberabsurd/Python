import time
from conf.ATM_conf import goods,money_url
from lib.production_log import log
def shoping(money):
    while True:
        for line in goods.items():
            print(line)
        buy=input('选择要购买的商品 : ')
        if buy in goods:
            money=money-goods[buy][1]
            with open(money_url,'w',encoding='utf-8') as f:
                f.write(str(money))
                f.flush()
                info = time.strftime('%Y-%m-%d %X') + ' 您购买了 : %s ,余额为: %s,交易结果为: successful.' % (goods[buy][0],money)
                log(info)
        if buy == 'no' or buy == 'quit':
            return
