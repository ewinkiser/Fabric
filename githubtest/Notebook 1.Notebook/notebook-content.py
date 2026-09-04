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
# META           "id": "a4f9c7c2-2ec6-483f-97ac-c1c3d8763be4"
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
