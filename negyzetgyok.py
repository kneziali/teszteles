import unittest

def negyzetgyok(szam : int):
    if szam > 0:
        return szam ** 0.5
    if szam == 0:
        return "nulla"
    return "Negatív szam nem lehet"



class SeggVizsgalo(unittest.TestCase):
    def test_negativ(self):
        self.assertEqual(negyzetgyok(-1), "Negatív szam nem lehet")
    def test_pozitiv(self):
        self.assertEqual(negyzetgyok(1), 1)
    def test_nulla(self):
        self.assertGreater(negyzetgyok(10), 0)
        
unittest.main()