from pyspark.sql import SparkSession


class WordCountJob:

    def __init__(self, spark: SparkSession):
        self._spark = spark

    def execute(self, src: str, dst: str):
        self._spark \
            .sparkContext \
            .textFile(src) \
            .flatMap(lambda line: line.split(" ")) \
            .map(lambda word: (word, 1)) \
            .reduceByKey(lambda a, b: a + b) \
            .map(lambda t: (str(t[0]), int(t[1]))) \
            .toDF(["word", "count"]) \
            .write \
            .parquet(dst)
