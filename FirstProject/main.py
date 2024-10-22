import pyspark
from pyspark.sql.types import IntegerType
from pyspark.sql import SparkSession

def print_df():
    my_list = [1, 2, 3]
    # spark = SparkSession.builder.appName("my first spark app").getOrCreate()
    spark = (
        SparkSession
        .builder
        .master("spark://localhost:7077")
        .appName("my first spark app")
        .getOrCreate()
    )
    df = spark.createDataFrame(my_list, IntegerType())
    df.show()

if __name__ == "__main__":
    print_df()