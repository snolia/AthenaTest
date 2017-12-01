# -*- coding: utf8 -*-
import unittest
from AthenaTest.common.loadDatas import *

import sys
import importlib
importlib.reload(sys)

class TestAppPendingOrderSearch(unittest.TestCase):

    def setUp(self):
        self.datafile = '/Users/snolia/PycharmProjects/SCM3.0/AthenaTest/datacase/search_datacase/app_pending_order_search.xls'

    def test_pickUpGoodsSearch(self):
        '''待提货'''
        datafile = self.datafile
        loadDatas(self, datafile, u'pickUpGoodsSearch')

    def test_houseCallSearch(self):
        '''待上门'''
        datafile = self.datafile
        loadDatas(self, datafile, u'houseCallSearch')
    def test_signSearch(self):
        '''待签收'''
        datafile = self.datafile
        loadDatas(self, datafile, u'signSearch')

    def test_abnormalSearch(self):
        '''异常'''
        datafile = self.datafile
        loadDatas(self, datafile, u'abnormalSearch')

    def test_allOrderSearch(self):
        '''全部订单'''
        datafile = self.datafile
        loadDatas(self, datafile, u'allOrderSearch')

if __name__ == "__main__":
    unittest.main()
