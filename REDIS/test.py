import redis

REDIS_CON = {
    "host":'127.0.0.1',
    "port":6379,
    "db":2,
    "decode_responses":True 
}

con = redis.Redis(**REDIS_CON)
print(con.rpop('z'))
