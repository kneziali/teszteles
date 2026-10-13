import unittest

def szamologep(elso: int,masodik:int,muv:str):
    if muv == "+":
        return elso + masodik
    elif muv == "-":
        return elso - masodik
    elif muv == "*":
        return elso * masodik
    elif muv == "/":
        if masodik == 0:
            print("enye nullaval nem osztunk!")
        else:
            return elso / masodik
    else:
        print("Hibas muveleti jel!")



class SeggVizsgalo(unittest.TestCase):
    def test_negativ_osszeadas(self):
        self.assertGreater(szamologep(1,1,"+"), 0)
    def test_egyenloseg_szorzas(self):
        self.assertEqual(szamologep(10,10,"*"), 100)
    def test_nulla_kivonas(self):
        self.assertLess(szamologep(-1,-5,"+"), 0)
    def test_pozitiv_szorzas(self):
        self.assertGreater(szamologep(1,1,"*"), 0)
    def test_pozitiv_kivonas(self):
        self.assertLess(szamologep(1,100,"-"), 0)
    def test_negativ_kivonas(self):
        self.assertGreater(szamologep(100,1,"-"), 0)    
    def test_oszt(self):
        self.assertEqual(szamologep(1,1,"/"), 0)    
    def test_oszt(self):
        self.assertGreater(szamologep(100,1,"/"), 0)    
    def test_oszt_nullaval(self):
        self.assertEqual(szamologep(10,0,"/"), "enye nullaval nem osztunk!")    
    def test_muvelet(self):
        self.assertEqual(szamologep(10,0,"x"), "Hibas muveleti jel!")    
    
unittest.main()