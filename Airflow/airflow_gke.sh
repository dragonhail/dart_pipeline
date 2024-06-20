
helm repo add apache-airflow https://airflow.apache.org
helm repo list
kubectl create namespace airflow
helm upgrade --install airflow apache-airflow/airflow -n airflow --debug
ssh-keygen -t rsa -b 4096
kubectl create secret generic airflow-gke-git-secret --from-file=gitSshKey=/home/mun_js/.ssh/id_rsa -n airflow
kubectl get secret -n airflow
helm show values apache-airflow/airflow > values.yaml
vi values.yaml

#copy codes below to values.yaml
gitSync:
  enabled: True
  repo: git@github.com:mjs1995/gcp-de-pipeline.git
  branch: main
  rev: HEAD
  subPath: "terraform-airflow-gke/airflow"
  sshKeySecret: airflow-gke-git-secret

helm upgrade airflow apache-airflow/airflow -f values.yaml -n airflow --debug

# Create secret static web server key
kubectl create secret generic my-webserver-secret --from-literal="webserver-secret-key=$(python3 -c 'import secrets; print(secrets.token_hex(16))')"
kubectl get secret my-webserver-secret --namespace=default -o yaml > my-webserver-secret.yaml
sed -i 's/namespace: default/namespace: airflow/' my-webserver-secret.yaml
kubectl apply -f my-webserver-secret.yaml
helm upgrade airflow apache-airflow/airflow -n airflow --set webserverSecretKeySecretName=my-webserver-secret --debug

# Connect to Airflow UI
kubectl port-forward svc/airflow-webserver 8080:8080 --namespace airflow
