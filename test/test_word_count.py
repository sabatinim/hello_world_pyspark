import unittest
from typing import Tuple

from pyspark import SparkContext, RDD, Row
from pyspark.sql import SparkSession


class TestApp(unittest.TestCase):
    def test_word_count(self):
        spark = SparkSession(SparkContext("local", "PySpark Word Count dockerized!"))
        words = spark.sparkContext.textFile("/code/raw/input.txt").flatMap(lambda line: line.split(" "))

        words \
            .map(lambda word: (word, 1)) \
            .reduceByKey(lambda a, b: a + b) \
            .map(lambda t: (str(t[0]), int(t[1]))) \
            .toDF(["word", "count"]) \
            .write \
            .parquet("/tmp/golden.parquet")

        actual = spark.read.parquet("/tmp/golden.parquet").collect()
        self.assertEqual([Row(word='one', count=4),
                          Row(word='two', count=1),
                          Row(word='three', count=3),
                          Row(word='four', count=1),
                          Row(word='five', count=1),
                          Row(word='six', count=1)], actual)
