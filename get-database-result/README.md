# get-database-result
## podman run
* podman run -d --pod report-pod --volume /User-Path:/app/data -e INPUT_FILE_PATH="/app/data/" -e INPUT_FILE_NAME="assert-actual-002-test_task_run.sql" -e OUTPUT_FILE_PATH="/app/data/" -e OUTPUT_FILE_NAME="assert-actual-002-test_task_run.csv"  --name get-database-result get-database-result