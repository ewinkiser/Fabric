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
# META           "id": "23fe434f-f98b-43b9-a905-5a948c676fd8"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

# Welcome to your new notebook
# Type here in the cell editor to add code!
from pyspark.sql.types import *

schema = StructType([
    StructField("policy_id", StringType(), True),
    StructField("policy_name", StringType(), True),
    StructField("policy_type", StringType(), True),   # DQ, Security, Naming, Pipeline
    StructField("applies_to", StringType(), True),    # Bronze, Silver, Gold, All
    StructField("rule_expression", StringType(), True),
    StructField("severity", StringType(), True),      # Error, Warning
    StructField("enabled", BooleanType(), True)
])

empty_df = spark.createDataFrame([], schema)

empty_df.write.format("delta").mode("overwrite").saveAsTable("guardrail_policies")

spark.sql("SHOW TABLES").show()

display(spark.table("guardrail_policies"))

spark.sql("""
INSERT INTO guardrail_policies VALUES
('P001', 'CoverageAmount must be > 0', 'DQ', 'Silver', 'CoverageAmount > 0', 'Error', true)
""")

spark.sql("SHOW TABLES").show()


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
