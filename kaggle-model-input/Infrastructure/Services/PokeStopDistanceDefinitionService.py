class PokeStopDistanceDefinitionService:
    @staticmethod
    def get_poke_stop_distance_definition(
            is_near_100m,
            is_near_250m,
            is_near_500m,
            is_near_1000m,
            is_near_2500m,
            is_near_5000m
    ):
        if is_near_100m:
            return 'pokestopIn100m'
        elif is_near_250m:
            return 'pokestopIn250m'
        elif is_near_500m:
            return 'pokestopIn500m'
        elif is_near_1000m:
            return 'pokestopIn1000m'
        elif is_near_2500m:
            return 'pokestopIn2500m'
        elif is_near_5000m:
            return 'pokestopIn5000m'
        else:
            return 'pokestopIn+5000m'
