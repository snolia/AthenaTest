# -*- coding: utf8 -*-
import unittest
from AthenaTest.common.loadDatas import *

import sys
import importlib
importlib.reload(sys)

class TestWebBasicDataAuditSearch(unittest.TestCase):

    def setUp(self):
        self.datafile = '/Users/snolia/PycharmProjects/SCM3.0/AthenaTest/datacase/search_datacase/web_basic_data_audit_search.xls'

    def test_merchantInfoAuditSearch(self):
        '''商家资料审核、商家资料审核详情'''
        datafile = self.datafile
        loadDatas(self, datafile, u'merchantInfoAuditSearch')

    def test_trunkInfoAuditSearch(self):
        '''物流资料审核、物流资料详情'''
        datafile = self.datafile
        loadDatas(self, datafile, u'trunkInfoAuditSearch')

    def test_branchInfoAuditSearch(self):
        '''网点资料审核、网点资料审核详情'''
        datafile = self.datafile
        loadDatas(self, datafile, u'branchInfoAuditSearch')

        # 这块移动到loadDatas中进行处理
        #errortest = loadDatas(self, datafile, u'addData')
        #print(errortest)
        #for result in errortest:
            #with self.subTest(data=result):  # 注意subTest的用法
                #self.assertEqual(result, "pass")


if __name__ == "__main__":
    unittest.main()



