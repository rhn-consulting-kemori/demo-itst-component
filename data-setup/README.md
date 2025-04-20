# data-setup
## Build
#### podman build -t data-setup .
## Run
#### podman run -d --volume /Users-Path:/app/data --name data-setup data-setup
## VENV
#### source /Users/kemori/dev/python/py3-13-2/bin/activate
#### deactivate
## OpenShift
#### oc new-app https://github.com/rhn-consulting-kemori/demo-itst-component.git --context-dir=/data-setup  --name=data-setup
