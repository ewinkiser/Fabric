# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "23fe434f-f98b-43b9-a905-5a948c676fd8",
# META       "default_lakehouse_name": "lh_gold_lakehouse",
# META       "default_lakehouse_workspace_id": "5d8d180a-48e5-49fd-8e71-1619c5582932",
# META       "known_lakehouses": [
# META         {
# META           "id": "a4f9c7c2-2ec6-483f-97ac-c1c3d8763be4"
# META         },
# META         {
# META           "id": "1c4eb718-b388-4063-a10c-52b088e39e7d"
# META         },
# META         {
# META           "id": "23fe434f-f98b-43b9-a905-5a948c676fd8"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

# Welcome to your new notebook
# Type here in the cell editor to add code!

silver.write.format("delta").mode("overwrite").saveAsTable("lh_silver_lakehouse.dbo.claims_silver")


from pyspark.sql import functions as F

silver = (
    bronze
    .withColumn("Provider", F.initcap(F.col("Provider")))
    .withColumn("Notes", F.trim(F.col("Notes")))
    .withColumn(
        "EndDate",
        F.when(F.col("EndDate").isNull(), F.lit("2099-12-31"))
         .otherwise(F.col("EndDate"))
    )
    .withColumn(
        "CoverageTier",
        F.when(F.col("CoverageAmount") >= 4000, "Premium")
         .when(F.col("CoverageAmount") >= 2000, "Standard")
         .otherwise("Basic")
    )
)

spark.read.table("lh_silver_lakehouse.dbo.claims_silver").show()
silver.show()

df_silver = spark.read.table("silver_lakehouse.claims_silver")
df_silver = spark.read.table("lh_silver_lakehouse.claims_silver")

df_silver = spark.read.table("lh_silver_lakehouse.claims_silver")

df_silver = spark.read.table("lh_silver_lakehouse.dbo.claims_silver")
df_silver.show()

from pyspark.sql import functions as F

df_gold_summary = (
    df_silver
    .groupBy("EmployeeID", "BenefitType", "CoverageTier", "Provider")
    .agg(
        F.count("*").alias("record_count"),
        F.sum("CoverageAmount").alias("total_coverage_amount"),
        F.avg("CoverageAmount").alias("avg_coverage_amount")
    )
)

df_gold_summary.write.mode("overwrite").format("delta").saveAsTable("lh_gold_lakehouse.dbo.claims_gold_summary")

display(spark.read.table("lh_gold_lakehouse.dbo.claims_gold_summary"))


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
