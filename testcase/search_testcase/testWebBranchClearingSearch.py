# -*- coding: utf8 -*-
import unittest
from AthenaTest.common.loadDatas import *

import sys
import importlib
importlib.reload(sys)

class TestWebBranchClearingSearch(unittest.TestCase):

    def setUp(self):
        self.datafile = '/Users/snolia/PycharmProjects/SCM3.0/AthenaTest/datacase/search_datacase/web_branch_clearing_search.xls'

    def test_standardBranchBillConfirmSearch(self):
        '''网点账单确认'''
        datafile = self.datafile
        loadDatas(self, datafile, u'standardBranchBillConfirmSearch')

    def test_nonsBranchBillConfirmSearch(self):
        '''网点对账（非标）'''
        datafile = self.datafile
        loadDatas(self, datafile, u'nonsBranchBillConfirmSearch')


        # 这块移动到loadDatas中进行处理
        #errortest = loadDatas(self, datafile, u'addData')
        #print(errortest)
        #for result in errortest:
            #with self.subTest(data=result):  # 注意subTest的用法
                #self.assertEqual(result, "pass")


if __name__ == "__main__":
    unittest.main()



