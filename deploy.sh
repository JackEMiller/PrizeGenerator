scp dockerstack-compose.yaml jenkins@docker-master:docker-compose.yaml
scp stackdeploy.sh jenkins@docker-master:stackdeploy.sh
rm databaseuri.txt
touch databaseuri.txt
echo $DATABASEURI
echo $DATABASEURI >> databaseuri.txt
cat databaseuri.txt
scp databaseuri.txt jenkins@docker-master:databaseuri.txt
ssh jenkins@docker-master << EOF
    export DB_URI=$(cat databaseuri.txt)
    sudo docker login --username=$DOCKERHUB_USR --password=$DOCKERHUB_PSW
    sudo docker pull jmiller2612/prizepipeline_service1:1
    sudo docker pull jmiller2612/prizepipeline_service2:1
    sudo docker pull jmiller2612/prizepipeline_service3:1
    sudo docker pull jmiller2612/prizepipeline_service4:1
    sudo docker stack deploy --compose-file docker-compose.yaml prizegeneratorstack
#ssh jenkins@docker-master echo $DATABASE_URI
#ssh jenkins@docker-master 
EOF