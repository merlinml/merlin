import os
import yaml
from kubernetes import client, config, utils


config.load_kube_config("path/to/kubeconfig_file")

with open(
    os.path.join(os.path.dirname(__file__), "k8s/spark-operator/pyspark-pi.yaml")
) as f:
    dep = yaml.safe_load(f)
    custom_object_api = client.CustomObjectsApi()
    # requires spark operator in cluster
    custom_object_api.create_namespaced_custom_object(
        group="sparkoperator.k8s.io",
        version="v1beta2",
        namespace="spark-jobs",
        plural="sparkapplications",
        body=dep,
    )
    print("SparkApplication created")
