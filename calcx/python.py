#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
编程语言为Python时，圈复杂度计算
"""
from cycle_complexity_base import CycleComplexityBase
import re

class Python(CycleComplexityBase):
    """
    python计算
    """
    def __init__ (self, file_path):
        """
        初始化
        """
        super(Python, self).__init__(file_path)
        self.class_name = "class"
        self.func_name = "def"
        # 判定规则
        self.judge_rules = {
            "if": 1,
            "elif": 1,
            "while": 1,
            "for": 1,
            "try": 1,
            "except": 1,
        }
        # 非函数内标识
        self.out_func_label = ["if", "while", "for", "try"]


    def calc_cycle_complexity(self):
        """
        计算圈复杂度
        return: 列表
        """
        func_name = ""
        # 函数空格数
        func_name_blank_num = 0
        key = ""
        # 返回结果
        ret = []
        # 圈复杂度计数
        count = 1
        if len(self.file_content) <= 0:
            return ret
        for idx in range(len(self.file_content)):
            line_value_list = [val for val in re.split(" |:", self.file_content[idx].strip()) if len(val) > 0]
            # 函数
            if self.func_name in line_value_list:
                func_name_blank_num = self.get_blank_num_by_str(self.file_content[idx])
                if count > 0 and len(key) > 0:
                    ret.append((key, count))
                if len(line_value_list) >= 2:
                    func_name = line_value_list[1].split("(")[0]
                    key = "%s:%d" % (func_name, idx)
                count = 1
            for k, v in self.judge_rules.items():
                # 存在标识
                if k in line_value_list:
                    if k in self.out_func_label:
                        blank_num = self.get_blank_num_by_str(self.file_content[idx])
                        if len(func_name) <= 0 or blank_num <= func_name_blank_num:
                            if count > 0 and len(key) > 0:
                                ret.append((key, count))
                            key = "%s:%d" % (k, idx)
                            count = v + 1
                        else:
                            count += v
                    else:
                        count += v
                    break
        if count > 0 and len(key) > 0:
            ret.append((key, count))
        return ret


    def get_blank_num_by_str(self, line):
        """
        获取每一行前缀空格数
        """    
        count = 0
        for v in line:
            if v != " ":
                break
            count += 1
        return count
            


