import os
import sys
import re
from pyspark import SparkContext, SparkConf

# 配置环境变量
if __name__ == "__main__":
    # 修改所有集群环境变量
    os.environ['JAVA_HOME'] = '/export/server/jdk'
    os.environ['HADOOP_HOME'] = '/export/server/hadoop'
    os.environ['PYSPARK_PYTHON'] = '/export/server/anaconda3/bin/python3'
    os.environ['PYSPARK_DRIVER_PYTHON'] = '/export/server/anaconda3/bin/python3'

    # 修改运行模式为集群
    conf = SparkConf().setMaster("spark://node1.itcast.cn:7077").setAppName("RemoteTest")
    sc = SparkContext(conf=conf)
    # todo:2-数据处理：读取、转换、保存
    # step1: 读取数据
    input_rdd = sc.textFile("hdfs://node1:8020/spark/wordcount/input")
    # step2: 处理数据
    result_rdd = (input_rdd.filter(lambda x: len(x.strip()))
                  .flatMap(lambda x: re.split('\\s+', x.strip()))
                  .map(lambda x: (x, 1))
                  .reduceByKey(lambda x, y: x + y)
                  )
    # step3: 保存结果
    result_rdd.foreach(lambda x: print(x))
    result_rdd.saveAsTextFile("hdfs://node1:8020/spark/wordcount/output3")
    # todo:3-关闭SparkContext
    sc.stop()
