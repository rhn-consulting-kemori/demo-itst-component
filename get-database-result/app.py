# -*- coding: utf-8 -*-
import psycopg2
import os

# Environment Parameter
host = os.getenv('DB_HOST', '127.0.0.1')
dbName = os.getenv('DB_NAME', 'postgres')
user = os.getenv('DB_USER', 'postgres')
password = os.getenv('DB_PASS', 'postgres')
port = os.getenv('DB_PORT', '5432')
# ---
inputFilePath = os.getenv('INPUT_FILE_PATH', './')
inputFileName = os.getenv('INPUT_FILE_NAME', 'assert-actual-002-test_task_run.sql')
outputFilePath = os.getenv('OUTPUT_FILE_PATH', './')
outputFileName = os.getenv('OUTPUT_FILE_NAME', 'assert-actual-002-test_task_run.csv')

# File Read
input_f = open(inputFilePath + inputFileName, 'r', encoding='UTF-8')
sql_data = input_f.read()
input_f.close()

# SQL
outputquery = "COPY ({0}) TO STDOUT WITH CSV".format(sql_data)

# RUN SQL
connection = psycopg2.connect(host=host, dbname=dbName, user=user, password=password, port=port)
cursor = connection.cursor()
with open(outputFilePath + outputFileName, "w") as output_f:
    cursor.copy_expert(outputquery, output_f)
