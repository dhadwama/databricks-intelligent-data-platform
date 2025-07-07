# ML model training notebook example
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.feature import VectorAssembler
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

# Load processed data
df = spark.table("processed_data_table")

# Prepare features
assembler = VectorAssembler(inputCols=["feature1", "feature2"], outputCol="features")
training_data = assembler.transform(df)

# Train a logistic regression model
lr = LogisticRegression(featuresCol="features", labelCol="label")
model = lr.fit(training_data)

# Save the model
model.save("/dbfs/models/logistic_regression_model")
