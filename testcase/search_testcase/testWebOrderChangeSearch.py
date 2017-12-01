# -*- coding: utf8 -*-
import unittest
from AthenaTest.common.loadDatas import *

import sys
import importlib
importlib.reload(sys)

class TestWebOrderChangeSearch(unittest.TestCase):

    def setUp(self):
        self.datafile = '/Users/snolia/PycharmProjects/SCM3.0/AthenaTest/datacase/search_datacase/web_order_change_search.xls'

    def test_orderCancelSearch(self):
        '''订单取消查询'''
        datafile = self.datafile
        loadDatas(self, datafile, u'orderCancelSearch')

    def test_orderChangeSearch(self):
        '''订单变更查询'''
        datafile = self.datafile
        loadDatas(self, datafile, u'orderChangeSearch')

    def test_orderChangeAuditSearch(self):
        '''变更审核查询'''
        datafile = self.datafile
        loadDatas(self, datafile, u'orderChangeAuditSearch')

    def test_orderTerminationSearch(self):
        '''服务终止查询'''
        datafile = self.datafile
        loadDatas(self, datafile, u'orderTerminationSearch')

    def test_orderTerminationAuditSearch(self):
        '''服务终止审核查询'''
        datafile = self.datafile
        loadDatas(self, datafile, u'orderTerminationAuditSearch')


if __name__ == "__main__":
    unittest.main()



