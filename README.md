# User Data Streaming Project

## Introduction
This project is designed to fetch random user data from an external API, format the data, and stream it to a Kafka topic.
The primary goal is to demonstrate how to integrate data fetching, processing, and streaming using Python and Kafka.
Additionally, the project includes steps to add timestamps and labels to the data and finally save it to a PostgreSQL database.

![](Images/image.webp)

## Tools and Technologies
- __Python:__ The main programming language used for scripting and data processing.
- __Requests:__ A [Python](https://www.python.org/) library used to make HTTP requests to fetch data from the external API.
- __UUID:__ A Python module used to generate unique identifiers for each user.
- __Kafka:__ A distributed streaming platform used to publish and subscribe to streams of records.
- __KafkaProducer:__ A [Kafka](https://kafka.apache.org/) client used to send records to a Kafka topic.
- __KafkaConsumer:__ A Kafka client used to read records from a Kafka topic.
- __PostgreSQL:__ A powerful, open-source object-relational database system.
- __psycopg2:__ A [PostgreSQL]((https://www.postgresql.org/)) adapter for Python.

## Code Explanation
The project consists of several key components, each serving a specific purpose:
### stream_user_data_to_kafka.py
This script fetches random user data from the randomuser.me API, formats it into a structured dictionary,
and streams it to the users_info Kafka topic. The script runs for one minute, continuously fetching and sending data.
### add_timestamp_to_users_info.py
This script reads data from the users_info Kafka topic, adds a current UTC timestamp to each record,
and sends the updated records to the timestamp_topic Kafka topic. It ensures that each piece of user data is timestamped for tracking purposes.
### add_label_to_timestamped_data.py
This script reads data from the timestamp_topic Kafka topic, adds a random label (e.g., “Good”, “Bad”, “Excellent”, “Awful”, “Normal”) to each record, and sends the labeled records to the label_topic Kafka topic. This step simulates adding a qualitative assessment to the data.
### save_labeled_data_to_postgres.py
This script reads data from the label_topic Kafka topic and saves it to a PostgreSQL database. It extracts relevant fields from each record and inserts them into the user_data table, ensuring that all user information, along with the timestamp and label, is stored in the database.
## Project Diagram
Below is a diagram of the data flow in this project:
![](Images/Diagram.svg)

## Getting Started: Running the Project
- Ensure you have Docker and docker-compose installed on your system. If not, please follow the official [Docker](https://docs.docker.com/) installation guide for your operating system.

__Step 1: Clone the Repository__
1. Open your terminal.
2. Clone the project repository from GitHub to your local machine using the following command:
    ``` 
    git clone https://github.com/mahdimlo/user_data_streaming.git
    ```
__Step 2: Navigate to Project Directory__
1. Use the command line to navigate to the root directory of the project:
    ```
    cd user_data_streaming
    ```
__Step 3: Start Docker Containers__
1. Execute the following command to start all services defined in the docker-compose file:
   ```
   docker-compose up
   ```
   This command will build and start the Docker containers for various services in your project.



