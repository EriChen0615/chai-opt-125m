#!/bin/bash
# DEP_NAME=eric-opt-deployment-30b

kubectl delete deployment $DEP_NAME
kubectl apply -f deployment.yaml
kubectl get pods | grep ^$DEP_NAME