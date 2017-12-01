# -*- coding: utf8 -*-
import unittest
from AthenaTest.common.loadDatas import *

import sys
import importlib
importlib.reload(sys)

class TestWebTimebarOrderSearch(unittest.TestCase):

    def setUp(self):
        self.datafile = '/Users/snolia/PycharmProjects/SCM3.0/AthenaTest/datacase/search_datacase/web_timebar_order_search.xls'

    def test_outBoundTimebarSearch(self):
        '''出库时效'''
        datafile = self.datafile
        loadDatas(self, datafile, u'outBoundTimebarSearch')

    def test_arriveTimebarSearch(self):
        '''到件时效'''
        datafile = self.datafile
        loadDatas(self, datafile, u'arriveTimebarSearch')

    def test_appointTimebarSearch(self):
        '''预约时效'''
        datafile = self.datafile
        loadDatas(self, datafile, u'appointTimebarSearch')

    def test_signTimebarSearch(self):
        '''签收时效'''
        datafile = self.datafile
        loadDatas(self, datafile, u'signTimebarSearch')

    def test_distributionTimebarSearch(self):
        '''配送时效'''
        datafile = self.datafile
        loadDatas(self, datafile, u'distributionTimebarSearch')


        # 这块移动到loadDatas中进行处理
        #errortest = loadDatas(self, datafile, u'addData')
        #print(errortest)
        #for result in errortest:
            #with self.subTest(data=result):  # 注意subTest的用法
                #self.assertEqual(result, "pass")


if __name__ == "__main__":
    unittest.main()



