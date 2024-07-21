properties([githubProjectProperty(displayName: '', projectUrlStr: 'https://github.com/dorsh97/World-of-Games.git/')])

pipeline {
    agent any
    
    environment {
        DOCKER_HUB_CREDENTIALS = credentials('dockerhub-credentials-id')
        // Parameters for testing and pushing:
        DOCKER_HUB_REPO = 'dorsh97/wog'
        DOCKER_IMAGE_TAG = 'latest'
        TESTING_CONTAINER_NAME = 'wog-container'
        TESTING_PORT = '8777'
        TESTING_SCORE_VALUE = '100'
    }
    
    stages {
        stage('Checkout') {
            steps {
                git branch: 'master', url: 'https://github.com/dorsh97/World-of-Games.git'
            }
        }
        
        stage('Build') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'echo ${TESTING_SCORE_VALUE} > Scores.txt'
                        sh 'docker build -t ${DOCKER_HUB_REPO}:latest .'
                    } else {
                        bat 'echo %TESTING_SCORE_VALUE% > Scores.txt'
                        bat 'docker build -t %DOCKER_HUB_REPO%:latest .'
                    }
                }
            }
        }
        
        stage('Run') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'docker run --name ${TESTING_CONTAINER_NAME} -d -p ${TESTING_PORT}:5000 -v $(pwd)/Scores.txt:/app/Scores.txt ${DOCKER_HUB_REPO}:latest'
                    } else {
                        bat 'echo DEBUG: DOCKER_HUB_REPO=%DOCKER_HUB_REPO%'
                        bat 'echo DEBUG: DOCKER_IMAGE_TAG=%DOCKER_IMAGE_TAG%'
                        bat 'docker run --name %TESTING_CONTAINER_NAME% -d -p %TESTING_PORT%:5000 -v "%cd%\\Scores.txt:/app/Scores.txt" %DOCKER_HUB_REPO%:latest'
                    }
                }
            }
        }
        
        stage('Test') {
            steps {
                script {
                    writeFile file: 'e2e_test.py', text: """
import sys
from Utilities.e2e import main_function

def e2e_test():
    port = sys.argv[1]
    url = f"http://localhost:{port}"
    sys.exit(main_function(url))

e2e_test()
"""
                    
                    if (isUnix()) {
                        sh 'pip install -r requirements.txt'
                        try {
                            sh 'python e2e_test.py ${TESTING_PORT}'
                            echo "Testing Successful"
                        } catch (Exception e) {
                            error "Testing Failed"
                        }
                    } else {
                        bat 'pip install -r requirements.txt'
                        try {
                            bat 'python e2e_test.py %TESTING_PORT%'
                            echo "Testing Successful"
                        } catch (Exception e) {
                            error "Testing Failed"
                        }
                    }
                }
            }
        }
        
        stage('Finalize') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'echo "" > Scores.txt'
                        sh 'docker login -u ${DOCKER_HUB_CREDENTIALS_USR} -p ${DOCKER_HUB_CREDENTIALS_PSW}'
                        sh 'docker push ${DOCKER_HUB_REPO}:${DOCKER_IMAGE_TAG}'
                        sh 'docker rm -vf ${TESTING_CONTAINER_NAME}'
                        sh 'docker rmi ${DOCKER_HUB_REPO}:${DOCKER_IMAGE_TAG}'
                    } else {
                        bat 'echo "" > Scores.txt'
                        bat 'docker login -u %DOCKER_HUB_CREDENTIALS_USR% -p %DOCKER_HUB_CREDENTIALS_PSW%'
                        bat 'docker push %DOCKER_HUB_REPO%:%DOCKER_IMAGE_TAG%'
                        bat 'docker rm -vf %TESTING_CONTAINER_NAME%'
                        bat 'docker rmi %DOCKER_HUB_REPO%:%DOCKER_IMAGE_TAG%'
                    }
                }
            }
        }
    }
    
    post {
        always {
            script {
                try {
                    if (isUnix()) {
                        sh 'docker rm -vf ${TESTING_CONTAINER_NAME}'
                    } else {
                        bat 'docker rm -vf %TESTING_CONTAINER_NAME%'
                    }
                } catch (Exception e) {
                    echo "Container has already been removed or does not exist."
                }

                try {
                    if (isUnix()) {
                        sh 'docker rmi ${DOCKER_HUB_REPO}:latest'
                    } else {
                        bat 'docker rmi %DOCKER_HUB_REPO%:latest'
                    }
                } catch (Exception e) {
                    echo "Image has already been removed or does not exist."
                }
                
                cleanWs()
            }
        }
    }
}
