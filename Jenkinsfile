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

       
        stage('Test (Unit tests in Docker)') {
            agent any 
            steps {
                script {
                   
                    bat 'docker build -t test-image .' 
                    
                    
                    bat 'docker run --rm test-image pytest'
                }
            }
        }

    
        stage('Build & Push Docker Image') {
            agent any
            steps {
                script {
                    def dockerHubUser = 'volodimirbabak'
                    def repoName = 'exam-lab' 

                    docker.withRegistry('', 'dockerhub-creds') {
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
        always {
            
             script { try { bat 'docker rmi test-image' } catch(e) {} }
        }
    }
}