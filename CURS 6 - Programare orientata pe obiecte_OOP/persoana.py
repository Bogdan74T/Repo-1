class Persoana:
    # nume = ""
    # prenume = ""
    # age = 0
    def __init__(self, nume, prenume, age):
        self.nume = nume        #self.nume != nume ( ca sa accesam field-urile clasei trebuie sa le scriem cu self. inainte.
        self.prenume = prenume
        self.age = age

    def prezentare(self):
        print(f"Salut, ma numesc {self.nume} {self.prenume}. Si am {self.age} ani")

    def get_varsta_peste_10_ani(self):
        return self.age + 10

# vali = Persoana("Chiras","Valentin",24)
# # print(vali.prenume)
# vali.prenume = "Fanica"
# # print(vali.prenume)
#
# alina = Persoana("Dobrescu","Alina",23)
# # print(alina.prenume)
# vali.prezetare()
# alina.prezetare()
# print(alina.get_varsta_peste_10_ani())