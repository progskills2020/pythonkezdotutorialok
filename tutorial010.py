#objektum orientált programozás alapok

class Kutya:
    def __init__(self, nev, kor):
        self.nev = nev
        self.kor = kor
        

    def ugat(self):
        print("vau vau")
    
    def bemutato(self):
        print("A kutya neve %s és kora %d év" % (self.nev, self.kor))

"""
kutya1 = Kutya("Johni", 3)
kutya1.ugat()
kutya2 = Kutya("János", 4)
kutya2.ugat()
kutya1.bemutato()
kutya2.bemutato()
"""

class Patkányfogó(Kutya):
    def __init__(self, nev, kor, gyorsasag):
        super().__init__(nev, kor)
        self.gyorsasag = gyorsasag

pf1 = Patkányfogó("Jumbo", 3, 10)

print(pf1.gyorsasag)




