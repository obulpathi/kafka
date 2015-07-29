# kafka
Publish-subscribe messaging rethought as a distributed commit log

* Kafka has very good performance, but there are some rough edges around guarantees
* Consumption and production is done in small sizes batches, this is done in order to achieve higher performance
* Check pointing on production and consumption side is done on a coarse grained level, which creates lots of problems for one time guarantees
* kafka brokers are stateless, and all the state is stored in ZooKeeper
* If a node (Producer, Consumer or Kafka Broker) crashes and restarted, it resumes from the last checkpointed state in ZooKeeper
* This leads to duplicate or dropped messages if not carefully worked around in code
* Also this solution is kind of redundant to transfer files from FTP Server to Kafka and then stream them to HDFS and process by Spark (Rather than transferring files from FTP Server to HDFS)
* Kafka is really good as a realtime storage for Analytics solutions
* As a storage for Batch Data, HDFS is much better than Kafka
