# -*- coding: UTF-8 -*-
import logging
import os
import time
from datetime import datetime
from logging import handlers

BASE_PATH = os.path.dirname(__file__)
LOG_FILE = "log.log"
LOG_LEVEL = 'info'
sleep_num = 300
project_path = BASE_PATH


class MyLogging(object):
    # 日志级别关系映射
    level_relations = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'crit': logging.CRITICAL
    } 

    def __init__(self, filename, level='info', maxBytes=20 * 1024 * 1024, backCount=10,
                 fmt='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'):
        self.logger = logging.getLogger(filename)
        # 设置日志格式
        format_str = logging.Formatter(fmt)
        # 设置日志级别
        self.logger.setLevel(self.level_relations.get(level))
        # 往屏幕上输出
        sh = logging.StreamHandler()
        # 设置屏幕上显示的格式
        sh.setFormatter(format_str)
        th = handlers.RotatingFileHandler(filename=filename, maxBytes=maxBytes, backupCount=backCount,
                                          encoding='utf-8')
        # 设置文件里写入的格式
        th.setFormatter(format_str)
        # 把对象加到logger里
        self.logger.addHandler(sh)
        self.logger.addHandler(th)


class RunJob:
    def job(self, dir):
        curtime = datetime.now().strftime('%Y%m%d_%H%M%S')
        command_add = 'git add .'
        command_commit = 'git commit -m \'%s\'' % (curtime)
        # command_push = 'git push -u origin master'
        command_push = 'git push'
        os.chdir(dir)
        output_add = os.popen(command_add).read()
        my_log.logger.info(output_add)
        output_commit = os.popen(command_commit).read()
        my_log.logger.info(output_commit)
        output_push = os.popen(command_push).read()
        my_log.logger.info(output_push)
        return


if __name__ == '__main__':
    LOG_PATH = os.path.join(BASE_PATH, 'commit_logs')
    if not os.path.exists(LOG_PATH):
        os.makedirs(LOG_PATH)
    LOG_FULL_NAME = os.path.join(LOG_PATH, LOG_FILE)
    my_log = MyLogging(LOG_FULL_NAME, LOG_LEVEL)
    while True:
        try:
            RunJob().job(project_path)
        except Exception as f:
            my_log.logger.error(f)
        time.sleep(sleep_num)
