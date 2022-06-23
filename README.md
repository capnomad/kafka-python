# kafka-python
A sample Kafka Producer-Consumer application in python. We can install kafka broker on 

#### What is Kafka? :
* It’s a Pub-sub messaging system. 
* Publishers are called Producers. Subscribers are called Consumers 
* Producer sends messages to Topic. Consumer retrieve from Topic
* Kafka keeps topics in Broker. Also called a Server. Broker has access to machine resources, like filesystem.
* Distribution is handled by scaling number of Brokers without affecting Producers and Consumers.
* Kafka Cluster is a group of multiple Kafka Brokers. It can have single Broker on a single Machine or multiple. 
* Cluster of 1 = Single Broker running on single Machine
* Cluster of 2 = Two Brokers running on single Machine
![image](https://user-images.githubusercontent.com/23707225/175257475-46e194a1-21db-4686-a273-b273e141a37e.png)

#### What are Kafka Topics? :
* Central kafka abstraction
* Named feed of messages
* Producer produces a topic
* Consumer consumes a topic
* Topics are Logical entity
* Physically represented as a log

#### What is Apache Zookeeper? :
* Apache Zookeeper is a Distributed system. 
* Centralized service for maintaining metadata about the cluster, 
  *  Config information
  *  Health status
  *  Group membership
  *  Used with: `Hadoop`, `Hbase`, `Mesos`, `Solr`, `Redis`, `Neo4j`

#### Kafka's Distributed Architecture
![image](https://user-images.githubusercontent.com/23707225/175257748-782a8500-5778-4ee9-b861-67069c2f9d1e.png)


## Prerequisites:
- WSL2 enabled on windows
- Linux distribution intalled and setup from [Microsoft Store](https://apps.microsoft.com/store/detail/ubuntu/9PDXGNCFSCZV)
- Python 3 
- OpenJDK or Oracle JDK



## Install Dependencies

Update Packages: 
In the Ubuntu shell opened above run the package manager to get the latest updates.
```
sudo apt-get update && sudo apt-get upgrade -y
```

Install JDK: 
Apache Kafka requires Java runtime version 8 or above, install Java by using the command below in Ubuntu shell:
```
sudo apt install openjdk-8-jdk -y
```

## Download Kafka
Download the Apache Kafka tarball using the command below in shell. This will download Apache Kafka version 2.8.0
```
wget https://downloads.apache.org/kafka/2.8.0/kafka_2.13-2.8.0.tgz
```

Run the command to untar the Kafka archive and change the directory to Kafka.
```
tar -zxf kafka_2.13-2.8.0.tgz
cd kafka_2.13-2.8.0
```


## Run the Kafka Cluster
Zookeaper: Run below command to start Zookeeper

```
bin/zookeeper-server-start.sh config/zookeeper.properties
```

Kafka Server: 
Open another terminal and run below command

```
bin/kafka-server-start.sh config/server.properties
```
  


## Run Python producer and consumer

Install Python 3 and run below commands in different terminal windows

```
python producer.py
```

```
python consumer.py
```

## References 
* [How to Install Apache Kafka on Windows WSL 2?](https://dcrunch.dev/blog/kafka/set-up-and-run-apache-kafka-on-windows-wsl-2/)
* https://downloads.apache.org/kafka/2.8.0/kafka_2.13-2.8.0.tgz
