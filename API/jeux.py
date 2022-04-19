"""Jeux Module
"""
from code import Code


class Jeux:
    """Jeux Module
    """
    def __init__(self, console, genre, prix, description, code):
        self.__console = console
        self.__genre = genre
        self.__prix = prix
        self.__description = description
        self.__code = code

    @property
    def console(self):
        """The console property."""
        return self.__console

    @console.setter
    def console(self, value):
        self.__console = value

    @property
    def genre(self):
        """The genre property."""
        return self.__genre

    @genre.setter
    def genre(self, value):
        self.__genre = value

    @property
    def prix(self):
        """The prix property."""
        return self.__prix

    @prix.setter
    def prix(self, value):
        self.__prix = value

    @property
    def description(self):
        """The description property."""
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value

    @property
    def code(self):
        """The code property."""
        return self.__code

    @code.setter
    def code(self, value):
        """setter
        """
        self.__code = value

    def genre_is_valid(self):
        """genre_is_valid
        """
        return (
            self.__genre == "RPG"
            or self.__genre == "sport"
            or self.__genre == "simulation"
        )

    def console_is_valid(self):
        """console_is_valid
        """
        return self.__console != "FakeConsole"

    def code_is_valid(self):
        """code_is_valid
        """
        code = Code(self.__code)
        return code.code_is_valid()

    def jeux_is_valid(self):
        """jeux_is_valid
        """
        return (
            self.genre_is_valid() and self.console_is_valid() and self.code_is_valid()
        )
