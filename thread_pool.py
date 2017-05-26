# -*- coding: utf-8 -*-

#
# Author: Alex
# Created Time: 2017年05月26日 星期五 09时04分58秒
import time
from multiprocessing.dummy import Pool as ThreadPool

pool = ThreadPool()

def doSomethings(x):
    print(x)
    time.sleep(1)
    print("====")
    return x


def cli():
    res = pool.map(doSomethings, range(10))
    print("*"*30)
    print(res)


if __name__ == '__main__':
    cli()
