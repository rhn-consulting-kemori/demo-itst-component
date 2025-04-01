# CREATE quay.io image-pull secret
## OpenShift Command
* oc create secret generic quayio --from-file .dockerconfigjson=~/.docker/config.json --type kubernetes.io/dockerconfigjson
* oc secrets link default quayio --for pull
## image stream
* oc import-image create-table --confirm --insecure --from quay.io/rhn_consulting_kemori/create_table