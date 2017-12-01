# -*- coding: utf8 -*-
import unittest
from AthenaTest.common.loadDatas import *

import sys
import importlib
importlib.reload(sys)

class TestWebIkeaDispatchManageSearch(unittest.TestCase):

    def setUp(self):
        self.datafile = '/Users/snolia/PycharmProjects/SCM3.0/AthenaTest/datacase/search_datacase/web_ikea_dispatch_manage_search.xls'

    def test_deliveryOrderDispatchSearch(self):
        '''宜家调度：配送调度列表'''
        datafile = self.datafile
        loadDatas(self, datafile, u'deliveryOrderDispatchSearch')

    def test_installOrderDispatchSearch(self):
        '''宜家调度：安装调度列表'''
        datafile = self.datafile
        loadDatas(self, datafile, u'installOrderDispatchSearch')

    def test_samsOrderDispatchSearch(self):
        '''宜家调度：SMAS调度列表'''
        datafile = self.datafile
        loadDatas(self, datafile, u'samsOrderDispatchSearch')
        
if __name__ == "__main__":
    unittest.main()
