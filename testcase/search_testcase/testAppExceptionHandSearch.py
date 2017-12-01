# -*- coding: utf8 -*-
import unittest
from AthenaTest.common.loadDatas import *

import sys
import importlib
importlib.reload(sys)

class TestAppExceptionHandSearch(unittest.TestCase):

    def setUp(self):
        self.datafile = '/Users/snolia/PycharmProjects/SCM3.0/AthenaTest/datacase/search_datacase/app_exception_hand_search.xls'

    def test_abnormalTodoSearch(self):
        '''异常待办：待处理列表'''
        datafile = self.datafile
        loadDatas(self, datafile, u'abnormalTodoSearch')

    def test_abnormalTrackSearch(self):
        '''异常待办：异常追踪列表'''
        datafile = self.datafile
        loadDatas(self, datafile, u'abnormalTrackSearch')

    def test_abnormalEndSearch(self):
        '''异常待办：已完结列表'''
        datafile = self.datafile
        loadDatas(self, datafile, u'abnormalEndSearch')

if __name__ == "__main__":
    unittest.main()
