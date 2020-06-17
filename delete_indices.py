#!/usr/bin/env python
import time
import base64
import urllib
from elasticsearch import Elasticsearch

# Information used to build the URL used to access the ElasticSearch API
ES_HOST='localhost'
ES_PORT='9200'


#Function to delete indices 

def delete_index(): 
    ES_CONECTION = '%s:%s' % (ES_HOST, ES_PORT )
    BODY = {
"query": {
"range" : {
"@timestamp" : {
    "lt" : "now"

}
}
}
}
    es = Elasticsearch({ES_CONECTION} )

    es.delete_by_query(index='filebeat-*', body=BODY)



def main():
    print ('INFO: Starting task')
    delete_index()
    print ('INFO: Completed')
# #############################################################################
if __name__ == "__main__":
    main()