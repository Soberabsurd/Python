import os
from conf.ATM_conf import url
def log(info):
    if os.path.exists(url+r'\data\log.txt'):
        with open(url+r'\data\log.txt','a',encoding='utf-8') as f:
            f.write(info)
            f.write('\n')
            f.flush()
    else:
        with open(url+r'\data\log.txt','w',encoding='utf-8') as f:
            f.write(info)
            f.write('\n')
            f.flush()