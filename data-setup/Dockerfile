FROM python:3.13.2

ARG project_dir=/app/

COPY . $project_dir

WORKDIR $project_dir

RUN pip install -r requirements.txt

CMD ["python", "app.py"]

EXPOSE 8090
