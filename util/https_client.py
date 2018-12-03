#coding=utf-8
import requests
import time
import json
import warnings
from config import config
from log import logger
warnings.simplefilter("ignore")


class HTTPsClient(object):
    def __init__(self, url):
        self.url = url
        self.session = requests.session()
        self.timeout = float(config.read_data('server')['timeout'])

    def send(self, data=None, **kwargs):
        flag = False
        response = None
        while not flag:
            try:
                print(self.url, data)
                response = self.session.request(method='POST', url=self.url, data=data, **kwargs)
                if response.elapsed.total_seconds() > self.timeout:
                    raise BaseException(u'request timeout！elapsed time：%s' % response.elapsed.total_seconds())
            except requests.exceptions.ConnectionError:
                print(u'HTTP连接失败！！！正在准备重发。。。')
                logger.error(u'HTTP连接失败！！！正在准备重发。。。')
                time.sleep(5)
                continue
            flag = True
        self.session.close()
        try:
            result = json.loads(str(response.text))
        except ValueError, e:
            logger.error('\n%s\n%s\n%s\n%s' % (repr(e), self.url, data, response.text))
            result = response.text
        return result
