import os
import sys
import re
from pyspark import SparkContext, SparkConf

# 配置环境变量
if __name__ == "__main__":
    # 配置JDK的路径
    os.environ['JAVA_HOME'] = 'D:/jdk1.8.0_241'
    # 配置Hadoop的路径
    os.environ['HADOOP_HOME'] = 'D:/hadoop-3.3.0'
    # 配置base环境Python解析器的路径
    os.environ['PYSPARK_PYTHON'] = 'D:/Miniconda3/python.exe'
    # 配置base环境Python解析器的路径
    os.environ['PYSPARK_DRIVER_PYTHON'] = 'D:/Miniconda3/python.exe'
    # todo:1-构建SparkContext

    conf = SparkConf().setAppName('APP_name').setMaster('local[2]')
    sc = SparkContext(conf=conf)

    # todo:2-数据处理：读取、转换、保存
    # step1: 读取数据
    input_rdd = sc.textFile(r'..\datas\wordcount\word_rep.txt')
    # step2: 处理数据
    result_rdd = (input_rdd.filter(lambda x: len(x.strip()))
                  .flatMap(lambda x: re.split('\\s+', x.strip()))
                  .map(lambda x: (x, 1))
                  .reduceByKey(lambda x, y: x + y)
                  )
    # step3: 保存结果
    # result_rdd.foreach(lambda x: print(x))
    result_rdd.saveAsTextFile(path=r'..\datas\wordcount\output1')
    # todo:3-关闭SparkContext

    sc.stop()
