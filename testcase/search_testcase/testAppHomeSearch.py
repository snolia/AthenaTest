# -*- coding: utf8 -*-
import unittest
from AthenaTest.common.loadDatas import *

import sys
import importlib
importlib.reload(sys)

class TestAppHomeSearch(unittest.TestCase):

    def setUp(self):
        self.datafile = '/Users/snolia/PycharmProjects/SCM3.0/AthenaTest/datacase/search_datacase/app_home_search.xls'

    def test_homeViewSearch(self):
        '''宜家app:app首页'''
        datafile = self.datafile
        loadDatas(self, datafile, u'homeViewSearch')

if __name__ == "__main__":
    unittest.main()
