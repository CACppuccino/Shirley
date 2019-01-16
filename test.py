import requests
import time
from settings import *

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
