# Data Entry API
## Podman
#### Build
* podman build -t data-entry-https .
* podman tag data-entry-https quay.io/rhn_consulting_kemori/data-entry-https
* podman push quay.io/rhn_consulting_kemori/data-entry-https
### Run
* podman run -d --pod report-pod  -e URL_PUSH_DATA="localhost:8089/api/test_result" --name data-entry-https data-entry-https
* option --volume /USER-PATH/data:/app/data
## OpenShift
* oc new-app quay.io/rhn_consulting_kemori/data-entry-https -e URL_PUSH_DATA="result-manager-demo-report.apps.rosa.rosa-6hxjb.nnh2.p3.openshiftapps.com/api/test_result" --name=data-entry-https
* oc get pods -l deployment=data-entry-https --field-selector status.phase=Running
* oc rsync ./data/input/ data-entry-https-989dbd77c-nf7qn:/app/data/input/ --no-perms
* oc rsync data-entry-https-989dbd77c-nf7qn:/app/data/output/ ./data/output
* oc delete deployment data-entry-https
* oc delete service data-entry-https