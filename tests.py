# -*- coding: utf-8 -*-

# 统一测试
# Author: Alex
# Created Time: 2017年05月12日 星期五 11时15分06秒
import requests
import unittest

host = 'http://api.nlp.eyedmp.com'
ner_url = '%s/ner/all' % host
content1 = '广州迪奥信息科技有限公司创立于2012年。'
content2 = '5月14日，国家主席习近平在北京出席“一带一路”国际合作高峰论坛开幕式，并发表题为《携手推进“一带一路”建设》的主旨演讲。'


def debug(title, *args):
    print("-"*20)
    print(title)
    print(args)


class NLPTestCase(unittest.TestCase):
    def test_init(self):
        """接口基本测试"""
        r = requests.post(ner_url+"?debug=true", json={"contents":[content1]}).json()
        self.assertEqual(r['code'], 0, msg=r['message'])
        self.assertGreater(r['run_time'], 0, msg=r['message'])

    def test_ner(self):
        """测试实体识别接口"""
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
        print(r)
        self.assertEqual(r['code'], 0, msg=r['message'])
        debug("依存句法分析接口: maximum-entropy: ", r)

        url = "%s/dependency/crf" % host
        r = requests.post(url, json={"content":content1}).json()
        self.assertEqual(r['code'], 0, msg=r['message'])
        debug("依存句法分析接口: crf: ", r)


if __name__ == '__main__':
    unittest.main()
