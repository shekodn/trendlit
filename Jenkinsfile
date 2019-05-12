pipeline {
  agent none
  environment {
    registry = "shekodn/trendlit"
    registryCredential = 'shekodn'

  }
  stages {
    // stage('Test') {
    //   agent {
    //     docker {
    //       image 'python:3.7-alpine'
    //     }
    //   }
    //   steps {
    //     sh 'python3 -m unittest tests/test_compiled_code.py'
    //   }
    // }
    stage('Deliver') {
      agent {
        docker {
          image 'shekodn/alpine-essential:0.0.1'
        }
      }

        steps {
          script {
          docker.withRegistry('', 'docker_hub') {

            sh 'scripts/docker_check.sh'
            sh 'scripts/docker_build.sh'
            sh 'scripts/docker_push.sh'
          }
        }
      }
    }
  }
}
