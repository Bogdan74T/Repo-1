from Curs_6.masina import Masina
# vlad = Persoana("Diaconescu", "Vlad", 45)
# vlad.prezentare()

audi = Masina("Audi","A6")
# audi.prezentare_masina()
audi.culoare = "negru"
audi.prezentare_masina()

audi.accelereaza(50)
audi.start()
audi.accelereaza(50)
audi.accelereaza(30)
# print(audi.viteza)
audi.stop()
# print(audi.viteza)
audi.accelereaza(10)
audi.start()
audi.accelereaza(40)
audi.incetineste(30)
audi.incetineste(40)
# audi.incetineste(40)
audi.stop()
# audi.culoare = "Verde"
audi.vopseste("Verde")
print(audi.culoare)