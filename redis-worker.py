import time
import redis

r = redis.Redis(host='127.0.0.1', port=6379, db=0)

sub = r.pubsub()
sub.subscribe('api-email')

while True:
    message = sub.get_message()

    if message:
        email = str(message["data"])
        print(f"Sendning email => {email} to external API")
    time.sleep(5)
