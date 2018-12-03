#!/usr/bin/env python
#coding=utf-8
import unittest


class TestCase(unittest.TestCase):

    def test_success(self):
        print("test_success")

    def test_id_not_exist(self):
        print("test_id_not_exist")

    def test_id_type_is_string(self):
        print("test_id_type_is_string")

    def test_id_is_None(self):
        print("test_id_is_None")

    def test_id_is_empty(self):
        print("test_id_is_empty")


if __name__ == '__main__':
    unittest.main(verbosity=2)
