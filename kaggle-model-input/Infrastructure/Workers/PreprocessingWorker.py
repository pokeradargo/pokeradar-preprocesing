from Infrastructure.Repositories.MongoRepository import MongoRepository
from threading import Thread
from queue import *


def worker(my_queue):
    repository = MongoRepository()
    while True:
        while not my_queue.empty():
            item = my_queue.get()
            repository.run_pre_processing(item)
            my_queue.task_done()


def start_queue(collection):
    my_queue = Queue(maxsize=0)
    # NOTE: use only one thread if calculate_co_relations is active
    for i in range(5):
        thread = Thread(target=worker, args=(my_queue,))
        thread.setDaemon(True)
        thread.start()

    for item in collection:
        my_queue.put(item)

    print("start queue")
    my_queue.join()
