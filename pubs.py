import os
from google.cloud import pubsub_v1
import mysql.connector
import pandas as pd

credentials_path = 'directory to json credential'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

publisher = pubsub_v1.PublisherClient()
topic_path = 'your-pubsub-topics'


#data = 'first message'
def conntomysql(q):
    conn = mysql.connector.connect(
        host='your compute engine external ip',
        port='your port',
        user='user',
        password='password',
        db = 'yourdb'
    )
    

    data = pd.read_sql_query(q, conn)
    
    return data

q = 'select * from table'
data = conntomysql(q)
data = bytes(data.to_csv(line_terminator='\r\n', index=False), encoding='utf-8')


future = publisher.publish(topic_path, data)
print(f'published message id {future.result()}')
