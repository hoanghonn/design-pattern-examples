class Singleton():
    _instance = None

    def __init__(self):
        raise Exception('Private construction')

    @staticmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
        return cls._instance


if __name__ == "__main__":
    print(Singleton.get_instance(Singleton))
