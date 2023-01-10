import time

import pika


RABBIT_HOST = "127.0.0.1"
USERNAME = "guest"
PASSWORD = "guest"

credentials = pika.PlainCredentials(username=USERNAME, password=PASSWORD)


def callback(ch, method, proties, body):
    print(f"[EVENT] => {body} sending email")
    time.sleep(2)


try:
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=RABBIT_HOST, credentials=credentials)
    )

    channel = connection.channel()
    channel.queue_declare(queue="pl-api-email")

    channel.basic_consume(
        queue="pl-api-email", on_message_callback=callback, auto_ack=True
    )

    channel.start_consuming()
except Exception as e:
    print(f"[ERROR] {e}")