FROM python:3.13.2

ARG project_dir=/app/

COPY . $project_dir

WORKDIR $project_dir

RUN pip install -r requirements.txt

# ENV Parameter
ENV DB_USER=postgres
ENV DB_PASS=postgres
ENV DB_HOST=127.0.0.1
ENV DB_PORT=5432
ENV DB_NAME=postgres
ENV INPUT_FILE_PATH=./
ENV INPUT_FILE_NAME=assert-actual-002-test_task_run.sql
ENV OUTPUT_FILE_PATH=./
ENV OUTPUT_FILE_NAME=assert-actual-002-test_task_run.csv

# File Write Grant
USER root
RUN chgrp -R 0 /mnt/data && chmod -R g=u /mnt/data
USER 1001

CMD ["python", "app.py"]
