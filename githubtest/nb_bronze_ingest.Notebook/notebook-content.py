# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "1c4eb718-b388-4063-a10c-52b088e39e7d",
# META       "default_lakehouse_name": "lh_bronze_lakehouse",
# META       "default_lakehouse_workspace_id": "5d8d180a-48e5-49fd-8e71-1619c5582932",
# META       "known_lakehouses": [
# META         {
# META           "id": "1c4eb718-b388-4063-a10c-52b088e39e7d"
# META         }
# META       ]
# META     },
# META     "warehouse": {
# META       "default_warehouse": "9ec61abc-4414-4037-9709-2a37e0cb7623",
# META       "known_warehouses": [
# META         {
# META           "id": "9ec61abc-4414-4037-9709-2a37e0cb7623",
# META           "type": "Lakewarehouse"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

bronze = spark.read.format("delta").load("Tables/carrier_claims_raw")
bronze.show()


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Attach bronze and silver lakehouses in the notebook
bronze = spark.read.format("delta").load("Tables/carrier_claims_raw")


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
