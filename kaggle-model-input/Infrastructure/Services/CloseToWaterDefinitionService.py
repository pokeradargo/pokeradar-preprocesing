class CloseToWaterDefinitionService:
    @staticmethod
    def get_close_to_water_definition(is_close_to_water):
        if is_close_to_water:
            return 'Yes'
        else:
            return 'No'
