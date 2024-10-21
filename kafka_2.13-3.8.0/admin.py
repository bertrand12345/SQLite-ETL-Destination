from kafka.admin import KafkaAdminClient, NewTopic
from kafka.errors import TopicAlreadyExistsError

admin_client = KafkaAdminClient(bootstrap_servers="localhost:9092", client_id='test')
topic_list = []
new_topic = NewTopic(name="bankbranch", num_partitions=2, replication_factor=1)
topic_list.append(new_topic)

try:
    admin_client.create_topics(new_topics=topic_list)
    print("Topic created successfully.")
except TopicAlreadyExistsError:
    print("Topic 'bankbranch' already exists.")
