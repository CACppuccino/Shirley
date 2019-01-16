# use requirement.txt for virtual env install

from test import succ_test, fail_test

def test():
    succ_test()
    fail_test()
    

if __name__=='__main__':
    print('start testing...    (^-^)')
    test()
    print('Test end')
