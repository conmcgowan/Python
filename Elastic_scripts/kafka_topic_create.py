from kafka.admin import KafkaAdminClient, NewTopic
import logging
from org_pipeline_automation import *


class kafka_pipeline_manager:
    def __init__(self):
        self.__admin_client = KafkaAdminClient(
            bootstrap_servers="localhost:9092", 
            client_id='loremIpsum'
            )
         
    def create(self, org_name):
        resp = self.__createTopic(org_name)
        return resp
                
    def __createTopic(self, org_name):
        topic_list = []
        try:
            #grabs topics and appends to list, which allows multiple updates at once
            #TODO Change partions and replication factors to standard
            topic_list.append(NewTopic(name="pcf_%s" % org_name))
            self.admin_client.create_topics(new_topics=topic_list, validate_only=False)
            return "kafka topic successfully created for org {0}".format(org_name)
        except Exception as e:
            logging.error(e)
            return "failed to create kafka topic for {0}".format(org_name)

#def main():
#    createTopic()
    
if __name__ == "__main__":
    pass