#!/usr/bin/env python
#coding=utf-8
import unittest
import sys
import os
import json
import random
from util.config import config, Config, DATA_PATH
from util.mysql_client import mysql_client
from util.https_client import HTTPsClient
from util.log import logger


class deleteUserById(unittest.TestCase):
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

    @classmethod
    def setUpClass(cls):
        params = {
            "name": "test",
            "password": "123456"
        }
        url = config.get("server", "host") + cls.__module + '/' + 'insertUser'
        result = HTTPsClient(url).send(params)
        deleteUserById.user_id = result["data"]["id"]

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
        params['id'] = deleteUserById.user_id
        response = self.send(params)
        code_result = response['code']
        self.assertEqual(str(code_result), self.__result_code["STATUS_SUCCESS_CODE"])

    def test_id_not_exist(self):
        '''id不存在'''
        params = self.__params.copy()
        params['id'] = 12345678910
        response = self.send(params)
        code_result = response['code']
        self.assertEqual(str(code_result), self.__result_code["USER_DELETE_FAIL_CODE"])

    def test_id_type_is_string(self):
        '''id类型为string类型'''
        params = self.__params.copy()
        params['id'] = "test"
        response = self.send(params)
        code_result = response['code']
        self.assertEqual(str(code_result), self.__result_code["USER_DELETE_FAIL_CODE"])

    def test_id_is_None(self):
        '''id为None'''
        params = self.__params.copy()
        params['id'] = None
        response = self.send(params)
        code_result = response['code']
        self.assertEqual(str(code_result), self.__result_code["USER_DELETE_FAIL_CODE"])

    def test_id_is_empty(self):
        '''id为空'''
        params = self.__params.copy()
        params['id'] = ""
        response = self.send(params)
        code_result = response['code']
        self.assertEqual(str(code_result), self.__result_code["USER_DELETE_FAIL_CODE"])


if __name__ == '__main__':
    unittest.main(verbosity=1)
