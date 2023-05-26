pipeline {
    agent any
    stages {
        stage('step1') {
            steps {
                echo 'step 1'
            }            
        }
        stage('STEP 2 - Paralelo') {
            parallel {
                stage('step2 A') {
                    steps {
                        echo 'step 2 A'
                    }            
                }
                stage('step2 B') {
                    steps {
                        echo 'step 2 B'
                    }            
                }
            }
        }
        stage('step3') {
            steps {
                echo 'step 3'
            }            
        }        
    }
}