# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "228aba6b-7bb4-4d3a-98e3-a5400824f550",
# META       "default_lakehouse_name": "silver_lakehouse",
# META       "default_lakehouse_workspace_id": "5e57f493-2162-43a2-bdf8-35ff9072d4dc",
# META       "known_lakehouses": [
# META         {
# META           "id": "228aba6b-7bb4-4d3a-98e3-a5400824f550"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

from pyspark.sql.types import *
from pyspark.sql.functions import col, when, trim, to_date, upper

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

df_raw = spark.createDataFrame(data, schema)

df_silver = (df_raw
    # ── Cleanse ──────────────────────────────────────────
    .dropDuplicates(["claim_id"])                          # remove dupes
    .dropna(subset=["claim_id","amount","status"])         # drop nulls on key fields
    .withColumn("carrier_id", trim(upper(col("carrier_id"))))   # standardize strings
    .withColumn("status",     trim(upper(col("status"))))
    .withColumn("claim_date", to_date(col("claim_date"), "yyyy-MM-dd"))  # cast date

    # ── Filter ───────────────────────────────────────────
    .filter(col("status") != "DISPUTED")                  # business rule

    # ── Transform ────────────────────────────────────────
    .withColumnRenamed("claim_id", "claim_key")
    .withColumn("claim_category",
        when(col("amount") >= 15000, "High Value")
        .otherwise("Standard"))
)

df_silver.write \
    .format("delta") \
    .mode("overwrite") \
    .option("overwriteSchema", "true") \
    .saveAsTable("claims_silver")

print(f"Done! {df_silver.count()} rows written to claims_silver ✅")
df_silver.printSchema()





# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
