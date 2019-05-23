#!/usr/bin/env bash
set -e

echo "run container"

REPOSITORY=shekodn
IMAGE=trendlit
TAG=`make version`

PORT=80

docker run -p ${PORT}:${PORT} -e "PORT=${PORT}" \
	${REPOSITORY}/${IMAGE}:${TAG}
