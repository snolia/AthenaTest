# -*- coding: utf8 -*-
import unittest
from AthenaTest.common.loadDatas import *

import sys
import importlib
importlib.reload(sys)

class TestAppIkeaShipmentSearch(unittest.TestCase):

    def setUp(self):
        self.datafile = '/Users/snolia/PycharmProjects/SCM3.0/AthenaTest/datacase/search_datacase/app_ikea_shipment_search.xls'

    def test_waitLoadOrderSearch(self):
        '''宜家配送订单：待装车列表'''
        datafile = self.datafile
        loadDatas(self, datafile, u'waitLoadOrderSearch')

    def test_waitSignShipmentSearch(self):
        '''宜家配送订单：待签收列表'''
        datafile = self.datafile
        loadDatas(self, datafile, u'waitSignShipmentSearch')

    def test_ikeaAbnormalShipmentSearch(self):
        '''宜家配送订单：异常订单列表'''
        datafile = self.datafile
        loadDatas(self, datafile, u'ikeaAbnormalShipmentSearch')

if __name__ == "__main__":
    unittest.main()
