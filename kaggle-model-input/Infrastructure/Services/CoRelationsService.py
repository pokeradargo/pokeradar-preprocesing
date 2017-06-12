
class CoRelationsService:
    @staticmethod
    def init_correlations(item):
        response = {}
        for pokemon_number in range(1, 152):
            if item.get('cooc_' + str(pokemon_number)) == "true":
                response['cooc_' + str(pokemon_number)] = 1
            else:
                response['cooc_' + str(pokemon_number)] = 0
        return response

    @staticmethod
    def increase_correlations(item, co_relations):
        if item is not None:
            for pokemon_number in range(1, 152):
                co_relations['cooc_' + str(pokemon_number)] += int(item['cooc_' + str(pokemon_number)])

        return co_relations


