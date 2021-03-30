from abc import ABC, ABCMeta, abstractclassmethod


class FilmBuilder(ABC):
    @abstractclassmethod
    def generate_scripts(self):
        raise NotImplementedError

    @abstractclassmethod
    def record_scenes(self):
        raise NotImplementedError

    @abstractclassmethod
    def edit_footages(self):
        raise NotImplementedError

    @abstractclassmethod
    def get_result(self):
        print("completed")


class DocumentationFilmBuilder(FilmBuilder):
    def generate_scripts(self):
        pass

    def record_scenes(self):
        pass

    def edit_footages(self):
        pass

    def get_result(self):
        return super().get_result()


class CinematicFilmBuilder(FilmBuilder):
    def generate_scripts(self):
        pass

    def record_scenes(self):
        pass

    def edit_footages(self):
        pass

    def add_CGI(self):
        pass

    def get_result(self):
        return super().get_result()
