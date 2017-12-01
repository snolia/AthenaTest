# -*- coding: utf8 -*-
import unittest
from AthenaTest.common.loadDatas import *

import sys
import importlib
importlib.reload(sys)

class TestWebBackendSearch(unittest.TestCase):

    def setUp(self):
        self.datafile = '/Users/snolia/PycharmProjects/SCM3.0/AthenaTest/datacase/search_datacase/web_backend_search.xls'

    def test_orderTurnSearch(self):
        '''末端转单查询'''
        datafile = self.datafile
        loadDatas(self, datafile, u'orderTurnSearch')

    def test_takeOperationSearch(self):
        '''代操作查询'''
        datafile = self.datafile
        loadDatas(self, datafile, u'takeOperationSearch')

    def test_confirmCostSearch(self):
        '''大区成本查询'''
        datafile = self.datafile
        loadDatas(self, datafile, u'confirmCostSearch')

    def test_clearingCostSearch(self):
        '''大区结算查询'''
        datafile = self.datafile
        loadDatas(self, datafile, u'clearingCostSearch')

    def test_payCostSearch(self):
        '''大区支付查询'''
        datafile = self.datafile
        loadDatas(self, datafile, u'payCostSearch')

    def test_addFeeAuditSearch(self):
        '''增值审核'''
        datafile = self.datafile
        loadDatas(self, datafile, u'addFeeAuditSearch')

    def test_verifiyChangeSearch(self):
        '''核销变更'''
        datafile = self.datafile
        loadDatas(self, datafile, u'verifiyChangeSearch')

if __name__ == "__main__":
    unittest.main()



