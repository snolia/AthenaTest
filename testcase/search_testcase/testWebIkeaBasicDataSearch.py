# -*- coding: utf8 -*-
import unittest
from AthenaTest.common.loadDatas import *

import sys
import importlib
importlib.reload(sys)

class TestWebIkeaBasicDataSearch(unittest.TestCase):

    def setUp(self):
        self.datafile = '/Users/snolia/PycharmProjects/SCM3.0/AthenaTest/datacase/search_datacase/web_ikea_basic_data_search.xls'

    def test_ikeaCarInfoSearch(self):
        '''宜家基础资料：车辆与司机列表'''
        datafile = self.datafile
        loadDatas(self, datafile, u'ikeaCarInfoSearch')

    def test_ikeaWorkerSearch(self):
        '''宜家基础资料：安装工人列表'''
        datafile = self.datafile
        loadDatas(self, datafile, u'ikeaWorkerSearch')
        
if __name__ == "__main__":
    unittest.main()
