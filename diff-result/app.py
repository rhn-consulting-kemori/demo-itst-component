# -*- coding: utf-8 -*-
import os
import difflib

# Environment Parameter
actual_dir_path = os.getenv('ACTUAL_DIR_PATH', './')
expected_dir_path = os.getenv('EXPECTED_DIR_PATH', './')
diff_dir_path = os.getenv('DIFF_DIR_PATH', './')
# ---
actual_file_name = os.getenv('ACTUAL_FILE_NAME', 'assert-actual-002-test_task_run.csv')
expected_file_name = os.getenv('EXPECTED_FILE_NAME', 'assert-expected-002-test_task_run.csv')
diff_file_name = os.getenv('DIFF_FILE_NAME', 'assert-diff-002-test_task_run.txt')

# Path
actual_path = os.path.join(actual_dir_path, actual_file_name)
expected_path = os.path.join(expected_dir_path, expected_file_name)
diff_path = os.path.join(diff_dir_path, diff_file_name)

# File Open
actual_file = open(actual_path)
expected_file = open(expected_path)

# Diff
diff = difflib.Differ()
output_diff = diff.compare(actual_file.readlines(), expected_file.readlines())

# Write result
with open(diff_path, "w") as output_f:
    for data in output_diff :
        if data[0:1] in ['+', '-'] :
            output_f.write(data + '\n')

# File Close
actual_file.close()
expected_file.close()
