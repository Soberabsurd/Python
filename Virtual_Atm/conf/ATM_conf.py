import json
import os
import time
main_str='-----------------\n' \
         '1.商城购物.\n' \
         '2.金额提现.\n' \
         '3.账户转账.\n' \
         '4.账户还款.\n' \
         '5.操作日志.\n' \
         '6.管理接口.\n' \
         '7.退出平台.\n' \
         '-----------------'
userinfo_dict={'admin':'123456',
          'wangdong':'wangdong',
          'alex':'alex3714'
          }
goods={
    '1':['iphoneX',8300],
    '2':['mate8',4000],
    '3':['3D_TV',20000],
    '4':['apple_mac',16000],
    '5':['lenovo_pc',8000],
    '6':['Ipad',5000]
}
control_list='----------------\n' \
             '1.添加用户.\n' \
             '2.冻结用户.\n' \
             '3.用户额度.\n' \
             '----------------\n'
interface='1.查询用户额度.\n' \
          '2.修改用户额度.\n'
def change():
    from lib.production_log import log
    modify=int(input('修改额度值 : '))
    with open(money_url,'w',encoding='utf-8') as f:
        f.write(json.dumps(modify))
    info = time.strftime('%Y-%m-%d %X') + ' 修改余额为: %s,交易结果为: successful.' % (modify)
    log(info)
    return '修改额度成功.'
url=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
userinfo=url+r'\data\user'
money_url=url+r'\data\money'
