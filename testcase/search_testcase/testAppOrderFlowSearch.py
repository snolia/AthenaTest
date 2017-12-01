# -*- coding: utf8 -*-
import unittest
from AthenaTest.common.loadDatas import *

import sys
import importlib
importlib.reload(sys)

class TestAppOrderFlowSearch(unittest.TestCase):

    def setUp(self):
        self.datafile = '/Users/snolia/PycharmProjects/SCM3.0/AthenaTest/datacase/search_datacase/app_order_flow_search.xls'

    def test_clearingFlowSearch(self):
        '''订单流水：结算流水列表'''
        datafile = self.datafile
        loadDatas(self, datafile, u'clearingFlowSearch')

if __name__ == "__main__":
    unittest.main()
