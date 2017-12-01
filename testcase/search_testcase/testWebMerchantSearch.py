# -*- coding: utf8 -*-
import unittest
from AthenaTest.common.loadDatas import *

import sys
import importlib
importlib.reload(sys)

class TestWebMerchantSearch(unittest.TestCase):

    def setUp(self):
        self.datafile = '/Users/snolia/PycharmProjects/SCM3.0/AthenaTest/datacase/search_datacase/web_merchant_system_search.xls'

    def test_merchantSearch(self):
        '''商家列表查询'''
        datafile = self.datafile
        loadDatas(self, datafile, u'merchantSearch')


if __name__ == "__main__":
    unittest.main()
