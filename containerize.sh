#!/bin/bash

CONTAINER_NAME="opt-125m-x86-v1"
DOCKER_HUB="erichen0615"
PLATFORM_ARG="linux/amd64"

sudo docker build --platform $PLATFORM_ARG -t $CONTAINER_NAME .

echo $CONTAINER_NAME "Built image " $CONTAINER_NAME " for platform " $PLATFORM_ARG

function getImageId() 
{
    docker images --format="{{.Repository}} {{.ID}}" |
    grep $CONTAINER_NAME |
    cut -d' ' -f2
}
IMG_ID=$(getImageId)
echo image tag = $IMG_ID

HUB_IMG_NAME=$DOCKER_HUB/$CONTAINER_NAME 
sudo docker tag $IMG_ID $HUB_IMG_NAME
sudo docker push $HUB_IMG_NAME 

echo "Image pushed to docker hub, name = " $HUB_IMG_NAME 


