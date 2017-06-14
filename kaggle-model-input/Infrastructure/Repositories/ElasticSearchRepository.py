from elasticsearch import Elasticsearch


class ElasticSearchRepository:
    ServerIp = "pokeradar-elastic-master-dev.sandbox"
    ServerPort = 9200

    def connect_to_database(self):
        return Elasticsearch(hosts={
            self.ServerIp: self.ServerPort
        })

    def persist_item(self, item):
        client = self.connect_to_database()
        client.index(
            index="datainput",
            doc_type="json",
            body=item
        )
