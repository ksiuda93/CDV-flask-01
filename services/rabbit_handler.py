import pika


def create_msg(queue_name, msg_body):
    USERNAME = "guest"
    PASSWORD = "guest"
    RABBITMQ_HOST = "127.0.0.1"

    credentials = pika.PlainCredentials(username=USERNAME, password=PASSWORD)

    try:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=RABBITMQ_HOST, credentials=credentials)
        )

        channel = connection.channel()
        channel.queue_declare(queue=queue_name)
        channel.basic_publish(exchange='', routing_key=queue_name, body=msg_body)
        print(f"[EVENT] => {msg_body} has been sent to RabbitMQ")
    except Exception as e:
        print(f"[ERROR] {e}")

