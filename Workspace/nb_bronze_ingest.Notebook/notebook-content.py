# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "728fa79c-bab2-437b-a63d-08af871316d6",
# META       "default_lakehouse_name": "lh_bronze_lakehouse",
# META       "default_lakehouse_workspace_id": "e180442a-d3c7-4bef-a4b8-7db064480870",
# META       "known_lakehouses": [
# META         {
# META           "id": "728fa79c-bab2-437b-a63d-08af871316d6"
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
