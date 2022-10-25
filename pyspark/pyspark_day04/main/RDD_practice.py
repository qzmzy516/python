#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyspark import SparkContext, SparkConf
import os
import re

"""
-------------------------------------------------
   Description :	TODO：远程连接环境
   SourceFile  :	RDD_pretice
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
    # 1、创建一个1 - 10数组的RDD，将所有元素 * 2
    # 形成新的RDD

    # input1 = sc.parallelize(range(1, 11))
    # print(input1.map(lambda x: x * 2).collect())

    # 2、创建一个10 - 20
    # 数组的RDD，使用mapPartitions将所有元素 * 2
    # 形成新的RDD
    # todo 未做出来
    # input2 = sc.parallelize([10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
    # print(input2.mapPartitions(lambda x: x * 2).take(5))

    # 3、创建一个元素为1 - 5的RDD，运用flatMap创建一个新的RDD，新的RDD为原RDD每个元素的平方和三次方来组成1, 1, 4, 8, 9, 27…
    # input3 = sc.parallelize(range(1, 6))
    # print(input3.flatMap(lambda x: (x * x, x ** 3)).collect())

    # 4、创建一个4个分区的RDD数据为Array(10, 20, 30, 40, 50, 60)，使用glom将每个分区的数据放到一个数组

    # input4 = sc.parallelize((10, 20, 30, 40, 50, 60), 4)
    # print(input4.glom().collect())

    # 5、创建一个
    # RDD数据为Array(1, 3, 4, 20, 4, 5, 8)，按照元素的奇偶性进行分组
    # input5 = sc.parallelize((1, 3, 4, 20, 4, 5, 8))
    # result5 = input5.groupBy(lambda x: x % 2).collect()
    # print(sorted([(x, sorted(y)) for (x, y) in result5]))

    # 6、创建一个RDD（由字符串组成）Array("xiaoli", "laoli", "laowang", "xiaocang", "xiaojing", "xiaokong")，
    # 过滤出一个新RDD（包含"xiao"子串）
    # input6 = sc.parallelize(("xiaoli", "laoli", "laowang", "xiaocang", "xiaojing", "xiaokong"))
    # print(input6.filter(lambda x: len(re.findall('\w*xiao\w*', x)) > 0).collect())
    # # 7、创建一个
    # RDD数据为1 to 10，请使用sample不放回抽样
    #
    # 8、创建一个
    # RDD数据为1
    # to
    # 10，请使用sample放回抽样
    #
    # 9、创建一个
    # RDD数据为Array(10, 10, 2, 5, 3, 5, 3, 6, 9, 1), 对
    # RDD
    # 中元素执行去重操作
    # input9 = sc.parallelize((10, 10, 2, 5, 3, 5, 3, 6, 9, 1))
    # print(input9.distinct().collect())

    # 10、创建一个分区数为5的RDD，数据为0to100，之后使用coalesce再重新减少分区的数量至2
    # input10 = sc.parallelize((range(0, 101)), 5)
    # print(input10.getNumPartitions())
    # print(input10.coalesce(2).getNumPartitions())
    # #11、创建一个分区数为5的
    # RDD，数据为0to100，之后使用repartition再重新减少分区的数量至
    # 3
    # input11 = sc.parallelize((range(0, 101)), 5)
    # print(input11.repartition(3).getNumPartitions())

    # 12、创建一个
    # RDD数据为1, 3, 4, 10, 4, 6, 9, 20, 30, 16, 请给RDD进行分别进行升序和降序排列
    # input12 = sc.parallelize((1, 3, 4, 10, 4, 6, 9, 20, 30, 16))
    # print(input12.sortBy(lambda x:x).collect())
    # print(input12.sortBy(lambda x:x,ascending=False).collect())

    # 13、创建两个RDD，分别为rdd1和rdd2数据分别为1to6和4to10，求并集
    rdd1 = sc.parallelize((range(1, 7)))
    rdd2 = sc.parallelize((range(4, 11)))
    # print(rdd1.intersection(rdd2).collect())

    # 14、创建两个RDD，分别为rdd1和rdd2数据分别为1to 6和4to10，计算差集，两个都算
    print(rdd1.filter(lambda x: x == y for y in (rdd1.intersection(rdd2).collect())))
    # 15、创建两个RDD，分别为rdd1和rdd2数据分别为1
    # to
    # 6
    # 和4
    # to
    # 10，计算交集
    #
    # 16、创建两个RDD，分别为rdd1和rdd2数据分别为1
    # to
    # 6
    # 和4
    # to
    # 10，计算
    # 2
    # 个
    # RDD
    # 的笛卡尔积
    #
    # 17、创建两个RDD，分别为rdd1和rdd2数据分别为1
    # to
    # 5
    # 和11
    # to
    # 15，对两个RDD拉链操作
    #
    # 18、创建一个RDD数据为List(("female", 1), ("male", 5), ("female", 5), ("male", 2))，请计算出female和male的总数分别为多少
    #
    # 19、创建一个有两个分区的
    # RDD数据为List(("a", 3), ("a", 2), ("c", 4), ("b", 3), ("c", 6), ("c", 8))，取出每个分区相同key对应值的最大值，然后相加
    #
    # 20、 创建一个有两个分区的
    # pairRDD数据为Array(("a", 88), ("b", 95), ("a", 91), ("b", 93), ("a", 95), ("b", 98))，根据
    # key
    # 计算每种
    # key
    # 的value的平均值
    #
    # 21、统计出每一个省份广告被点击次数的
    # TOP3，数据在access.log文件中
    # 数据结构：时间戳，省份，城市，用户，广告
    # 字段使用空格分割。
    # 样本如下：
    # 1516609143867
    # 6
    # 7
    # 64
    # 16
    # 1516609143869
    # 9
    # 4
    # 75
    # 18
    # 1516609143869
    # 1
    # 7
    # 87
    # 12
    #
    # 22、读取本地文件words.txt, 统计出每个单词的个数，保存数据到
    # hdfs
    # 上
    #
    # 23、读取
    # people.json
    # 数据的文件, 每行是一个
    # json
    # 对象，进行解析输出
    #
    # 24、保存一个
    # SequenceFile
    # 文件，使用spark创建一个RDD数据为Array(("a", 1), ("b", 2), ("c", 3))，保存为SequenceFile格式的文件到hdfs上
    #
    # 25、读取24题的SequenceFile
    # 文件并输出
    #
    # 26、读写
    # objectFile
    # 文件，把
    # RDD
    # 保存为objectFile，RDD数据为Array(("a", 1), ("b", 2), ("c", 3))，并进行读取出来
    #
    # 27、使用内置累加器计算Accumulator.txt文件中空行的数量

    # todo:3-关闭SparkContext
    sc.stop()
