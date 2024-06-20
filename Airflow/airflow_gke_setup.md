Set GKE
```bash
gcloud container clusters create gke-airflow \
--machine-type e2-medium \
--num-nodes 1 \
--region "asia-northeast3" \
--enable-autoscaling \
--min-nodes 1 \
--max-nodes 3
```

```bash
gcloud container clusters get-credentials gke-airflow --region "asia-northeast3"
```

```bash
curl https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3 | bash
```

```bash
helm repo add apache-airflow https://airflow.apache.org
helm repo update
```

```bash
kubectl create namespace airflow
```

```bash
helm install airflow apache-airflow/airflow --namespace airflow
```

```bash
kubectl port-forward svc/airflow-webserver 8080:8080 -n airflow
```

