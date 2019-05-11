pipeline {
  agent any
  stages {
    stage('error') {
      steps {
        sh '''#!/usr/bin/env bash
set -e

# The goal of this script is to check if the tag that is going to be pushed is unique.
# In other words, if RELEASE variable was updated in the Makefile.
echo "check if the tag wasn\'t pushed before"

REPOSITORY=shekodn
IMAGE=trendlit
TAG=0.0.8

! docker pull ${REPOSITORY}/${IMAGE}:${TAG}
'''
      }
    }
  }
}