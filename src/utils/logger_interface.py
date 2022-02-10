import logging
from logging import getLogger

class LoggerInterface(object):
    '''日志接口'''
    def __init__(self, name=None, logging_level=None):
        # 日志基础配置
        logging.basicConfig(format='[%(name)s][%(levelname)s]: %(message)s')
        # 创建logger
        if name is None:
            # 设置name为类名
            name = self.__class__.__name__
        self.logger = getLogger(name)
        # 设置日志等级
        if logging_level is None:
            self.logger.setLevel(logging.INFO)
        else:
            self.logger.setLevel(logging_level)        
