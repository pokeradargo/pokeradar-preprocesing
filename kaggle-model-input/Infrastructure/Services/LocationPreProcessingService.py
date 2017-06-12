from Infrastructure.Services.CloseToWaterDefinitionService import CloseToWaterDefinitionService
from Infrastructure.Services.PokeStopDistanceDefinitionService import PokeStopDistanceDefinitionService
from Infrastructure.Services.UrbanDefinitionService import UrbanDefinitionService
from Infrastructure.Services.TerrainDefinitionService import TerrainDefinitionService
from Infrastructure.Services.ContinentDefinitionService import ContinentDefinitionService
from Infrastructure.Services.GymDistanceDefinitionService import GymDistanceDefinitionService

class LocationPreProcessingService:
    @staticmethod
    def pre_processing_location(item):
        urbanization = UrbanDefinitionService.get_urban_definition(
            item.get('rural') == 'true',
            item.get('midurban') == 'true',
            item.get('suburban') == 'true',
            item.get('urban') == 'true',
        )
        terrain_type = TerrainDefinitionService.get_terrain_definition(
            int(item.get('terrainType'))
        )
        poke_stop_distance = PokeStopDistanceDefinitionService.get_poke_stop_distance_definition(
            item.get('pokestopIn100m') == 'true',
            item.get('pokestopIn250m') == 'true',
            item.get('pokestopIn500m') == 'true',
            item.get('pokestopIn1000m') == 'true',
            item.get('pokestopIn2500m') == 'true',
            item.get('pokestopIn5000m') == 'true',
        )
        gym_distance = GymDistanceDefinitionService.get_gym_distance_definition(
            item.get('gymIn100m') == 'true',
            item.get('gymIn250m') == 'true',
            item.get('gymIn500m') == 'true',
            item.get('gymIn1000m') == 'true',
            item.get('gymIn2500m') == 'true',
            item.get('gymIn5000m') == 'true',
        )
        close_to_water = CloseToWaterDefinitionService.get_close_to_water_definition(
            item.get('closeToWater')
        )
        continent = ContinentDefinitionService.get_continent_definition(
            item.get('continent')
        )
        return {
            'urbanization': urbanization,
            'terrain_type': terrain_type,
            'close_to_water': close_to_water,
            'poke_stop_distance': poke_stop_distance,
            'gym_distance': gym_distance,
            'continent': continent
        }
