pipeline{
        agent any
        environment{
            DATABASEURI = credentials("DATABASEURI")
            DOCKERHUB = credentials("DOCKERHUB")
        }
        stages{
            stage('Prerequisites'){
                steps{
                    sh 'pip3 install pymysql'
                }
            }
            stage('Test'){
                steps{
                    sh 'echo $DATABASEURI'
                    sh "python3 -m pytest tests --cov=service1 --cov=service2 --cov=service3 --cov=service4"
                }
            }
            stage('Build images'){
                steps{
                    sh ""
                    sh "sudo docker-compose build"
                }
            }
            stage('Push images to dockerhub'){
                steps{
                    sh 'docker login --username=${env.DOCKERHUB_USR} --password=${env.DOCKERHUB_USR}'
                    sh 'docker push service1'
                    sh 'docker push service2'
                    sh 'docker push service3'
                    sh 'docker push service4'
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