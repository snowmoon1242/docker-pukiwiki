# run container
docker run --name=pukiwiki -d -p=10080:80 -v /etc/localtime:/etc/localtime:ro snowmoon1242/pukiwiki:1.5.0 &
