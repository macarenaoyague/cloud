FROM ubuntu:16.04

RUN apt-get update && \
    apt-get install -y openjdk-8-jdk wget python2.7 python-pip

RUN wget https://archive.apache.org/dist/spark/spark-1.5.2/spark-1.5.2-bin-hadoop2.6.tgz && \
    tar -xvzf spark-1.5.2-bin-hadoop2.6.tgz && \
    rm spark-1.5.2-bin-hadoop2.6.tgz && \
    mv spark-1.5.2-bin-hadoop2.6 /spark

COPY WordCount.py /WordCount.py
COPY input_file.txt /data/input_file.txt

ENV SPARK_HOME /spark
ENV PATH $SPARK_HOME/bin:$PATH
ENV PYSPARK_PYTHON /usr/bin/python2.7

ENTRYPOINT ["spark-submit", "--master", "local[*]", "/WordCount.py"]