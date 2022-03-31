import unittest

from pyspark import SparkContext, Row
from pyspark.sql import SparkSession

from jobs.word_count import WordCountJob
import shutil


class TestApp(unittest.TestCase):
    def setUp(self) -> None:
        shutil.rmtree("/tmp/golden", ignore_errors=True)

    def test_word_count(self):
        spark = SparkSession(SparkContext("local", "PySpark Word Count dockerized!"))

        WordCountJob(spark).execute(
            src="/code/raw/input.txt",
            dst="/tmp/golden/output.parquet"
        )

        self.assertEqual([Row(word='one', count=4),
                          Row(word='two', count=1),
                          Row(word='three', count=3),
                          Row(word='four', count=1),
                          Row(word='five', count=1),
                          Row(word='six', count=1)], spark.read.parquet("/tmp/golden/output.parquet").collect())
