pipeline {
    agent any
    environment {
        BRANCH='Release'
    }
    stages {
        stage('step1') {
            steps {
                echo 'script 1 - step 1'
                sh 'printenv'
            }            
        }
        stage('step2') {
            when {
                 expression { BRANCH ==~ /(Master|Hotfix)/ }
            }
            steps {
                echo 'script 1 - step 2'
            }
        }    
        stage('step3') {
            when {
                 expression { BRANCH ==~ /(Release)/ }
            }            
            steps {
                echo 'script 1 - step 3'
            }
        }           
    }
}