
Remember to put your repo to public

podman build . -t quay.io/tanirvan/hello-python:v1.0
podman push quay.io/tanirvan/hello-python:v1.0

oc new-app --name hello-python quay.io/tanirvan/hello-python:v1.0
oc create route hello-world --service hello-world
curl -kv https://hello-world.apps.example.com
