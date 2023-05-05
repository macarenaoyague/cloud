from pyspark import SparkContext, SparkConf
import io

conf = SparkConf().setAppName("word_frequency").setMaster("local")
sc = SparkContext(conf=conf)

input_path = "/data/input_file.txt"
output_path = "/data/output_file.txt"

text_rdd = sc.textFile(input_path)
words_rdd = text_rdd.flatMap(lambda line: line.split())
word_count_rdd = words_rdd.map(lambda word: (word.lower(), 1)).reduceByKey(lambda x, y: x + y)
sorted_word_count_rdd = word_count_rdd.sortBy(lambda x: x[1], False)

with io.open(output_path, mode="w", encoding="utf-8") as output_file:
    output_file.write(u"\n".join([u"{0}: {1}".format(x[0], x[1]) for x in sorted_word_count_rdd.collect()]))