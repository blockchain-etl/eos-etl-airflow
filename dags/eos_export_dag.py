from __future__ import print_function

from eosetl_airflow.build_export_dag import build_export_dag
from eosetl_airflow.variables import read_export_dag_vars

# airflow DAG
DAG = build_export_dag(
    dag_id='eos_export_dag',
    **read_export_dag_vars(
        var_prefix='eos_',
        export_schedule_interval='0 12 * * *',
        export_start_date='2018-06-08',
        export_max_workers=30,
        export_batch_size=1,
    )
)
