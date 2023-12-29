
class Movie:

    def __init__(self, title, genre, release_year, rating,ranking):
        self.__title = title
        self.__genre = genre
        self.__release_year = release_year
        self.__rating = rating
        self.__ranking = ranking

    def resetAll(self):
        self.__title = ""
        self.__genre = ""
        self.__release_year = ""
        self.__rating = ""
        self.__ranking = ""

    def get_title(self):
        return self.__title

    def get_genre(self):
        return self.__genre

    def get_release_year(self):
        return self.__release_year

    def get_rating(self):
        return self.__rating

    def get_ranking(self):
        return self.__ranking


