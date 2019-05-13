pipeline {
  agent none
  stages {
    stage('Test') {
      agent {
        docker {
          image 'python:3.7-alpine'
        }
      }
      steps {
        sh 'python3 -m unittest tests/test_compiled_code.py'
      }
    }

    stage('Build') {
      steps {
        sh 'scripts/docker_build.sh'
      }
    }

    stage('Push') {
      steps {
        script {
          docker.withRegistry('', 'docker_hub') {
            try {
              sh 'scripts/docker_check.sh'
              sh 'scripts/docker_push.sh'
            } catch (Exception e) {
              sh 'echo check that the intended version is already bumped'
            }
          }
        }
      }
    }

    stage('Remove') {
      steps {
        sh 'scripts/docker_rmi.sh'
      }
    }
  }
}
