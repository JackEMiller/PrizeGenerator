pipeline{
        agent any
        stages{
            stage('Prerequisites'){
                steps{
                    sh 'pip3 install -r requirements.txt'
                }
            }
            stage('Test'){
                steps{
                    sh "python3 -m pytest tests --cov=service1 --cov=service2 --cov=service3 --cov=service4"
                }
            }
            stage('Build'){
                steps{
                    sh ""
                }
            }
        }
}