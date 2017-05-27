# -*- coding: utf-8 -*-

# 分类测试
# Author: Alex
# Created Time: 2017年05月26日 星期五 20时11分39秒
import sys
import pprint
import requests

pp = pprint.PrettyPrinter(indent=4)

def cli(host):
    host = 'http://%s' % host
    url = '%s/classify/predicts/root_model?debug=true' % host

    print("-"*40)
    contents = []
    for i in range(2):
        contents.append('广州迪奥信息科技有限公司是一家从事大数据研发的公司, 地址是广州市天河区华观路新塘田头岗二路一横街4号B栋3楼. %d' % i)

    r = requests.post(url, json={"contents": contents}).json()
    pp.pprint(r)

    print("-"*40)
    contents = []
    for i in range(1000):
        contents.append('广州迪奥信息科技有限公司是一家从事大数据研发的公司, 地址是广州市天河区华观路新塘田头岗二路一横街4号B栋3楼. %d' % i)

    r = requests.post(url, json={"contents": contents}).json()
    pp.pprint(r['run_time'])


if __name__ == '__main__':
    cli(sys.argv[1])
