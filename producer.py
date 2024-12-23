#!/usr/bin/env python
import pika
import sys


def produce(message):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    channel.basic_publish(exchange='', routing_key='hello', body=message)
    print(f" [x] Sent '{message}'")
    connection.close()

if __name__ == '__main__':
    produce(" ".join(sys.argv[1:]))