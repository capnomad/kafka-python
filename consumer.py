# Import KafkaConsumer from Kafka library
from kafka import KafkaConsumer
import sys
import configparser 

# Reading config from kafka_conf.ini
config = configparser.ConfigParser()
config.read('kafka_conf.ini')

# Define server with port
bootstrap_servers =config['kafka_config']['bootstrap_server']

# Define topic name from where the message will recieve
topicName = config['kafka_config']['topic']

# Initialize consumer variable
consumer = KafkaConsumer (topicName, group_id = 'group1',bootstrap_servers = bootstrap_servers,
auto_offset_reset = 'earliest')
print("~~~~~~~~~~~ Waiting for producer to publish ~~~~~~~~~~~")

# Read and print message from consumer
try:
    for msg in consumer:
        # Print message
        print("\n********** Message received **********")
        print("Topic: ", msg.topic)
        print("Partiton: ", msg.partition)
        print("Message: ", msg.value)

        print("\n~~~~~~~~~~~ Waiting for producer to publish ~~~~~~~~~~~")
except KeyboardInterrupt:
    print("Stopping consumer !!!")
    # Terminate the script
    sys.exit()
