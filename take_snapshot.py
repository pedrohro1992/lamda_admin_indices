#!/usr/bin/env python
import time
import base64
import urllib
from elasticsearch import Elasticsearch
# Information used to build the URL used to access the ElasticSearch API
ES_HOST='localhost'
ES_PORT='9200'
# #############################################################################
def lambda_handler(event, context):
    print ('INFO: Lambda handler activated')
    #print ('INFO: Event ID is %s' % event['id'])
    main()
# #############################################################################
def create_snapshot():
    #Create conection string
    ES_CONECTION = '%s:%s' % (ES_HOST, ES_PORT )
    es = Elasticsearch({ES_CONECTION} )
    REPOSITORY = 'snapshot-localhost-s3'
    INDEX_BODY = {
        "indices": "filebeat*"
    }
    SNAPSHOT='index_snapshot_%s' % time.strftime('%Y_%m_%d')
    es.snapshot.create(repository=REPOSITORY, snapshot=SNAPSHOT, body=INDEX_BODY)
# #############################################################################
def main():
    print ('INFO: Starting task')
    create_snapshot()
    print ('INFO: Completed')
# #############################################################################
if __name__ == "__main__":
    main()