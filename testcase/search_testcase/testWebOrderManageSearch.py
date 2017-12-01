# -*- coding: utf8 -*-
import unittest
from AthenaTest.common.loadDatas import *

import sys
import importlib
importlib.reload(sys)

class TestWebOrderManageSearch(unittest.TestCase):

    def setUp(self):
        self.datafile = '/Users/snolia/PycharmProjects/SCM3.0/AthenaTest/datacase/search_datacase/web_order_manage_search.xls'

    def test_importDirectSearch(self):
        '''直营导单'''
        datafile = self.datafile
        loadDatas(self, datafile, u'importDirectSearch')

    def test_addOrderSearch(self):
        '''录单'''
        datafile = self.datafile
        loadDatas(self, datafile, u'addOrderSearch')

    def test_importOrderSearch(self):
        '''暂存单'''
        datafile = self.datafile
        loadDatas(self, datafile, u'importOrderSearch')

    def test_TMSOrderSearch(self):
        '''TMS绑单'''
        datafile = self.datafile
        loadDatas(self, datafile, u'TMSOrderSearch')

    def test_printOrderSearch(self):
        '''打印订单'''
        datafile = self.datafile
        loadDatas(self, datafile, u'printOrderSearch')

    def test_allOrderSearch(self):
        '''订单查询'''
        datafile = self.datafile
        loadDatas(self, datafile, u'allOrderSearch')


if __name__ == "__main__":
    unittest.main()



