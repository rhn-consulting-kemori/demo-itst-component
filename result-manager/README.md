# Report Manager
## Build
#### podman build -t result-manager .
## Run
#### podman run -d --pod report-pod --name result-manager result-manager
## VENV
#### source /Users/kemori/dev/python/py3-13-2/bin/activate
#### deactivate
## Data
* curl -X POST -H "Content-Type: application/json" -d '{"test_id": "ST-E001-00000001", "test_name": "sample_test", "test_description": "sample"}' http://127.0.0.1:8089/api/test_result
* curl -X POST -H "Content-Type: application/json" -d '{"test_result_seq":@, "test_id": "@", "test_group": "@", "test_pipeline": "@", "test_task": "@","simulation_date": "@", "start_time": "@", "end_time": "@", "test_result": "@", "evidence_link": "@", "sw_category": "@", "sw_id": "@", "sw_name": "@", "sw_version": "@"}' http://127.0.0.1:8089/api/test_task
* curl -X POST -H "Content-Type: application/json" -d '{"test_result_seq": @, "test_id": "@", "test_group": "@", "test_pipeline": "@", "simulation_date": "@"}' http://127.0.0.1:8089/api/pipeline_summary
* curl -X POST -H "Content-Type: application/json" -d '{"test_result_seq": 2}' http://127.0.0.1:8089/api/test_result_summary
## OpenShift
#### oc new-app https://github.com/rhn-consulting-kemori/demo-itst-pipeline.git --context-dir=/result-manager -e DB_USER=@ -e DB_PASS=@ -e DB_PORT=@ -e DB_NAME=@ -e DB_HOST=test-postgresql.demo-report.svc.cluster.local --name=result-manager
#### oc create route edge result-manager --service=result-manager --insecure-policy=Redirect