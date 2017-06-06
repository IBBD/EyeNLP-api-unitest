# -*- coding: utf-8 -*-

# 统一测试
# Author: Alex
# Created Time: 2017年05月12日 星期五 11时15分06秒
#import sys
import requests
import unittest

host = 'http://api.nlp.eyedmp.com'
content1 = '广州迪奥信息科技有限公司创立于2012年。'
content2 = '5月14日，国家主席习近平在北京出席“一带一路”国际合作高峰论坛开幕式，并发表题为《携手推进“一带一路”建设》的主旨演讲。'


def debug(title, *args):
    print("-"*20)
    print(title)
    print(args)


class NLPTestCase(unittest.TestCase):
    def test_init(self):
        """接口基本测试"""
        ner_url = '%s/ner/all' % host
        r = requests.post(ner_url+"?debug=true", json={"contents":[content1]}).json()
        self.assertEqual(r['code'], 0, msg=r['message'])
        self.assertGreater(r['run_time'], 0, msg=r['message'])

    def test_ner(self):
        """测试实体识别接口"""
        ner_url = '%s/ner/all' % host
        r = requests.post(ner_url, json={"contents":[content1]}).json()
        self.assertEqual(r['code'], 0, msg=r['message'])
        self.assertEqual(len(r['data']), 1, msg=r['message'])
        debug("单文本的实体识别接口: ", r)

        r = requests.post(ner_url, json={"contents":[content1, content2]}).json()
        self.assertEqual(r['code'], 0, msg=r['message'])
        self.assertEqual(len(r['data']), 2, msg=r['message'])
        debug("单文本的实体识别接口: ", r)

    def test_keywords(self):
        """测试关键词提取接口"""
        url = "%s/article/keywords/" % host
        r = requests.post(url + '1', json={"contents":[content1]}).json()
        self.assertEqual(r['code'], 0, msg=r['message'])
        self.assertEqual(len(r['data']), 1, msg=r['message'])
        debug("单文本的关键词提取接口: ", r)

        r = requests.post(url + '2', json={"contents":[content1, content2]}).json()
        self.assertEqual(r['code'], 0, msg=r['message'])
        self.assertEqual(len(r['data']), 2, msg=r['message'])
        debug("多文本的关键词提取接口: ", r)

    def test_summary(self):
        """测试自动摘要提取接口"""
        url = "%s/article/summary/" % host
        r = requests.post(url + '1', json={"contents":[content1]}).json()
        self.assertEqual(r['code'], 0, msg=r['message'])
        self.assertEqual(len(r['data']), 1, msg=r['message'])
        debug("单文本的自动摘要提取接口: ", r)

        r = requests.post(url + '2', json={"contents":[content1, content2]}).json()
        self.assertEqual(r['code'], 0, msg=r['message'])
        self.assertEqual(len(r['data']), 2, msg=r['message'])
        debug("多文本的自动摘要提取接口: ", r)

    def test_phrase(self):
        """测试短语提取提取接口"""
        url = "%s/article/summary/" % host
        r = requests.post(url + '1', json={"contents":[content1]}).json()
        self.assertEqual(r['code'], 0, msg=r['message'])
        self.assertEqual(len(r['data']), 1, msg=r['message'])
        debug("单文本的短语提取接口: ", r)

        r = requests.post(url + '2', json={"contents":[content1, content2]}).json()
        self.assertEqual(r['code'], 0, msg=r['message'])
        self.assertEqual(len(r['data']), 2, msg=r['message'])
        debug("多文本的短语提取接口: ", r)

    def test_segment(self):
        """测试词性分析接口"""
        url = "%s/segment/stardard" % host
        r = requests.post(url, json={"content":content1}).json()
        self.assertEqual(r['code'], 0, msg=r['message'])
        self.assertGreater(len(r['data']), 0, msg=r['message'])
        debug("标准词性分析接口: ", r)

        url = "%s/segment/senior" % host
        r = requests.post(url, json={"content":content1}).json()
        self.assertEqual(r['code'], 0, msg=r['message'])
        self.assertGreater(len(r['data']), 0, msg=r['message'])
        debug("高级词性分析接口: ", r)

    def test_suggest(self):
        """文本推荐接口"""
        url = "%s/suggest/distance" % host
        words = {"words": ["自行车","单车","摩托车","汽车","大巴"]}
        r = requests.post(url, json=words).json()
        self.assertEqual(r['code'], 0, msg=r['message'])
        self.assertGreater(len(r['data']), 0, msg=r['message'])
        debug("语义距离计算接口: ", r)

        url = "%s/suggest/sentence" % host
        contents = {
            "contents": [
                "威廉王子发表演说 呼吁保护野生动物",
                "《时代》年度人物最终入围名单出炉 普京马云入选",
                "“黑格比”横扫菲：菲吸取“海燕”经验及早疏散",
                "英报告说 空气污染带来“公共健康危机",
                "日本保密法将正式生效 日媒指其损害国民知情权"
            ],
            "word":"陈述",
            "size":2
        }
        r = requests.post(url, json=contents).json()
        self.assertEqual(r['code'], 0, msg=r['message'])
        self.assertEqual(len(r['data']), 2, msg=r['message'])
        debug("文本推荐接口: ", r)

    def test_dependency(self):
        """依存句法分析"""
        url = "%s/dependency/maximum-entropy" % host
        r = requests.post(url, json={"content":content1}).json()
        self.assertEqual(r['code'], 0, msg=r['message'])
        debug("依存句法分析接口: maximum-entropy: ", r)

        url = "%s/dependency/crf" % host
        r = requests.post(url, json={"content":content1}).json()
        self.assertEqual(r['code'], 0, msg=r['message'])
        debug("依存句法分析接口: crf: ", r)

    def test_classify(self):
        content = '市民于2016年1月1日在东莞市黄江镇江南路（港华门诊部正对面）的小米手机专卖店购买了一个苹果5S手机，价值2600元（有发票）。市民反映经苹果官方网站查询到该手机激活日期为2014，并于1月2日与商家协商退换，商家拒绝处理。现市民要求商家更换一台全新的手机或退款，请协调。'
        url = "%s/classify/contents/predict/cellphone" % host
        r = requests.post(url, json={"contents":[content]}).json()
        self.assertEqual(r['code'], 0, msg=r['message'])
        self.assertEqual(len(r['data']), 1, msg="返回结果和输入不对应")
        debug("文本分类接口: ", r)


if __name__ == '__main__':
    #host = 'http://' + sys.argv[1]
    unittest.main()
