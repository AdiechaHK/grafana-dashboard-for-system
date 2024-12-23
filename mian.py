#!/usr/bin/env python
import pika

def callback(ch, method, properties, body):
    print(f" [x] Received {body}")

def produce(message):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='hello')
    channel.basic_publish(exchange='',
                        routing_key='hello',
                        body=message)
    print(f" [x] Sent {message}")
    connection.close()

def consume():
    channel.basic_consume(queue='hello',
                      auto_ack=True,
                      on_message_callback=callback)

