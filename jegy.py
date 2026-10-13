import unittest

def gyakjegy(pont: int):
    if pont >=0 and pont < 41:
        print("Elégtelen (1)")
        ertek = 1

    elif pont >=41 and pont < 55:
        print("Elégséges (2)")
        ertek = 2

    elif pont >=55 and pont < 70:
        print("Közepes (3)")
        ertek = 3

    elif pont >=71 and pont < 85:
        print("Jó (4)")
        ertek = 4

    elif pont >=86 and pont < 101:
        print("Jeles (5)")
        ertek = 5

    else:
        print("Nemjo ocsi")



class SeggVizsgalo(unittest.TestCase):
    def test_egy(self):
        self.assertEqual(gyakjegy(40), 1)

unittest.main()