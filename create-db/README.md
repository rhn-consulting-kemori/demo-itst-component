# Postgresql set up
## Podman
#### podman pod create --name report-pod -p 5432:5432,8088:8088,8089:8089
#### podman run --name postgres-srv --pod report-pod -e POSTGRES_PASSWORD=＠ -d postgres:16
#### podman exec -it postgres-srv bash
#### psql -U postgres
## OpenShift
### デプロイ
#### oc new-app postgresql -e POSTGRESQL_DATABASE=＠ -e POSTGRESQL_USER=＠ -e POSTGRESQL_PASSWORD=＠ --name=test-postgresql
#### postgresのユーザーはすでに作成されているので、指定するとエラーになる
### 外部公開
#### oc expose deployment test-postgresql --port=5432 --target-port=5432 --type=LoadBalancer --name outer-test-postgresql-svc