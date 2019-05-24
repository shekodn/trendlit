#!/usr/bin/env bash
set -e

echo "push image"

REPOSITORY=shekodn
IMAGE=trendlit
TAG=`make version`
HASH=`git log --format="%H" -n 1 | cut -c1-6`

docker push ${REPOSITORY}/${IMAGE}:${TAG}
docker push ${REPOSITORY}/${IMAGE}:${HASH}
docker push ${REPOSITORY}/${IMAGE}:latest
