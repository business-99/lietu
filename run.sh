docker network create blabla
docker build --rm -t lietuops:0.1 .
docker run --name lietuops --privileged=true -e HOST_IP="172.30.66.80" --network=blabla -v $(pwd)/static:/home/src/static -v $(pwd)/db.sqlite3:/home/db.sqlite3 -v $(pwd)/src/scriptfile:/home/src/scriptfile -d lietuops:0.1
docker run -p 8090:80 --name lietunginx --privileged=true --network=blabla -v $(pwd)/nginx/www:/www -v $(pwd)/static:/static -v $(pwd)/nginx/conf.d:/etc/nginx/conf.d -v $(pwd)/nginx/log:/var/log/nginx -d nginx