#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
线程
"""
import threading

class MyThread(threading.Thread):
    """
    线程类
    """
    def __init__(self, func, args):
        """
        初始化
        """
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.res = None

    def run(self):
        """
        执行
        """
        self.res = self.func(self.args)

    def getResult(self):
        """
        获取结果
        """
        return self.res