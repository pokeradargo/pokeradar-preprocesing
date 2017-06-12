from Infrastructure.Services.AppearedDayOfWeekDefinitionService import AppearedDayOfWeekDefinitionService
from Infrastructure.Services.AppearedTimeOfDayDefinitionService import AppearedTimeOfDayDefinitionService


class TimePreProcessingService:
    @staticmethod
    def pre_processing_time(item):
        appeared_day_of_week = AppearedDayOfWeekDefinitionService.get_appeared_day_of_week_definition(
            item.get('appearedDayOfWeek')
        )
        appeared_time_of_day = AppearedTimeOfDayDefinitionService.get_appeared_time_of_day_definition(
            item.get('appearedTimeOfDay')
        )
        return {
            'appeared_day_of_week': appeared_day_of_week,
            'appeared_time_of_day': appeared_time_of_day
        }
