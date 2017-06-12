from pymongo import MongoClient
from Infrastructure.Services.LocationPreProcessingService import LocationPreProcessingService
from Infrastructure.Services.TimePreProcessingService import TimePreProcessingService
from Infrastructure.Services.WeatherPreProcessingService import WeatherPreProcessingService
from Infrastructure.Services.CoRelationsService import CoRelationsService

class MongoRepository:
    ServerIp = ''
    ServerPort = ''

    def __init__(self, server_ip, server_port):
        self.ServerIp = server_ip
        self.ServerPort = server_port

    def connect_to_database(self):
        client = MongoClient(self.ServerIp, self.ServerPort)
        db = client['datalake']
        return db['kaggle-datalake']

    def get_all(self):
        collection = self.connect_to_database()

        for item in collection.find():
            pokemon_id = item.get('pokemonId')
            location_data = LocationPreProcessingService.pre_processing_location(item)
            time_data = TimePreProcessingService.pre_processing_time(item)
            weather_data = WeatherPreProcessingService.pre_processing_weather(item)
            co_relations = CoRelationsService.init_correlations(item)
            old_co_relations = self.find_item_by_index(pokemon_id, location_data, time_data, weather_data)
            if old_co_relations is not None:
                co_relations = CoRelationsService.increase_correlations(
                    old_co_relations,
                    co_relations
                )
                self.update_items_by_index(pokemon_id, location_data, time_data, weather_data, co_relations)

            item_preprocessed = {
                'pokemon_id': pokemon_id,
                **location_data,
                **time_data,
                **weather_data,
                **co_relations
            }
            self.persist_item(item_preprocessed)

    def find_item_by_index(self, pokemon_id, location_data, time_data, weather_data):
        client = MongoClient(self.ServerIp, self.ServerPort)
        db = client['datainput']
        item = db['datainput'].find_one({
            'pokemon_id': pokemon_id,
            **location_data,
            **time_data,
            **weather_data,
        })
        return item

    def update_items_by_index(self, pokemon_id, location_data, time_data, weather_data, co_relations):
        client = MongoClient(self.ServerIp, self.ServerPort)
        db = client['datainput']
        db['datainput'].update_many(
            {
                'pokemon_id': pokemon_id,
                **location_data,
                **time_data,
                **weather_data,
            },
            {
                "$set": co_relations
            }
        )

    def persist_item(self, item):
        client = MongoClient(self.ServerIp, self.ServerPort)
        db = client['datainput']
        db['datainput'].insert_one(item)