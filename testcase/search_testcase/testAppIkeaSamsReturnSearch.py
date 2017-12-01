# -*- coding: utf8 -*-
import unittest
from AthenaTest.common.loadDatas import *

import sys
import importlib
importlib.reload(sys)

class TestAppIkeaSamsReturnSearch(unittest.TestCase):

    def setUp(self):
        self.datafile = '/Users/snolia/PycharmProjects/SCM3.0/AthenaTest/datacase/search_datacase/app_ikea_sams_return_search.xls'

    def test_waitPickUpGoodsSearch(self):
        '''宜家SMAS返货：待提货列表'''
        datafile = self.datafile
        loadDatas(self, datafile, u'waitPickUpGoodsSearch')

    def test_waitArriveSearch(self):
        '''宜家SMAS返货：待送达列表'''
        datafile = self.datafile
        loadDatas(self, datafile, u'waitArriveSearch')

    def test_ikeaAbnormalSamsSearch(self):
        '''宜家SMAS返货：异常订单列表'''
        datafile = self.datafile
        loadDatas(self, datafile, u'ikeaAbnormalSamsSearch')

if __name__ == "__main__":
    unittest.main()
