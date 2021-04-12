scp dockerstack-compose.yaml jenkins@docker-master:docker-compose.yaml
scp stackdeploy.sh jenkins@docker-master:stackdeploy.sh
rm databaseuri.txt
touch databaseuri.txt
echo $DATABASEURI
echo $DATABASEURI >> databaseuri.txt
cat databaseuri.txt
scp databaseuri.txt jenkins@docker-master:databaseuri.txt
ssh jenkins@docker-master << EOF
    export DATABASE_URI=$DATABASE_URI
    docker login --username=$DOCKERHUB_USR --password=$DOCKERHUB_PSW
    docker pull jmiller2612/prizepipeline_service1:1
    docker pull jmiller2612/prizepipeline_service2:1
    docker pull jmiller2612/prizepipeline_service3:1
    docker pull jmiller2612/prizepipeline_service4:1
    docker stack deploy --compose-file docker-compose.yaml prizegeneratorstack
#ssh jenkins@docker-master echo $DATABASE_URI
#ssh jenkins@docker-master 
EOF