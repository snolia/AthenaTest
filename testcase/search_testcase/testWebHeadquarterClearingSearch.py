# -*- coding: utf8 -*-
import unittest
from AthenaTest.common.loadDatas import *

import sys
import importlib
importlib.reload(sys)

class TestAddData(unittest.TestCase):

    def setUp(self):
        self.datafile = '/Users/snolia/PycharmProjects/SCM3.0/AthenaTest/datacase/search_datacase/web_headquarter_clearing_search.xls'

    def test_writeOffOrderSearch(self):
        '''订单冲销'''
        datafile = self.datafile
        loadDatas(self, datafile, u'writeOffOrderSearch')

    def test_writeOffRecordSearch(self):
        '''冲销记录'''
        datafile = self.datafile
        loadDatas(self, datafile, u'writeOffRecordSearch')

    def test_merchantReceiptSearch(self):
        '''商家收款单'''
        datafile = self.datafile
        loadDatas(self, datafile, u'merchantReceiptSearch')

    def test_standardBranchPaymentSearch(self):
        '''网点付款单（标准）'''
        datafile = self.datafile
        loadDatas(self, datafile, u'standardBranchPaymentSearch')

    def test_nonsBranchPaymentSearch(self):
        '''网点付款单（非标）'''
        datafile = self.datafile
        loadDatas(self, datafile, u'nonsBranchPaymentSearch')

    def test_noncycleTrunkPaymentSearch(self):
        '''物流付款单（按点）'''
        datafile = self.datafile
        loadDatas(self, datafile, u'noncycleTrunkPaymentSearch')

    def test_cycleTrunkPaymentSearch(self):
        '''物流付款单（手动）'''
        datafile = self.datafile
        loadDatas(self, datafile, u'cycleTrunkPaymentSearch')



            # 这块移动到loadDatas中进行处理
        #errortest = loadDatas(self, datafile, u'addData')
        #print(errortest)
        #for result in errortest:
            #with self.subTest(data=result):  # 注意subTest的用法
                #self.assertEqual(result, "pass")


if __name__ == "__main__":
    unittest.main()



