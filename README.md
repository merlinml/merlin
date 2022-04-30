## Interactive python spark session on microk8s

This uses bdrecipes/spark-on-docker:latest

https://datarecipes.hashnode.dev/23-apache-spark-on-kubernetes


`microk8s kubectl create serviceaccount bigdata-sa`
`microk8s kubectl create rolebinding bigdata-rb --clusterrole=edit --serviceaccount=default:bigdata-sa`
`K8_API_URL=$(microk8s kubectl config view --minify -o jsonpath="{.clusters[0].cluster.server}")`

Create the spark image (in future state this image will include vscode etc):

`microk8s kubectl apply -f https://raw.githubusercontent.com/g1thubhub/bdrecipes/KubernetesImage/scripts/interactive_pod.yaml`

Expose the pod so we can interact with spark (need this to be done programmatically, of course):

`microk8s kubectl expose pod interactive-pod --type=ClusterIP --cluster-ip=None`

/opt/spark/bin/spark-submit \
    --master k8s://https://kubernetes.default:443 \
    --deploy-mode client \
    --conf spark.kubernetes.authenticate.submission.caCertFile=$CACERT \
    --conf spark.kubernetes.authenticate.submission.oauthTokenFile=$TOKEN \
    --conf spark.kubernetes.container.image=bdrecipes/spark-on-docker:latest \
    --conf spark.executor.instances=2 \
    --conf spark.kubernetes.authenticate.driver.serviceAccountName=bigdata-sa \
    local:///opt/spark/work-dir/tutorials/module1/python/query_plans_docker.py \
    /opt/spark/work-dir/resources/warc.sample