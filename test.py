import requests
import time
from settings import *

def auto_post():
    print('shirley posting...')
    data = {"mainType":"2","subType":"1","country":"can1","openId":"oCiYP0dawrzKwMlmsKDdj15Bmk5","city":"can1","title":"请问哪里可以学PTE啊","remark":"请问哪里可以学习pte呢","pics":[],"address":None,"person":"can","weixin":"","tel":"","sentCar":{"sentCarType":0,"pp":0,"year":"","kNum":0,"bsx":0,"price":0},"tendData":{"areaMain":-1,"areaSub":-1,"houseType":-1,"wayType":-1,"cycleType":1,"tendPay":0},"answerType":13}
    r = requests.post(ROOT2 + '/huPublish/ph/', data = data)
    print('status_code', r.status_code)
    print('shirly leaves...')

def succ_test():
    print('succ test starts')
    params = {}
    start = time.time()
    r = requests.get(ROOT+'/tongcheng/records/', params=params)
    end = time.time()
    print('status code: ', r.status_code)
    print('time consume: ', end-start,' seconds')
    print('succ test ends')

def fail_test():
    """
    test whether the system fails properly
    """
    print('fail_test')
