"""code module doc"""

class Code:
    """code class doc"""
    def __init__(self, code):
        self.__code = code

    @property
    def code(self):
        """The code property."""
        return self.__code

    @code.setter
    def imm(self, value):
        self.__code = value

    def code_is_valid(self):
        """code is valid"""
        return self.annee_is_valid() and self.modele_is_valid()

    def annee_is_valid(self):
        """ annee is valid"""
        if self.__code[10:14].isdecimal():
            return int(self.__code[10:14]) < 2022
        else:
            return False

    def modele_is_valid(self):
        """ modele is valid"""
        if self.__code[0:3].isalpha():
            if self.__code[3:4] == ".":
                if self.__code[4:6].isdecimal():
                    if self.__code[6:7] == ".":
                        if self.__code[7:9].isdecimal():
                            if self.__code[9:10] == ".":
                                return True
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
