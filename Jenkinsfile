pipeline{
        agent any
        environment{
            DATABASE_URI = credentials("DATABASE_URI")
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
                    sh 'sudo echo $DATABASE_URI'
                    sh 'python3 -m pytest tests --cov=service1 --cov=service2 --cov=service3 --cov=service4'
                }
            }
            stage('Build images'){
                steps{
                    sh 'touch env.env'
                    sh 'echo DATABASE_URI=$DATABASE_URI >> env.env'
                    sh 'docker-compose build --build-arg DATABASE_URI=$DATABASE_URI'
                }
            }
            stage('Push images to dockerhub'){
                steps{
                    sh 'docker login --username=$DOCKERHUB_USR --password=$DOCKERHUB_PSW'
                    sh 'docker tag prizepipeline_service1 jmiller2612/prizepipeline_service1:1'
                    sh 'docker tag prizepipeline_service2 jmiller2612/prizepipeline_service2:1'
                    sh 'docker tag prizepipeline_service3 jmiller2612/prizepipeline_service3:1'
                    sh 'docker tag prizepipeline_service4 jmiller2612/prizepipeline_service4:1'
                    sh 'docker push jmiller2612/prizepipeline_service1:1'
                    sh 'docker push jmiller2612/prizepipeline_service2:1'
                    sh 'docker push jmiller2612/prizepipeline_service3:1'
                    sh 'docker push jmiller2612/prizepipeline_service4:1'
                }

            }
            stage('Configure VMs'){
                steps{
                    sh '/home/jenkins/.local/bin/ansible-playbook -i ansible-docker/inventory.yaml ansible-docker/playbook.yaml'
                }

            }
            stage('deploy to swarm'){
                steps{
                    sh 'bash deploy.sh'
                }

            }
        }
}