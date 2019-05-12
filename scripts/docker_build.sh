#!/usr/bin/env bash
set -e

echo "build image"

REPOSITORY=shekodn
IMAGE=trendlit
TAG=`make version`
HASH=`git log --format="%H" -n 1 | cut -c1-6`

# ARG ADMIN_PORT=some_default_value
# ENV ADMIN_PORT=${ADMIN_PORT}

ARG RELEASE=${TAG}

docker build --build-arg ${RELEASE} -t ${REPOSITORY}/${IMAGE}:${TAG} .
docker build --build-arg ${RELEASE} -t ${REPOSITORY}/${IMAGE}:${HASH} .
