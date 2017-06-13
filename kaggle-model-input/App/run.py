from Infrastructure.Repositories.MongoRepository import MongoRepository
from Infrastructure.Workers.PreprocessingWorker import *


def main():
    repository = MongoRepository('188.226.152.151', 25025)
    collection = repository.get_all()
    start_queue(collection=collection)

main()
