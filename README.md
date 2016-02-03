# コンテナ起動
docker run --name=pukiwiki -d -p=10080:80 -v /etc/localtime:/etc/localtime:ro -v /your/docker/dir:/var/www snowmoon1242/pukiwiki:1.5.0
