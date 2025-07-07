# Data ingestion notebook example
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

# Example: Read raw data from Azure Blob Storage
raw_data_path = "wasbs://<container>@<storage-account>.blob.core.windows.net/raw-data/"
df = spark.read.format("csv").option("header", "true").load(raw_data_path)

df.show(5)
