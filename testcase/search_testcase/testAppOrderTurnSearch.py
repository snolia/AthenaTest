# -*- coding: utf8 -*-
import unittest
from AthenaTest.common.loadDatas import *

import sys
import importlib
importlib.reload(sys)

class TestAppOrderTurnSearch(unittest.TestCase):

    def setUp(self):
        self.datafile = '/Users/snolia/PycharmProjects/SCM3.0/AthenaTest/datacase/search_datacase/app_order_turn_search.xls'

    def test_orderTurnAuditSearch(self):
        '''转单审核'''
        datafile = self.datafile
        loadDatas(self, datafile, u'orderTurnAuditSearch')

    def test_auditRecordSearch(self):
        '''审核记录'''
        datafile = self.datafile
        loadDatas(self, datafile, u'auditRecordSearch')


if __name__ == "__main__":
    unittest.main()
