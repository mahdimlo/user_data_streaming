FROM python:3.11

RUN apt update && apt install -y cron libpq-dev

ENV TZ=Asia/Tehran
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

ADD Code /code

RUN python3 -m venv /code/venv
RUN /code/venv/bin/pip install --upgrade pip
RUN /code/venv/bin/pip install -r /code/requirement.txt
RUN /code/venv/bin/pip install six

ENV schedule="* * * * *"
ENV python="/code/venv/bin/python"
ENV log_file_stream_user_data_to_kafka="/code/stream_user_data_to_kafka.log"
ENV log_file_add_timestamp_to_users_info="/code/add_timestamp_to_users_info.log"
ENV log_file_add_label_to_timestamped_data="/code/add_label_to_timestamped_data.log"
ENV log_file_save_labeled_data_to_postgres="/code/save_labeled_data_to_postgres.log"

RUN echo "$schedule $python /code/stream_user_data_to_kafka.py >> $log_file_stream_user_data_to_kafka 2>&1" > /etc/cron.d/data_pipeline_cron
RUN echo "$schedule $python /code/add_timestamp_to_users_info.py >> $log_file_add_timestamp_to_users_info 2>&1" >> /etc/cron.d/data_pipeline_cron
RUN echo "$schedule $python /code/add_label_to_timestamped_data.py >> $log_file_add_label_to_timestamped_data 2>&1" >> /etc/cron.d/data_pipeline_cron
RUN echo "$schedule $python /code/save_labeled_data_to_postgres.py >> $log_file_save_labeled_data_to_postgres 2>&1" >> /etc/cron.d/data_pipeline_cron

RUN chmod 0644 /etc/cron.d/data_pipeline_cron

RUN crontab /etc/cron.d/data_pipeline_cron

RUN touch /var/log/cron.log

CMD cron && tail -f /var/log/cron.log