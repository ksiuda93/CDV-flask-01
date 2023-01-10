import redis

r = redis.Redis(host='127.0.0.1', port=6379, db=0)


def create_msg(queue, msg):
    r.publish(queue, msg)
