
# mongodb 4.4.4

docker stop mongo
docker rm mongo

rm -rf /usr/local/mongo/db
docker run -itd --name mongo -p 27017:27017 -v /usr/local/mongo/db:/data/db  mongo --auth

docker exec -it mongo mongo admin
db.createUser({ user:'admin',pwd:'123456',roles:[ { role:'userAdminAnyDatabase', db: 'admin'},"readWriteAnyDatabase",{ role: "__system", db: "admin" }]});

