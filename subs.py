import os
from google.cloud import pubsub_v1
from concurrent.futures import TimeoutError

credentials_path = 'your path to json credential'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

subscriber = pubsub_v1.SubscriberClient()
subscription_path = 'your subscription path'

def callback(message):
    print(f'Recieved Message: {message}')
    print(f'data: {message.data}')
    message.ack()

streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)
print(f'Listening for messages on {subscription_path}')

with subscriber:
    try:
        streaming_pull_future.result()
    except:
        streaming_pull_future.cancel()
        streaming_pull_future.result()
