pipeline {
    agent any
    environment {
        BRANCH='Master'
    }
    stages {
        stage('step1') {
            steps {
                echo 'script 1 - step 1'
                sh 'printenv'
            }            
        }
        stage('step2') {
            steps {
                echo 'script 1 - step 2'
                sh 'printenv'
            }
        }    
    }
}