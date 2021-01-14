#!/bin/sh
. ./deployment/setEnv.sh

if [ -z "$1" ]
  then
    echo "No argument supplied"
    exit
fi

app_env=$env_dev

if [ "$1" = "staging" ] 
then 
    app_env=$env_test
    server_address=$server_staging
elif [ "$1" = "production" ] 
then 
    app_env=$env_production
    server_address=$server_production
fi

echo "Server address: ${server_address}"
echo "Environment: ${app_env}"

if ["$server_address" = ""]
then
    exit
fi

ssh -o StrictHostKeyChecking=no -i "~/.ssh/TE-dev-v1.pem" $server_address<<EOF

#Stop and remove the running sudo docker
echo "Stopping and removing the old container..."

sudo docker stop $container_name
sudo docker rm $container_name

sudo docker image prune -f --all

#Delete the old version of the code
rm -rf rai 

echo " Cloning rai repository..."
#Clone the new repo and checkout the branch to be delivered
ssh-agent bash -c 'ssh-add ~/.ssh/TE-bitbucket; git clone git@bitbucket.org:ticketeasy-dev/rai.git'

cd rai

if [ -z "$2" ]
  then
    #No tag has been provided
    echo "Branch to be deployed: $1 " 
    git checkout $1
else
    echo "A specific tag has been selected: $2 "
    git checkout tags/$2
fi

#Build a new sudo sudo docker image starting from the sudo dockerfile
echo "Building the sudo docker image starting from the sudo docker file..."
sudo docker build -t $image_name .

echo "The following environment will be loaded: $app_env "

#TODO: jaeger host to be changed
sudo docker run -d --name $container_name --network="host" -e APP_ENV=Test -v ~/rai:/app --add-host jaeger:$jaeger_server $image_name

echo "Load successfull"
EOF