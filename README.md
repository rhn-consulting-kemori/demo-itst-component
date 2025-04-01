# demo-itst-pipeline
## Create NameSpace

## Create Secret

## Create Database
* oc new-app postgresql -e POSTGRESQL_DATABASE=test -e POSTGRESQL_USER=test -e POSTGRESQL_PASSWORD=test --name=postgresql
## Create Table
* oc create -f create-table-job.yaml
* oc delete job create-table-job
## Insert Table
* oc create -f insert-table-job.yaml
* oc delete job insert-table-job
## Deploy App
### report-viewer
* oc new-app quay.io/rhn_consulting_kemori/report-viewer -e DB_USER=test -e DB_PASS=test -e DB_PORT=5432 -e DB_NAME=test -e DB_HOST=postgresql.demo-report.svc.cluster.local --name=report-viewer
* oc create route edge report-viewer --service=report-viewer --insecure-policy=Redirect
### report-viewer
* oc new-app quay.io/rhn_consulting_kemori/result-manager -e DB_USER=test -e DB_PASS=test -e DB_PORT=5432 -e DB_NAME=test -e DB_HOST=postgresql.demo-report.svc.cluster.local --name=result-manager
* oc create route edge result-manager --service=result-manager --insecure-policy=Redirect
### data-entry-https
* oc new-app quay.io/rhn_consulting_kemori/data-entry-https -e URL_PUSH_DATA="result-manager-demo-report.apps.rosa.rosa-6hxjb.nnh2.p3.openshiftapps.com/api/test_result" --name=data-entry-https
* oc get pods -l deployment=data-entry-https --field-selector status.phase=Running
* oc rsync ./data/input/ data-entry-https-989dbd77c-nf7qn:/app/data/input/ --no-perms
* oc rsync data-entry-https-989dbd77c-nf7qn:/app/data/output/ ./data/output
* oc delete deployment data-entry-https
* oc delete service data-entry-https