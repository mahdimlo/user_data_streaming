from kafka import KafkaConsumer
import psycopg2
import json

connection_params = {
    "dbname": "user",
    "user": "postgres",
    "password": "postgres123",
    "host": "postgres",
    "port": "5432"
}

consumer = KafkaConsumer("label_topic", 
                            bootstrap_servers=['kafka-broker:29092'],
                            auto_offset_reset='earliest',
                            group_id='event-collector-group-3',
                            value_deserializer=lambda m: json.loads(m.decode('utf-8')),
                            security_protocol= 'PLAINTEXT'
                            )

with psycopg2.connect(**connection_params) as connect:
    with connect.cursor() as cursor:
        for message in consumer:
            try:
                data = message.value
                user_id = data.get('id')
                first_name = data.get('first_name')
                last_name = data.get('last_name')
                gender = data.get('gender')
                address = data.get('address')
                post_code = data.get('post_code')
                email = data.get('email')
                dob = data.get('dob')
                registered_date = data.get('registered_date')
                phone = data.get('phone')
                picture = data.get('picture')
                timestamp = data.get("timestamp")
                labels = data.get("labels")

                cursor.execute("""
                    INSERT INTO user_data 
                    (id, first_name, last_name, gender, address, post_code, email, dob, registered_date, phone, picture, timestamp, labels) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, (user_id, first_name, last_name, gender, address, post_code, email, dob, registered_date, phone, picture, timestamp, labels))
                connect.commit()
            except Exception as e:
                print(f"Error processing message: {e}")
