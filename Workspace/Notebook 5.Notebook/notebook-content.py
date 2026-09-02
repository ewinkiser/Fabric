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


bronze = spark.sql("SELECT * FROM lh_bronze_lakehouse.dbo.carrier_claims_raw")
bronze.show()




df = spark.read.format("delta").load("lh_bronze_lakehouse.dbo.carrier_claims_raw")

df_silver = (
    df.filter(df.disputed == "No")
      .withColumnRenamed("claim_id", "claim_key")
      .withColumn("claim_category",
                  F.when(df.claim_amount > 5000, "HighValue")
                   .otherwise("Standard"))
      .withColumn("claim_amount", F.coalesce(df.claim_amount, F.lit(0)))
      .withColumn("state", F.upper(F.trim(df.state)))
      .withColumn("customer_name", F.initcap(F.trim(df.customer_name)))
)

df_silver.write.format("delta").mode("overwrite").save("Tables/claims_silver")






# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df = spark.read.format("csv").option("header","true").load("Files/benefits_20240109.csv")

df.write.format("delta").mode("overwrite").save("Tables/dbo/carrier_claims_raw")





# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
