#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
入口文件
"""
from library import file
from library import myThread
from consts import code
import string


def run_one(file_path):
    """
    单个文件执行入口函数
    """
    # 获取文件后缀
    suffix_name = file.get_file_suffix_name(file_path)
    # 判断后缀名是否在允许范围内
    if suffix_name not in code.SUFFIX_NAME_PROGRAM_LANGUAGE_DICT:
        print "this programming language not support now"
        return
    # 自动加载类
    code_name = code.SUFFIX_NAME_PROGRAM_LANGUAGE_DICT[suffix_name]
    exec("from calcx import %s" % (code_name))
    class_name = getattr(eval(code_name), string.capwords(code_name))
    # 类对象
    class_obj = class_name(file_path)
    # 执行结果
    return class_obj()

def run(path):
    """
    入口函数
    """
    #根据路径获取文件
    file_path_list = file.get_dir_file_name(path)
    # 线程池
    threads = []
    # 结果保存
    batch_result = {}
    # 并发执行
    for idx in range(len(file_path_list)):
        thd = myThread.MyThread(func=run_one, args=file_path_list[idx])
        threads.append(thd)
        batch_result[idx] = {"file": file_path_list[idx]}
    for thd in threads:
        # 循环启动线程
        thd.start()

    for idx in range(len(threads)):
        # 设置子线程超时2秒
        thd.join()
        batch_result[idx]["result"] = threads[idx].getResult()
    return batch_result
    

if __name__ == "__main__":
    print run("/home/work/script/index_cp.py")
