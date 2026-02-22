pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                echo 'Cloning source code...'
                git branch: 'main', url: 'https://github.com/yash1015/flask-app-ecs.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                sh 'docker build -t flask-app:latest .'
            }
        }

        stage('Stop Old Container') {
            steps {
                echo 'Stopping old container if exists...'
                sh 'docker rm -f flask-container || true'
            }
        }

        stage('Run New Container') {
            steps {
                echo 'Running new container...'
                sh 'docker run -d -p 5000:5000 --name flask-container flask-app:latest'
            }
        }

    }
}
