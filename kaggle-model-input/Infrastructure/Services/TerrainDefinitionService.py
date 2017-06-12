class TerrainDefinitionService:
    @staticmethod
    def get_terrain_definition(terrain_type):
        if terrain_type == 0:
            return "Water"
        elif terrain_type == 1:
            return "Evergreen Needleleaf forest"
        elif terrain_type == 2:
            return "Evergreen Broadleaf forest"
        elif terrain_type == 3:
            return "Deciduous Needleleaf forest"
        elif terrain_type == 4:
            return "Deciduous Broadleaf forest"
        elif terrain_type == 5:
            return "Mixed forest"
        elif terrain_type == 6:
            return "Closed shrublands"
        elif terrain_type == 7:
            return "Open shrublands"
        elif terrain_type == 8:
            return "Woody savannas"
        elif terrain_type == 9:
            return "Savannas"
        elif terrain_type == 10:
            return "Grasslands"
        elif terrain_type == 11:
            return "Permanent wetlands"
        elif terrain_type == 12:
            return "Croplands"
        elif terrain_type == 13:
            return "Urban and built-up"
        elif terrain_type == 14:
            return "Cropland/Natural vegetation mosaic"
        elif terrain_type == 15:
            return "Snow and ice"
        elif terrain_type == 16:
            return "Barren or sparsely vegetated"
        else:
            return "Unknown"
