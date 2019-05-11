pipeline {
    agent none
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'python:3.7-alpine'
                }
            }
            steps {
                sh echo 'python3 -m py_compile sources/add2vals.py sources/calc.py'
            }
        }
    }
}
