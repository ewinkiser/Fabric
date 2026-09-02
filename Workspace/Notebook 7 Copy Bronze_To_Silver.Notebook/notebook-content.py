# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "54b78f1e-b7de-4898-a439-0a339237b99a",
# META       "default_lakehouse_name": "lh_silver_lakehouse",
# META       "default_lakehouse_workspace_id": "e180442a-d3c7-4bef-a4b8-7db064480870",
# META       "known_lakehouses": [
# META         {
# META           "id": "54b78f1e-b7de-4898-a439-0a339237b99a"
# META         },
# META         {
# META           "id": "728fa79c-bab2-437b-a63d-08af871316d6"
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



# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
