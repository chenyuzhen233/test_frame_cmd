#coding=utf-8
import logging
from config import config, LOG_PATH
import os,time
import sys
reload(sys)
sys.setdefaultencoding('utf8')


class Logger(object):
    def __init__(self):
        c = config
        self.log_path = os.path.dirname(os.path.abspath(__file__))
        logger_name = c.get('log', 'logger_name') if c and c.get('log', 'logger_name') else 'TEST'
        self.logger = logging.getLogger(logger_name)
        #   设置默认等级,文件名
        logging.root.setLevel(logging.NOTSET)
        self.file_name = c.get('log', 'file_name') if c and c.get('log', 'file_name') else 'test_log'
        self.current_time = time.strftime('_%Y%m%d',time.localtime())
        #   设置控制台，文件日志等级
        # self.console_output_level = c.get('log', 'console_level') if c and c.get('log', 'console_level') \
        #     else logging.INFO
        self.file_output_level = c.get('log', 'file_level') if c and c.get('log', 'file_level') else logging.DEBUG
        #   设置日志格式
        self.pattern = '[%(asctime)s][%(levelname)s] %(message)s'
        self.fmt = logging.Formatter(self.pattern, "%Y-%m-%d %H:%M:%S")

    def get_logger(self):
        #   防止反复添加handler
        if not self.logger.handlers:
            #   添加控制台handler，设置默认输出日志等级，日志格式
            # console_handler = logging.StreamHandler()
            # console_handler.setLevel(self.console_output_level)
            # console_handler.setFormatter(self.fmt)
            # self.logger.addHandler(console_handler)

            #   添加文件handler，设置默认输出日志等级，日志格式
            file_handler = logging.FileHandler(filename=(os.path.join(LOG_PATH, self.file_name+self.current_time+".log")),
                                               encoding='utf-8')
            file_handler.setLevel(self.file_output_level)
            file_handler.setFormatter(self.fmt)
            self.logger.addHandler(file_handler)
        return self.logger

logger = Logger().get_logger()

if __name__ == '__main__':
    logger.info("test....")
