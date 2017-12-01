# -*- coding: utf8 -*-
import sys
import importlib
importlib.reload(sys)

import time,sys
sys.path.append('./SCM3.0')

import unittest
from HTMLTestRunner import HTMLTestRunner

# 指定测试用例为当前文件夹下的 interface 目录
test_dir = './testcase/search_testcase'
discover = unittest.defaultTestLoader.discover(test_dir,pattern = 'test*.py')

if __name__ == "__main__":
	now = time.strftime("%Y-%m-%d %H_%M_%S")
	filename = './report/' + now + 'result.html'
	fp = open(filename, 'wb')
	runner = HTMLTestRunner(stream=fp,
							title='泛家居供应链管理系统接口测试报告')
	runner.run(discover)
	fp.close()