from Infrastructure.Repositories.MongoRepository import MongoRepository
from Infrastructure.Workers.PreprocessingWorker import *


def main():
    repository = MongoRepository('poke-mongo', 5432)
    collection = repository.get_all()
    start_queue(collection=collection)

main()
