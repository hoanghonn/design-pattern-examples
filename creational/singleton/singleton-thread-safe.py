from io import StringIO
import threading


class Singleton():
    _instance = None

    def __init__(self):
        raise Exception('Private construction')

    @staticmethod
    def get_instance(cls, self):
        thread_lock = threading.Lock()
        thread_lock.acquire()
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
        thread_lock.release()

        return cls._instance


if __name__ == "__main__":
    print(Singleton.get_instance(Singleton))
