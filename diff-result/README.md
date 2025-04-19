# diff-result
## podman run
* podman run -d  --volume /Users-Path:/app/data -e ACTUAL_DIR_PATH="/app/data/" -e EXPECTED_DIR_PATH="/app/data/" -e DIFF_DIR_PATH="/app/data/" -e ACTUAL_FILE_NAME="assert-actual-002-test_task_run.csv" -e EXPECTED_FILE_NAME="assert-expected-002-test_task_run.csv" -e DIFF_FILE_NAME="assert-diff-002-test_task_run.txt" --name diff-result diff-result
* 