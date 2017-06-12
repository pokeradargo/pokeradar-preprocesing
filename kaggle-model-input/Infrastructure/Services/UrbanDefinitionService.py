class UrbanDefinitionService:
    @staticmethod
    def get_urban_definition(
            rural,
            mid_urban,
            sub_urban,
            urban
    ):
        if rural:
            return 'rural'
        elif mid_urban and sub_urban and urban:
            return 'urban'
        elif mid_urban and sub_urban:
            return 'suburban'
        else:
            return 'midurban'
