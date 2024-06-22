from kafka import KafkaConsumer, KafkaProducer
import json
import random

labels = ["Good", "Bad", "Excellent", "Awful", "Normal"]

consumer = KafkaConsumer("timestamp_topic", 
                            bootstrap_servers=['kafka-broker:29092'],
                            auto_offset_reset='earliest',
                            group_id='event-collector-group-2',
                            value_deserializer=lambda m: json.loads(m.decode('utf-8')),
                            security_protocol= 'PLAINTEXT'
                            )
producer = KafkaProducer(bootstrap_servers=['kafka-broker:29092'], max_block_ms=5000)

for message in consumer:
    try:
        data = message.value
        data["labels"] = random.choice(labels)
        producer.send("label_topic", json.dumps(data).encode("utf-8"))
    except Exception as e:
        print(f"Error processing message: {e}")
