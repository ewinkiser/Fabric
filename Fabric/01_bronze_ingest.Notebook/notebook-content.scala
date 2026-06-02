// Fabric notebook source

// METADATA ********************

// META {
// META   "kernel_info": {
// META     "name": "synapse_pyspark"
// META   },
// META   "dependencies": {
// META     "lakehouse": {
// META       "default_lakehouse": "3c83ef5f-750c-451d-8451-863ab5d52e5a",
// META       "default_lakehouse_name": "benefits_lakehouse",
// META       "default_lakehouse_workspace_id": "5e57f493-2162-43a2-bdf8-35ff9072d4dc",
// META       "known_lakehouses": [
// META         {
// META           "id": "3c83ef5f-750c-451d-8451-863ab5d52e5a"
// META         }
// META       ]
// META     }
// META   }
// META }

// CELL ********************

from notebookutils import mssparkutils
display(mssparkutils.fs.ls("Files/raw/benefits"))




// METADATA ********************

// META {
// META   "language": "scala",
// META   "language_group": "synapse_pyspark"
// META }

// CELL ********************

display(dbutils.fs.ls("Files/raw"))


// METADATA ********************

// META {
// META   "language": "scala",
// META   "language_group": "synapse_pyspark"
// META }
