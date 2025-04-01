# CREATE TABLE for PostgreSQL
## podman
* podman build -t create_table .
* podman run --rm --name create_table_app --pod report-pod -e DB_USER=postgres -e DB_PASSWORD=postgres -e DB_SERVERNAME=localhost -e DB_PORTNUMBER=5432 create_table
## OpenShift
* oc create -f create-table-job.yaml
* oc delete job create-table-job