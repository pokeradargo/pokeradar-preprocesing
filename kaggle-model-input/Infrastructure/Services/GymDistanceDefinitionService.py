class GymDistanceDefinitionService:
    @staticmethod
    def get_gym_distance_definition(
            is_near_100m,
            is_near_250m,
            is_near_500m,
            is_near_1000m,
            is_near_2500m,
            is_near_5000m
    ):
        if is_near_100m:
            return 'gymIn100m'
        elif is_near_250m:
            return 'gymIn250m'
        elif is_near_500m:
            return 'gymIn500m'
        elif is_near_1000m:
            return 'gymIn1000m'
        elif is_near_2500m:
            return 'gymIn2500m'
        elif is_near_5000m:
            return 'gymIn5000m'
        else:
            return 'gymIn+5000m'
