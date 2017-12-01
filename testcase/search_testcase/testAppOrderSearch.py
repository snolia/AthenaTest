# -*- coding: utf8 -*-
import unittest
from AthenaTest.common.loadDatas import *

import sys
import importlib
importlib.reload(sys)

class TestAppOrderSearch(unittest.TestCase):

    def setUp(self):
        self.datafile = '/Users/snolia/PycharmProjects/SCM3.0/AthenaTest/datacase/search_datacase/app_order_search.xls'

    def test_orderSearch(self):
        '''app订单搜索'''
        datafile = self.datafile
        loadDatas(self, datafile, u'orderSearch')

if __name__ == "__main__":
    unittest.main()
