#!/usr/bin/env python
#coding=utf-8
import unittest
import sys
import os
import json
import random
import string
from util.config import config, Config, DATA_PATH
from util.mysql_client import mysql_client
from util.https_client import HTTPsClient
from util.log import logger


class insertUser(unittest.TestCase):
    # 错误编码
    __result_code = config.read_data("api_result_code")
    # 当前模块名
    __module = os.path.split(os.path.dirname(os.path.abspath(__file__)))[1]
    # 当前接口名称
    __method = sys._getframe().f_code.co_name
    # URL
    __url = config.get("server", "host") + __module + '/' + __method
    # 当前模块的配置文件
    __config = Config(config=os.path.join(DATA_PATH, __module + '.ini'))
    # 当前接口的参数
    __params = __config.read_data(__method)
    print("inserUser")

    def send(self, params):
        result = HTTPsClient(self.__url).send(params)
        # 直接输出字典会有中文乱码的情况
        # 所以使用json库中的dumps方法
        logger.debug(json.dumps(params, ensure_ascii=False))
        logger.debug(json.dumps(result, ensure_ascii=False))
        return result

    def test_success(self):
        '''测试成功'''
        params = self.__params.copy()
        # params['name'] = ''.join(random.sample(string.ascii_letters + string.digits, 20))
        params['name'] = ''
        code_result = self.send(self.__params)['code']
        self.assertEqual(str(code_result), self.__result_code["STATUS_SUSSECC"])

    def test_name_is_None(self):
        '''name参数为空'''
        params = self.__params.copy()
        params['name'] = None
        code_result = self.send(params)['code']
        self.assertEqual(str(code_result), self.__result_code["USER_INSERT_FAIL_CODE"])

    def test_name_is_empty(self):
        '''name参数为None'''
        params = self.__params.copy()
        params['name'] = ""
        code_result = self.send(params)['code']
        self.assertEqual(str(code_result), self.__result_code["USER_INSERT_FAIL_CODE"])

    def test_name_is_del(self):
        '''name参数为None'''
        params = self.__params.copy()
        del params['name']
        code_result = self.send(params)['code']
        self.assertEqual(str(code_result), self.__result_code["USER_INSERT_FAIL_CODE"])


if __name__ == '__main__':
    unittest.main(verbosity=1)
