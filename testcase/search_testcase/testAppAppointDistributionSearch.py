# -*- coding: utf8 -*-
import unittest
from AthenaTest.common.loadDatas import *

import sys
import importlib
importlib.reload(sys)

class TestAppAppointDistributionSearch(unittest.TestCase):

    def setUp(self):
        self.datafile = '/Users/snolia/PycharmProjects/SCM3.0/AthenaTest/datacase/search_datacase/app_appoint_distribution_search.xls'

    def test_alreadyArriveSearch(self):
        '''已到件'''
        datafile = self.datafile
        loadDatas(self, datafile, u'alreadyArriveSearch')

    def test_alreadyAppointSearch(self):
        '''已预约'''
        datafile = self.datafile
        loadDatas(self, datafile, u'alreadyAppointSearch')

    def test_serviceOrderSearch(self):
        '''服务中'''
        datafile = self.datafile
        loadDatas(self, datafile, u'serviceOrderSearch')

    def test_orderNotArriveSearch(self):
        '''未到件'''
        datafile = self.datafile
        loadDatas(self, datafile, u'orderNotArriveSearch')

if __name__ == "__main__":
    unittest.main()
