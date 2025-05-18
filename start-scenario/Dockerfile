FROM python:3.13.2

ARG project_dir=/app/

COPY . $project_dir

WORKDIR $project_dir

RUN pip install -r requirements.txt

# ENV Parameter
ENV REPORT_VIEWER_URL=https://report-viewer-demo-report.apps.rosa.openshiftapps.com/
ENV AAP_URL=https://controller.com/
ENV OPENSHIFT_URL=https://console-openshift-console.apps.rosa.openshiftapps.com/
ENV AAP_API_URL=https://controller.com/api/controller/v2/workflow_job_templates/39/launch/
ENV AAP_TOKEN=abc

CMD ["python", "app.py"]

EXPOSE 8090
