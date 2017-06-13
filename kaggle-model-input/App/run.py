from Infrastructure.Repositories.MongoRepository import MongoRepository
from Infrastructure.Workers.PreprocessingWorker import *


def main():
    repository = MongoRepository('poke-mongo', 27017)
    collection = repository.get_all()
    start_queue(collection=collection)

main()
