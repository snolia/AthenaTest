# -*- coding: utf8 -*-
import unittest
from AthenaTest.common.loadDatas import *

import sys
import importlib
importlib.reload(sys)

class TestWebFrontendSearch(unittest.TestCase):

    def setUp(self):
        self.datafile = '/Users/snolia/PycharmProjects/SCM3.0/AthenaTest/datacase/search_datacase/web_frontend_search.xls'

    def test_putInStorageSearch(self):
        '''入库列表查询'''
        datafile = self.datafile
        loadDatas(self, datafile, u'putInStorageSearch')

    def test_outBoundSearch(self):
        '''出库列表查询'''
        datafile = self.datafile
        loadDatas(self, datafile, u'outBoundSearch')

    def test_orderArriveSearch(self):
        '''到件列表查询'''
        datafile = self.datafile
        loadDatas(self, datafile, u'orderArriveSearch')


if __name__ == "__main__":
    unittest.main()
