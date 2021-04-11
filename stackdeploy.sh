#!/bin/bash
sudo docker login --username=$DOCKERHUB_USR --password=$DOCKERHUB_PSW
sudo docker pull jmiller2612/prizepipeline_service1:1
sudo docker pull jmiller2612/prizepipeline_service2:1
sudo docker pull jmiller2612/prizepipeline_service3:1
sudo docker pull jmiller2612/prizepipeline_service4:1
sudo docker stack deploy --compose-file docker-compose.yaml prizegeneratorstack