# INSERT TABLE for PostgreSQL
## podman
* podman build -t insert_table .
* podman run --rm --name insert_table_app --pod report-pod -e DB_USER=postgres -e DB_PASSWORD=postgres -e DB_SERVERNAME=localhost -e DB_PORTNUMBER=5432 insert_table
## OpenShift
* oc create -f insert-table-job.yaml
* oc delete job insert-table-job