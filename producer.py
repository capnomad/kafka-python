# Import KafkaProducer from Kafka library
from kafka import KafkaProducer
import configparser 
import sys

# Reading config from kafka_conf.ini
config = configparser.ConfigParser()
config.read('kafka_conf.ini')

# Define server with port
bootstrap_servers = config['kafka_config']['bootstrap_server']

# Define topic name where the message will publish
topicName = config['kafka_config']['topic']

# Initialize producer variable
producer = KafkaProducer(bootstrap_servers = bootstrap_servers)

# Publish text in defined topic
while True:
    try:
        print("\nEnter message to send: ", end="")
        msg = input()
        ack = producer.send(topicName, bytes(msg, 'utf8'))

        # Print message
        print("********** Message Sent **********")
        metadata = ack.get()
        print("Topic: ", metadata.topic)
        print("Partiton: ", metadata.partition)
        print("Message: ", msg)
    except KeyboardInterrupt:
        print("Shutting down Producer !!!!")
        sys.exit()
