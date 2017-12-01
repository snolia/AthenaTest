# -*- coding: utf8 -*-
import unittest
from AthenaTest.common.loadDatas import *

import sys
import importlib
importlib.reload(sys)

class TestWebIkeaServiceManageSearch(unittest.TestCase):

    def setUp(self):
        self.datafile = '/Users/snolia/PycharmProjects/SCM3.0/AthenaTest/datacase/search_datacase/web_ikea_service_manage_search.xls'

    def test_installOrderSearch(self):
        '''宜家安装管理：安装订单列表'''
        datafile = self.datafile
        loadDatas(self, datafile, u'installOrderSearch')

    def test_lockOrderSearch(self):
        '''宜家安装管理：安装锁定'''
        datafile = self.datafile
        loadDatas(self, datafile, u'lockOrderSearch')

    def test_waitCheckOrderSearch(self):
        '''宜家安装管理：安装审单'''
        datafile = self.datafile
        loadDatas(self, datafile, u'waitCheckOrderSearch')

    def test_installMeltOrderSearch(self):
        '''宜家安装管理：安装销单列表'''
        datafile = self.datafile
        loadDatas(self, datafile, u'installMeltOrderSearch')
        
if __name__ == "__main__":
    unittest.main()
