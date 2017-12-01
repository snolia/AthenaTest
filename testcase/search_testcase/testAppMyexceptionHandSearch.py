# -*- coding: utf8 -*-
import unittest
from AthenaTest.common.loadDatas import *

import sys
import importlib
importlib.reload(sys)

class TestAppMyexceptionHandSearch(unittest.TestCase):

    def setUp(self):
        self.datafile = '/Users/snolia/PycharmProjects/SCM3.0/AthenaTest/datacase/search_datacase/app_myexception_hand_search.xls'

    def test_mySponsorAbnormalSearch(self):
        '''我的异常：我的发起列表'''
        datafile = self.datafile
        loadDatas(self, datafile, u'mySponsorAbnormalSearch')

    def test_myAbnormalTodoSearch(self):
        '''我的异常：我的待办列表'''
        datafile = self.datafile
        loadDatas(self, datafile, u'myAbnormalTodoSearch')

    def test_myAbnormalEndSearch(self):
        '''我的异常：已完结列表'''
        datafile = self.datafile
        loadDatas(self, datafile, u'myAbnormalEndSearch')

if __name__ == "__main__":
    unittest.main()
