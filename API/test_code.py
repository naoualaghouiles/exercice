import unittest

from code import Code


class TestMethods(unittest.TestCase):
    """test_method class doctstring"""

    def test_annee_valid(self):
        """length caractere doit etre 15"""
        code = Code("FRA.12.42.2019")
        assert code.annee_is_valid()

    def test_annee_not_valid(self):
        """length caractere doit etre 15"""
        code = Code("FRA.12.42.2025")
        assert not code.annee_is_valid()

    def test_modele_0_3_not_valid(self):
        """length caractere doit etre 15"""
        code = Code("FR4.12.42.2019")
        assert not code.modele_is_valid()

    def test_modele_pr_3_4_not_valid(self):
        """length caractere doit etre 15"""
        code = Code("FRA-12.42.2019")
        assert not code.modele_is_valid()

    def test_modele_pr_4_6_not_valid(self):
        """length caractere doit etre 15"""
        code = Code("FRA.1A.42.2019")
        assert not code.modele_is_valid()

    def test_modele_pr_7_9_not_valid(self):
        """length caractere doit etre 15"""
        code = Code("FRA.14.A2.2019")
        assert not code.modele_is_valid()