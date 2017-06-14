from Infrastructure.Services.TemperatureDefinitionService import TemperatureDefinitionService
from Infrastructure.Services.PressureDefinitionService import PressureDefinitionService
from Infrastructure.Services.WindSpeedDefinitionService import WindSpeedDefinitionService
from Infrastructure.Services.WeatherIconDefinitionService import WeatherIconDefinitionService


class WeatherPreProcessingService:
    @staticmethod
    def pre_processing_weather(item):
        temperature = TemperatureDefinitionService.get_temperature_definition(
            float(item.get('temperature'))
        )
        pressure = PressureDefinitionService.get_pressure_definition(
            float(item.get('pressure'))
        )
        wind_speed = WindSpeedDefinitionService.get_wind_speed_definition(
            float(item.get('windSpeed'))
        )
        weather_icon = WeatherIconDefinitionService.get_weather_icon_definition(
            item.get('weatherIcon')
        )
        return {
            'temperature': temperature,
            'pressure': pressure,
            'wind_speed': wind_speed,
            'weather_icon': weather_icon
        }
