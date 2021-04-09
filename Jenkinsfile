pipeline{
        agent any
        stages{
            stage('Prerequisites'){
                steps{
                    sh 'pip3 install flask-testing'
                }
            }
            stage('Test'){
                steps{
                    sh "python3 -m pytest tests --cov=service1 --cov=service2 --cov=service3 --cov=service4"
                }
            }
            stage('Build images'){
                steps{
                    sh "sudo docker-compose build"
                }
            }
            stage('Push images to dockerhub'){
                steps{
                    sh ''
                }

            }
            stage('Configure VMs'){
                steps{
                    sh ''
                    sh '/home/jenkins/.local/bin/ansible-playbook -i ansible-docker/inventory.yaml ansible-docker/playbook.yaml'
                }

            }
            stage('deploy to swarm'){
                steps{
                    sh ''
                }

            }
        }
}