#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
计算单个文件的圈复杂度
"""


class CycleComplexityBase(object):
    """
    圈复杂度基类
    """
    def __init__(self, file_path):
        # 文件路径
        self.file_path = file_path
        # 读取文件内容
        try:
            with open(self.file_path, 'r') as fp:
                self.file_content = fp.readlines()
        except:
            self.file_content = []
        # 判定规则
        self.judge_rules = {}
        # 类标识
        self.class_name = ""
        # 函数标识
        self.func_name = ""


    def calc_cycle_complexity(self):
        """
        计算圈复杂度
        """
        pass
        return []


    def __call__(self):
        """
        类回调入口
        """
        return self.calc_cycle_complexity()



