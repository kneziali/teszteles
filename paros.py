import unittest

def osszeg(a,b):
    ossz = 0
    for i in range(a,b+1):
        if i % 2 == 0:
            ossz += i
    return ossz


class SeggVizsgalo(unittest.TestCase):
    def test_negativ(self):
        self.assertGreater(osszeg(1,10), 0)
    def test_egyenloseg(self):
        self.assertEqual(osszeg(42,100), 2130)
    def test_nulla(self):
        self.assertEqual(osszeg(0,0), 0)
        
unittest.main()