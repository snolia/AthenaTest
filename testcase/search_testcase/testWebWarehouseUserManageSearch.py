# -*- coding: utf8 -*-
import unittest
from AthenaTest.common.loadDatas import *

import sys
import importlib
importlib.reload(sys)

class TestWebWarehouseUserManageSearch(unittest.TestCase):

    def setUp(self):
        self.datafile = '/Users/snolia/PycharmProjects/SCM3.0/AthenaTest/datacase/search_datacase/web_warehouse_user_manage_search.xls'

    def test_accountListSearch(self):
        '''账号列表、账号列表详情'''
        datafile = self.datafile
        loadDatas(self, datafile, u'accountListSearch')

    def test_myAcountSearch(self):
        '''我的账号、我的账号详情'''
        datafile = self.datafile
        loadDatas(self, datafile, u'myAcountSearch')

    def test_roleManageSearch(self):
        '''角色管理'''
        datafile = self.datafile
        loadDatas(self, datafile, u'roleManageSearch')


        # 这块移动到loadDatas中进行处理
        #errortest = loadDatas(self, datafile, u'addData')
        #print(errortest)
        #for result in errortest:
            #with self.subTest(data=result):  # 注意subTest的用法
                #self.assertEqual(result, "pass")


if __name__ == "__main__":
    unittest.main()



