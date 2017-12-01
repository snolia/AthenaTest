# -*- coding: utf8 -*-
import unittest
from AthenaTest.common.loadDatas import *

import sys
import importlib
importlib.reload(sys)

class TestWebTerminalManageSearch(unittest.TestCase):

    def setUp(self):
        self.datafile = '/Users/snolia/PycharmProjects/SCM3.0/AthenaTest/datacase/search_datacase/web_terminal_manage_search.xls'

    def test_standardBranchBillSearch(self):
        '''网点账单（标准）'''
        datafile = self.datafile
        loadDatas(self, datafile, u'standardBranchBillSearch')

    def test_nonsBranchBillGeneratSearch(self):
        '''账单生成（非标）'''
        datafile = self.datafile
        loadDatas(self, datafile, u'nonsBranchBillGeneratSearch')

    def test_nonsBranchBillSearch(self):
        '''网点账单（非标）'''
        datafile = self.datafile
        loadDatas(self, datafile, u'nonsBranchBillSearch')

    def test_branchBillAuditSearch(self):
        '''网点账单审核'''
        datafile = self.datafile
        loadDatas(self, datafile, u'branchBillAuditSearch')


        # 这块移动到loadDatas中进行处理
        #errortest = loadDatas(self, datafile, u'addData')
        #print(errortest)
        #for result in errortest:
            #with self.subTest(data=result):  # 注意subTest的用法
                #self.assertEqual(result, "pass")


if __name__ == "__main__":
    unittest.main()



