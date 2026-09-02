# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "26030c8c-629f-4f44-9b6e-49a579494d69",
# META       "default_lakehouse_name": "lh_gold_lakehouse",
# META       "default_lakehouse_workspace_id": "e180442a-d3c7-4bef-a4b8-7db064480870",
# META       "known_lakehouses": [
# META         {
# META           "id": "26030c8c-629f-4f44-9b6e-49a579494d69"
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
