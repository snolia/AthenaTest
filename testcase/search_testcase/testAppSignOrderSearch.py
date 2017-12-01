# -*- coding: utf8 -*-
import unittest
from  AthenaTest.common.loadDatas import *

import sys
import importlib
importlib.reload(sys)

class TestAppSignOrderSearch(unittest.TestCase):

    def setUp(self):
        self.datafile = '/Users/snolia/PycharmProjects/SCM3.0/AthenaTest/datacase/search_datacase/app_sign_order_search.xls'

    def test_signedOrderSearch(self):
        '''已签收订单'''
        datafile = self.datafile
        loadDatas(self, datafile, u'signedOrderSearch')

if __name__ == "__main__":
    unittest.main()
