from Infrastructure.Workers.PreprocessingWorker import *


def main():
    repository = MongoRepository()
    collection = repository.get_all()
    start_queue(collection=collection)

main()
