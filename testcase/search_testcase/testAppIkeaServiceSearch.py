# -*- coding: utf8 -*-
import unittest
from AthenaTest.common.loadDatas import *

import sys
import importlib
importlib.reload(sys)

class TestAppIkeaServiceSearch(unittest.TestCase):

    def setUp(self):
        self.datafile = '/Users/snolia/PycharmProjects/SCM3.0/AthenaTest/datacase/search_datacase/app_ikea_service_search.xls'

    def test_waitSetOutOrderSearch(self):
        '''宜家安装订单：待出发列表'''
        datafile = self.datafile
        loadDatas(self, datafile, u'waitSetOutOrderSearch')

    def test_waitStartOrderSearch(self):
        '''宜家安装订单：待开始列表'''
        datafile = self.datafile
        loadDatas(self, datafile, u'waitStartOrderSearch')

    def test_waitSignServiceSearch(self):
        '''宜家安装订单：待签收列表'''
        datafile = self.datafile
        loadDatas(self, datafile, u'waitSignServiceSearch')

    def test_ikeaAbnormalServiceSearch(self):
        '''宜家安装订单：异常订单列表'''
        datafile = self.datafile
        loadDatas(self, datafile, u'ikeaAbnormalServiceSearch')

if __name__ == "__main__":
    unittest.main()
