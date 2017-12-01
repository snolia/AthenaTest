# -*- coding: utf8 -*-
import unittest
from AthenaTest.common.loadDatas import *

import sys
import importlib
importlib.reload(sys)

class TestWebBranchOrderSearch(unittest.TestCase):

    def setUp(self):
        self.datafile = '/Users/snolia/PycharmProjects/SCM3.0/AthenaTest/datacase/search_datacase/web_branch_order_search.xls'

    def test_orderAppointSearch(self):
        '''预约列表查询'''
        datafile = self.datafile
        loadDatas(self, datafile, u'orderAppointSearch')

    def test_orderDistributionSearch(self):
        '''派单列表查询'''
        datafile = self.datafile
        loadDatas(self, datafile, u'orderDistributionSearch')

    def test_orderTurnAuditSearch(self):
        '''转单审核列表查询'''
        datafile = self.datafile
        loadDatas(self, datafile, u'orderTurnAuditSearch')

    def test_orderMonitorinSearch(self):
        '''服务监控列表查询'''
        datafile = self.datafile
        loadDatas(self, datafile, u'orderMonitorinSearch')

    def test_orderNotArriveSearch(self):
        '''未到件列表查询'''
        datafile = self.datafile
        loadDatas(self, datafile, u'orderNotArriveSearch')

    def test_printListSearch(self):
        '''打印面单列表查询'''
        datafile = self.datafile
        loadDatas(self, datafile, u'printListSearch')

if __name__ == "__main__":
    unittest.main()
