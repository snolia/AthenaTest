# -*- coding: utf8 -*-
import unittest
from AthenaTest.common.loadDatas import *

import sys
import importlib
importlib.reload(sys)

class TestWebIkeaShipmentManageSearch(unittest.TestCase):

    def setUp(self):
        self.datafile = '/Users/snolia/PycharmProjects/SCM3.0/AthenaTest/datacase/search_datacase/web_ikea_shipment_manage_search.xls'

    def test_deliveryOrderSearch(self):
        '''宜家配送管理：配送订单列表'''
        datafile = self.datafile
        loadDatas(self, datafile, u'deliveryOrderSearch')

    def test_outAssignOrderSearch(self):
        '''宜家配送管理：外埠指派'''
        datafile = self.datafile
        loadDatas(self, datafile, u'outAssignOrderSearch')

    def test_deliveryMeltOrderSearch(self):
        '''宜家配送管理：配送销单列表'''
        datafile = self.datafile
        loadDatas(self, datafile, u'deliveryMeltOrderSearch')
        
if __name__ == "__main__":
    unittest.main()
