# -*- coding: utf8 -*-
import unittest
from AthenaTest.common.loadDatas import *

import sys
import importlib
importlib.reload(sys)

class TestWebQualityAssuranceSearch(unittest.TestCase):

    def setUp(self):
        self.datafile = '/Users/snolia/PycharmProjects/SCM3.0/AthenaTest/datacase/search_datacase/web_quality_assurance_search.xls'

    def test_qualityStartSearch(self):
        '''质保发起列表查询'''
        datafile = self.datafile
        loadDatas(self, datafile, u'qualityStartSearch')

    def test_qualityHandSearch(self):
        '''质保处理列表查询'''
        datafile = self.datafile
        loadDatas(self, datafile, u'qualityHandSearch')

    def test_qualityTurnSearch(self):
        '''质保转派列表查询'''
        datafile = self.datafile
        loadDatas(self, datafile, u'qualityTurnSearch')

    def test_qualitySubOrderSearch(self):
        '''质保衍生单列表查询'''
        datafile = self.datafile
        loadDatas(self, datafile, u'qualitySubOrderSearch')

if __name__ == "__main__":
    unittest.main()
