#!/usr/bin/env python3

from datetime import datetime
import os
import random
import threading
import time

import boto3

producers = int(os.environ.get('PRODUCERS'))
if producers is None:
    producers = 1

consumers = int(os.environ.get('CONSUMERS'))
if consumers is None:
    consumers = 5

rate = int(os.environ.get('RATE'))
if rate is None:
    rate = 5

queue_url = os.environ.get('QUEUE_URL')
if queue_url is None:
    exit(1)


class Publisher(threading.Thread):
    def __init__(self, name, rate):
        threading.Thread.__init__(self)
        self.name = name
        self.rate = rate

        # each thread has its own client
        self.sqs = boto3.client('sqs')

    def run(self):
        print("Starting " + self.name)

        # sleep for a random amount of time, then send a message, repeat

        while True:
            # Send message to SQS queue
            response = self.sqs.send_message(
                QueueUrl=queue_url,
                DelaySeconds=0,
                MessageAttributes={
                    'Thread': {
                        'DataType': 'String',
                        'StringValue': self.name
                    }
                },
                MessageBody=(
                    "This message was produced by {} AT {}".format(self.name, datetime.now())
                )
            )

            print("{} Produced new message at {}".format(self.name, datetime.now()))


            time.sleep(random.uniform(0, rate))



class Consumer(threading.Thread):
    def __init__(self, name, rate):
        threading.Thread.__init__(self)
        self.name = name
        self.rate = rate

        # each thread has its own client
        self.sqs = boto3.client('sqs')

    def run(self):
        print("Starting " + self.name)

        while True:
            time.sleep(random.uniform(0, rate))

            # Receive message from SQS queue
            response = self.sqs.receive_message(
                QueueUrl=queue_url,
                AttributeNames=[
                    'SentTimestamp'
                ],
                MaxNumberOfMessages=1,
                MessageAttributeNames=[
                    'All'
                ],
                VisibilityTimeout=0,
                WaitTimeSeconds=0
            )

            if isinstance(response, dict) and 'Messages' in response:
                message = response['Messages'][0]
                receipt_handle = message['ReceiptHandle']

                # Delete received message from queue
                self.sqs.delete_message(
                    QueueUrl=queue_url,
                    ReceiptHandle=receipt_handle
                )
                print("{} Received and deleted message: {}".format(self.name, message['Body']))


if __name__ == '__main__':
    threads = []
    for i in range(producers):
        publisher_thread = Publisher('publisher-{}'.format(i), rate)
        threads.append(publisher_thread)

    for i in range(consumers):
        consumer_thread = Consumer('consumer-{}'.format(i), rate)
        threads.append(consumer_thread)

for thread in threads:
        thread.start()

