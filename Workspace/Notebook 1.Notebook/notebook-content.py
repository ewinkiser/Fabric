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
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

# Welcome to your new notebook
# Attach bronze and silver lakehouses in the notebook
bronze = spark.read.format("delta").load("Tables/carrier_claims_raw")
bronze.show()



# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
