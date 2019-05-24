#!/usr/bin/env bash
set -e

echo "build image"

REPOSITORY=shekodn
IMAGE=trendlit
TAG=`make version`
HASH=`git log --format="%H" -n 1 | cut -c1-6`

docker build --build-arg RELEASE=${TAG} -t ${REPOSITORY}/${IMAGE}:${TAG} .
docker build --build-arg RELEASE=${TAG} -t ${REPOSITORY}/${IMAGE}:${HASH} .
docker tag ${REPOSITORY}/${IMAGE}:${HASH} ${REPOSITORY}/${IMAGE}:latest
