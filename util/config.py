#!/usr/bin/env python
#coding=utf-8
import os
import ConfigParser

# 配置项目文件路径，增加可移植性
BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
CASE_PATH = os.path.join(BASE_PATH,'case')
LOG_PATH = os.path.join(BASE_PATH,'log')
REPORT_PATH = os.path.join(BASE_PATH,'report')
DATA_PATH = os.path.join(BASE_PATH,'data')
CONFIG_FILE = os.path.join(BASE_PATH,'conf','conf.ini')


class FileNotFoundError(StandardError):
    pass


class myconf(ConfigParser.ConfigParser):
    # 重写ConfigParser.ConfigParser()类中的optionxform函数
    # 使其支持option名称区分大小写
    def __init__(self,defaults=None):
        ConfigParser.ConfigParser.__init__(self,defaults=None)

    def optionxform(self, optionstr):
        return optionstr


class Config(object):
    # 读取配置文件
    def __init__(self, config=CONFIG_FILE):
        #   判断路径中是否存在文件
        if os.path.exists(config):
            self.conf_file = config
        else:
            info = ('Config File not found!%s' % config)
            raise FileNotFoundError(info)
        self._data = None
        self.config = myconf()
        self.config.read(config)

    # 根据传入的session和option，返回相应的属性
    # 例如：get('database', 'port')
    # return 3306
    def get(self, session, option):
        try:
            result = self.config.get(session, option)
        except (ConfigParser.NoSectionError, ConfigParser.NoOptionError) as e:
            print('请检查配置文件参数是否正确:')
            print('session:%s, option:%s') % (session, option)
            print(repr(e))
            return
        return result

    def read_data(self, section):
        params = dict(self.config.items(section))
        return params

config = Config()


if __name__ == '__main__':
    result =  Config().get('database', 'port')
    print result
    print type(result)
    print BASE_PATH
    # dict(config.read_data('database'))
