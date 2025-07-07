# Data transformation notebook example
from pyspark.sql import functions as F
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

# Assume df is loaded raw data
df = spark.table("raw_data_table")

# Simple transformation example
df_transformed = df.withColumn("ingestion_date", F.current_date())

df_transformed.write.mode("overwrite").saveAsTable("processed_data_table")
