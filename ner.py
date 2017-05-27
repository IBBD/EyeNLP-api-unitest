# -*- coding: utf-8 -*-

# 实体识别
# Author: Alex
# Created Time: 2017年05月25日 星期四 12时10分21秒
import sys
import pprint
import requests

pp = pprint.PrettyPrinter(indent=4)

def cli(host):
    host = 'http://%s' % host
    contents = [
        "广州华南理工大学座落于天河区。",
        "广州迪奥信息科技有限公司是一家从事大数据研发的公司, 地址是广州市天河区华观路新塘田头岗二路一横街4号B栋3楼.",
        "有个同学在广州市第一人民医院工作。",
        "旁边那个公安局的领导很不友好。",
        "有功电度表是一个专业术语。",
        "阿依莲(东圃大马路)位于雅怡街32号。",
    ]
    pp.pprint(contents)
    print("-"*40)

    ner_url = '%s/ner/all?debug=true' % host
    r = requests.post(ner_url, json={"contents": contents}).json()
    print('识别结果')
    pp.pprint(r)

    print("-"*40)
    contents = []
    for i in range(1000):
        contents.append('广州迪奥信息科技有限公司是一家从事大数据研发的公司, 地址是广州市天河区华观路新塘田头岗二路一横街4号B栋3楼.')

    r = requests.post(ner_url, json={"contents": contents}).json()
    pp.pprint(r['run_time'])


if __name__ == '__main__':
    cli(sys.argv[1])
