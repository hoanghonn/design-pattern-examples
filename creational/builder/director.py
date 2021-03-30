class FilmDirector():
    def __init__(self, FilmBuilder):
        self.FilmBuilder = FilmBuilder

    def construct(self, isActionType):
        self.FilmBuilder.generate_scripts()
        self.FilmBuilder.record_scenes()
        self.FilmBuilder.edit_footages()

        if isActionType:
            self.FilmBuilder.add_CGI()
