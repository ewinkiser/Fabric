# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "a4f9c7c2-2ec6-483f-97ac-c1c3d8763be4",
# META       "default_lakehouse_name": "lh_silver_lakehouse",
# META       "default_lakehouse_workspace_id": "5d8d180a-48e5-49fd-8e71-1619c5582932",
# META       "known_lakehouses": [
# META         {
# META           "id": "1c4eb718-b388-4063-a10c-52b088e39e7d"
# META         },
# META         {
# META           "id": "a4f9c7c2-2ec6-483f-97ac-c1c3d8763be4"
# META         }
# META       ]
# META     },
# META     "warehouse": {
# META       "known_warehouses": []
# META     }
# META   }
# META }

# CELL ********************

bronze = spark.read.format("delta").load("Tables/dbo/carrier_claims_raw")
bronze.show()



from pyspark.sql import functions as F

silver = (
    bronze
    .withColumn("Provider", F.initcap(F.col("Provider")))
    .withColumn("Notes", F.trim(F.col("Notes")))
    .withColumn("EndDate",
                F.when(F.col("EndDate").isNull(), F.lit("2099-12-31"))
                 .otherwise(F.col("EndDate")))
    .withColumn("CoverageTier",
                F.when(F.col("CoverageAmount") >= 4000, "Premium")
                 .when(F.col("CoverageAmount") >= 2000, "Standard")
                 .otherwise("Basic"))
    .withColumnRenamed("EmployeeID", "employee_id")
    .withColumnRenamed("BenefitType", "benefit_type")
    .withColumnRenamed("CoverageAmount", "coverage_amount")
    .withColumnRenamed("StartDate", "start_date")
    .withColumnRenamed("EndDate", "end_date")
)


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
