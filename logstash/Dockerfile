# Dockerfile to build a Logstash container with the proper configuration

# Set the base image to Elastic's Logstash docker container
FROM docker.elastic.co/logstash/logstash:8.16.3

# Remove the old Logstash config
# Reference: https://www.elastic.co/guide/en/logstash/current/_configuring_logstash_for_docker.html#_custom_images
RUN rm -f /usr/share/logstash/pipeline/logstash.conf

# Copy the config to its config location
ADD file_to_http.conf /usr/share/logstash/pipeline/file_to_http.conf

RUN rm -f /usr/share/logstash/config/logstash.yml

ADD logstash.yml /usr/share/logstash/config/logstash.yml