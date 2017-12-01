# -*- coding: utf8 -*-
import unittest
from AthenaTest.common.loadDatas import *

import sys
import importlib
importlib.reload(sys)

class TestWebBasicDataSearch(unittest.TestCase):

    def setUp(self):
        self.datafile = '/Users/snolia/PycharmProjects/SCM3.0/AthenaTest/datacase/search_datacase/web_basic_data_search.xls'

    def test_merchantInfoSearch(self):
        '''商家资料、商家资料详情'''
        datafile = self.datafile
        loadDatas(self, datafile, u'merchantInfoSearch')

    def test_warehouseInfoSearch(self):
        '''收货仓资料、收货仓资料详情'''
        datafile = self.datafile
        loadDatas(self, datafile, u'warehouseInfoSearch')

    def test_trunkInfoSearch(self):
        '''物流资料、物流资料详情'''
        datafile = self.datafile
        loadDatas(self, datafile, u'trunkInfoSearch')

    def test_branchInfoSearch(self):
        '''网点资料、网点资料详情'''
        datafile = self.datafile
        loadDatas(self, datafile, u'branchInfoSearch')


        # 这块移动到loadDatas中进行处理
        #errortest = loadDatas(self, datafile, u'addData')
        #print(errortest)
        #for result in errortest:
            #with self.subTest(data=result):  # 注意subTest的用法
                #self.assertEqual(result, "pass")


if __name__ == "__main__":
    unittest.main()



