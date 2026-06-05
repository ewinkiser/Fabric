# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "3c83ef5f-750c-451d-8451-863ab5d52e5a",
# META       "default_lakehouse_name": "benefits_lakehouse",
# META       "default_lakehouse_workspace_id": "5e57f493-2162-43a2-bdf8-35ff9072d4dc",
# META       "known_lakehouses": [
# META         {
# META           "id": "3c83ef5f-750c-451d-8451-863ab5d52e5a"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

from pyspark.sql.types import *

schema = StructType([
    StructField("claim_id", StringType()),
    StructField("carrier_id", StringType()),
    StructField("claim_date", StringType()),
    StructField("amount", DoubleType()),
    StructField("status", StringType()),
    StructField("adjuster_id", StringType())
])

data = [
    ("CLM001","CARRIER_A","2026-01-15",15000.00,"Open","ADJ101"),
    ("CLM002","CARRIER_B","2026-01-16",8500.00,"Closed","ADJ102"),
    ("CLM003","CARRIER_A","2026-01-17",22000.00,"Disputed","ADJ103"),
    ("CLM004","CARRIER_C","2026-01-18",4200.00,"Open","ADJ101"),
    ("CLM005","CARRIER_B","2026-01-19",31000.00,"Closed","ADJ104"),
    ("CLM006","CARRIER_A","2026-01-20",9800.00,"Disputed","ADJ102"),
    ("CLM007","CARRIER_C","2026-01-21",6500.00,"Open","ADJ103"),
    ("CLM008","CARRIER_B","2026-01-22",18700.00,"Closed","ADJ101")
]

df = spark.createDataFrame(data, schema)
df.write.format("delta").mode("overwrite").saveAsTable("carrier_claims_raw")
print(f"✅ Done — {df.count()} rows written to bronze_lakehouse")
df.show()




# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************




# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
