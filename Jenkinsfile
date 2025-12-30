pipeline {
    agent none
    options { timestamps() }

    stages {

        stage('Checkout SCM') {
            agent any
            steps {
                checkout scm
            }
        }

        // ЕТАП 1: Тестування (змінено під pytest та Alpine)
        stage('Test (Unit tests in Docker)') {
            agent {
                docker {
                    // Вимога білета: використовувати Alpine
                    image 'python:3.9-alpine' 
                    // Запуск від root потрібен, щоб встановити pip пакети всередині контейнера
                    args '-u root' 
                }
            }
            steps {
                // Спочатку встановлюємо pytest зі списку вимог
                sh 'pip install --no-cache-dir -r requirements.txt'
                // Запускаємо тести
                sh 'pytest'
            }
        }

        // ЕТАП 2: Збірка та Публікація (змінено назву репо)
        stage('Build & Push Docker Image') {
            agent any
            steps {
                script {
                    def dockerHubUser = 'volodimirbabak'
                    // Нова назва для іспиту
                    def repoName = 'exam-progression-app' 

                    // Використовуємо твій збережений ID 'dockerhub-creds'
                    docker.withRegistry('', 'dockerhub-creds') {
                        // Ця команда шукає Dockerfile у папці проєкту
                        def image = docker.build("${dockerHubUser}/${repoName}:${env.BUILD_NUMBER}")
                        image.push()
                        image.push('latest')
                    }
                }
            }
        }
    }

    post {
        success { echo "Pipeline completed successfully!" }
        failure { echo "Pipeline failed!" }
    }
}