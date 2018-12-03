#coding=utf-8
import os
import time
import unittest
from util.config import config, CASE_PATH, REPORT_PATH
from util import HTMLTestResult2


def all_case():
    discover = unittest.defaultTestLoader.discover(CASE_PATH, pattern="test*.py", top_level_dir=None)
    return discover

if __name__ == '__main__':
    result =  all_case()

    current_time = time.strftime('_%Y%m%d%H%M',time.localtime())

    file_name = config.get("log", "file_name")

    report_abspath = os.path.join(REPORT_PATH, file_name+current_time+".html")

    print(result)

    fp = open(report_abspath, "wb")
    runner = HTMLTestResult2.HTMLTestRunner(stream=fp,
                                           verbosity=2,
                                           title=u'接口自动化测试报告,测试结果如下：',
                                           description=u'用例执行情况：')
    runner.run(result)
    fp.close()