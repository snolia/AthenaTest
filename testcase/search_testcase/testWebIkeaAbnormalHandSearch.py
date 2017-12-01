# -*- coding: utf8 -*-
import unittest
from AthenaTest.common.loadDatas import *

import sys
import importlib
importlib.reload(sys)

class TestWebIkeaAbnormalHandSearch(unittest.TestCase):

    def setUp(self):
        self.datafile = '/Users/snolia/PycharmProjects/SCM3.0/AthenaTest/datacase/search_datacase/web_ikea_abnormal_hand_search.xls'

    def test_initiatedAbnormalSearch(self):
        '''宜家异常处理：已发起异常'''
        datafile = self.datafile
        loadDatas(self, datafile, u'initiatedAbnormalSearch')

    def test_samsReturnSearch(self):
        '''宜家异常处理：SAMS退货'''
        datafile = self.datafile
        loadDatas(self, datafile, u'samsReturnSearch')

    def test_outReturnSearch(self):
        '''宜家异常处理：内部退货'''
        datafile = self.datafile
        loadDatas(self, datafile, u'outReturnSearch')

    def test_changeMessageSearch(self):
        '''宜家异常处理：变更通知'''
        datafile = self.datafile
        loadDatas(self, datafile, u'changeMessageSearch')

if __name__ == "__main__":
    unittest.main()
