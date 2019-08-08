from __future__ import print_function

import logging

from eosetl_airflow.build_load_dag import build_load_dag
from eosetl_airflow.variables import read_load_dag_vars

logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)

# airflow DAG
DAG = build_load_dag(
    dag_id='eos_load_dag',
    chain='eos',
    **read_load_dag_vars(
        var_prefix='eos_',
        schedule_interval='30 13 * * *'
    )
)
