# spark or dask cluster
def create_cluster(cluster_type: str, worker_nodes: int):
    if cluster_type == "spark":
        print("need to work on spark")
    else:
        return _spawn_dask(worker_nodes)  # return client


def _spawn_dask(nodes: int, image: str = "ghcr.io/dask/dask"):
    from dask_kubernetes import KubeCluster, make_pod_spec

    pod_spec = make_pod_spec(image=image)
    cluster = KubeCluster(pod_spec)
    cluster.scale(nodes)
    from dask.distributed import Client

    client = Client(cluster)
    return client
