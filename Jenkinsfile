pipeline{
        agent any
        stages{
            stage('Test'){
                steps{
                    sh "pytest tests --cov=service1 --cov=service2 --cov=service3 --cov=service4"
                }
            }
            stage('Build'){
                steps{
                    sh ""
                }
            }
        }
}