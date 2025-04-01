# Report Viewer
## Build
#### podman build -t report-viewer .
## Run
#### podman run -d --pod report-pod --name report-viewer report-viewer
## VENV
#### source /Users/kemori/dev/python/py3-13-2/bin/activate
#### deactivate
## OpenShift
#### oc new-app https://github.com/rhn-consulting-kemori/demo-itst-pipeline.git --context-dir=/report-viewer -e DB_USER=test -e DB_PASS=test -e DB_PORT=5432 -e DB_NAME=test -e DB_HOST=test-postgresql.demo-report.svc.cluster.local --name=test-report-viewer
#### oc create route edge test-report-viewer --service=test-report-viewer --insecure-policy=Redirect