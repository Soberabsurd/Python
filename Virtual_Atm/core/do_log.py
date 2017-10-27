from conf.ATM_conf import url
def log():
    with open(url+r'\data\log.txt','r',encoding='utf-8') as read_f:
        for info in read_f:
            print(info,end='')