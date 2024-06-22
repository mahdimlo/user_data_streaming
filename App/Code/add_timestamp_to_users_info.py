from kafka import KafkaProducer, KafkaConsumer
from datetime import datetime
import json

try:
    consumer = KafkaConsumer("users_info", 
                             bootstrap_servers=['kafka-broker:29092'],
                             auto_offset_reset='earliest',
                             group_id='event-collector-group-1',
                             value_deserializer=lambda m: json.loads(m.decode('utf-8')),
                             security_protocol= 'PLAINTEXT'
                             )
    producer = KafkaProducer(bootstrap_servers=['kafka-broker:29092'], max_block_ms=5000)


    for message in consumer:
        try:
            data = message.value
            data["timestamp"] = str(datetime.utcnow())
            producer.send("timestamp_topic", json.dumps(data).encode('utf-8'))
        except Exception as e:
            print(f"Error processing message: {e}")

except KeyboardInterrupt:
    print("Script terminated by user.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    consumer.close()
    producer.close()
