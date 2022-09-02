#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
文件相关通用函数库
"""
import os

def get_file_suffix_name(file_path):
    """
        desc: 获取文件后缀名
        input: file_path string 文件路径
        return: _ string 后缀名
    """
    # 判断输入路径是否是文件目录或者输入参数非字符串类型, 如果不是，直接返回空字符串
    if os.path.isdir(file_path) or not isinstance(file_path, str):
        return ""
    listS = file_path.strip().split(".")
    if len(listS) > 0:
        return listS[-1]
    
    return ""


def get_dir_file_name(dir_path):
    """
        desc:获取当前目录或者文件下所有文件名称，如果路径是文件，返回文件
        input: dir_path string 目录
        return: _ string 以列表的形式返回所有文件的内容
    """
    result = []
    if os.path.exists(dir_path):
        if os.path.isdir(dir_path):
            for file_name in os.listdir(dir_path):
                # 非文件夹
                if not os.path.isdir(file_name):
                    # 返回绝对路径
                    result.append(dir_path + '/' + file_name)
        if os.path.isfile(dir_path):
            result.append(dir_path)
    return result