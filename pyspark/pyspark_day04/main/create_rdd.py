#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyspark import SparkContext, SparkConf
import os

"""
-------------------------------------------------
   Description :	TODO：远程连接环境
   SourceFile  :	create_rdd
   Author      :	MZY
   Date	       :	2022/10/24
-------------------------------------------------
"""

if __name__ == '__main__':
    # todo:0-设置系统环境变量:全部换成Linux地址
    os.environ['JAVA_HOME'] = '/export/server/jdk'
    os.environ['HADOOP_HOME'] = '/export/server/hadoop'
    os.environ['PYSPARK_PYTHON'] = '/export/server/anaconda3/bin/python3'
    os.environ['PYSPARK_DRIVER_PYTHON'] = '/export/server/anaconda3/bin/python3'

    # todo:1-构建SparkContext
    conf = SparkConf().setMaster("local[2]").setAppName("Remote Test APP")
    sc = SparkContext(conf=conf)

    # todo:2-数据处理：读取、转换、保存
    # step1: 读取数据
    datas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    input_rdd = sc.parallelize(datas)
    input_rdd.foreach(lambda x: print(x))
    # step2: 处理数据
    # step3: 保存结果

    # todo:3-关闭SparkContext
    sc.stop()
