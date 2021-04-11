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
                    sh 'sudo usermod -aG docker ${USER}'
                    sh 'sudo su - ${USER}'
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
                    sh 'sudo docker images -a'
                    sh 'sudo docker login --username=$DOCKERHUB_USR --password=$DOCKERHUB_PSW'
                    sh 'IMAGE_ID=$(sudo docker images --filter=reference=prizepipeline_service1 --format "{{.ID}}"'
                    sh 'sudo docker push jmiller2612/$IMAGE_ID:latest'
                    sh 'IMAGE_ID=$(sudo docker images --filter=reference=prizepipeline_service2 --format "{{.ID}}"'
                    sh 'sudo docker push localhost:5002/jmiller2612/$IMAGE_ID:latest'
                    sh 'IMAGE_ID=$(sudo docker images --filter=reference=prizepipeline_service3 --format "{{.ID}}"'
                    sh 'sudo docker push localhost:5003/jmiller2612/$IMAGE_ID:latest'
                    sh 'IMAGE_ID=$(sudo docker images --filter=reference=prizepipeline_service4 --format "{{.ID}}"'
                    sh 'sudo docker push localhost:5004/jmiller2612/$IMAGE_ID:latest'
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