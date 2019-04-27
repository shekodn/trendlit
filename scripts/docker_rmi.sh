#!/usr/bin/env bash
set -e

echo "remove image"

REPOSITORY=shekodn
IMAGE=trendlit
TAG=`make version`
HASH=`git log --format="%H" -n 1 | cut -c1-6`

docker rmi ${REPOSITORY}/${IMAGE}:${TAG}
docker rmi ${REPOSITORY}/${IMAGE}:${HASH}
