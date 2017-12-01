# -*- coding: utf8 -*-
import unittest
from AthenaTest.common.loadDatas import *

import sys
import importlib
importlib.reload(sys)

class TestWebWarehouseClearingSearch(unittest.TestCase):

    def setUp(self):
        self.datafile = '/Users/snolia/PycharmProjects/SCM3.0/AthenaTest/datacase/search_datacase/web_warehouse_clearing_search.xls'

    def test_cycleTrunkBillSearch(self):
        '''物流账单（周期）'''
        datafile = self.datafile
        loadDatas(self, datafile, u'cycleTrunkBillSearch')

    def test_noncycleTrunkBillSearch(self):
        '''物流账单（手动）'''
        datafile = self.datafile
        loadDatas(self, datafile, u'noncycleTrunkBillSearch')


        # 这块移动到loadDatas中进行处理
        #errortest = loadDatas(self, datafile, u'addData')
        #print(errortest)
        #for result in errortest:
            #with self.subTest(data=result):  # 注意subTest的用法
                #self.assertEqual(result, "pass")


if __name__ == "__main__":
    unittest.main()



