from Infrastructure.Repositories.MongoRepository import MongoRepository


def main():
    repository = MongoRepository('188.226.152.151', 25025)
    repository.get_all()

main()
