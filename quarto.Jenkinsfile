pipeline {
    agent any
    stages {
        stage('step1') {
            steps {
                echo 'step 1'
                sh 'sleep 5'
            }            
        }
        stage('STEP 2 - Paralelo') {
            parallel {
                stage('step2 A') {
                    steps {
                        echo 'step 2 A'
                        sh 'sleep 15'
                    }            
                }
                stage('step2 B') {
                    steps {
                        echo 'step 2 B'
                        sh 'sleep 10'
                    }            
                }
            }
        }
        stage('step3') {
            steps {
                echo 'step 3'
                sh 'sleep 5'
            }            
        }        
    }
}