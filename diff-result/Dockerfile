FROM python:3.13.2

ARG project_dir=/app/

COPY . $project_dir

WORKDIR $project_dir

RUN pip install -r requirements.txt

# ENV Parameter
ENV ACTUAL_DIR_PATH=./
ENV EXPECTED_DIR_PATH=./
ENV DIFF_DIR_PATH=./
ENV ACTUAL_FILE_NAME=assert-actual-002-test_task_run.csv
ENV EXPECTED_FILE_NAME=assert-expected-002-test_task_run.csv
ENV DIFF_FILE_NAME=assert-diff-002-test_task_run.txt

# File Write Grant
USER root
RUN mkdir -p /mnt/data
RUN chgrp -R 0 /mnt/data && chmod -R g=u /mnt/data
USER 1001

CMD ["python", "app.py"]
