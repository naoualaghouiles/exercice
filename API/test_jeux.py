import unittest

from jeux import Jeux


class TestMethods(unittest.TestCase):
    """test_method class doctstring"""

    def test_genre_valid(self):
        """length caractere doit etre 15"""
        j = Jeux("Console1", "sport", 500, "description1", "code1")
        assert j.genre_is_valid()

    def test_console_not_valid(self):
        """length caractere doit etre 15"""
        j = Jeux("FakeConsole", "sport", 500, "description1", "code1")
        assert not j.console_is_valid()

    def test_console_valid(self):
        """length caractere doit etre 15"""
        j = Jeux("Console1", "sport", 500, "description1", "code1")
        assert j.console_is_valid()
