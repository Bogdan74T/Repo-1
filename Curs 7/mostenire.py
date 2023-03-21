"""
Mostenire: uneori avem clase care impartasesc atribute sau/si metode. In cazul acesta putem face o clasa parinte
si apoi clase copil care sa mosteneasca parintele si implicit toate atributele si metodel sale

Mostenirea permite sa avem o ierarhie a claselor, cu oricate nivele dorim
Clasa copil poate avea in plus oricate atrbiute si metode doreste

In cazul metodelor, atunci cand avem in clasa copil o metoda cu exact acelasi nume ca un din clasa parinte,
se zice ca avem o suprascriere asura metodei respective (sau suprascriem metoda) cu cea din clasa copil ( se va apela metoda din clasa copil)

clasa parinte o putem apela n clasele copii cu super()
"""
class Persoana:

    def __init__(self,nume,varsta,adresa):
        self.nume = nume
        self.varsta = varsta
        self.adresa = adresa

    def descriere(self):
        print("-"*50)
        print(f"Nume: {self.nume}")
        print(f"Varsta: {self.varsta}")
        print(f"Adresa: {self.adresa}")

    def anul_nasterii(self):
        return 2023 - self.varsta

class Student(Persoana):

    def __init__(self,nume,varsta,adresa,facultate,an_studiu):
        # super() reprezinta clasa parinte, in cazul nostru Persoana
        # practic aici apela constructorul clasei parinte
        super().__init__(nume,varsta,adresa)
        # Putem apela metodele din clasa parinte si in urmatorul fel
        # Persoana.__init__(self,nume,varsta,adresa)
        self.facultate = facultate
        self.an_studiu= an_studiu

    def descriere(self):
        super().descriere()
        print(f"Facultate: {self.facultate}")
        print(f"An studiu:{self.an_studiu}")

class Angajat(Persoana):

    def __init__(self,nume,varsta,adresa,companie,salariu):
        super().__init__(nume,varsta,adresa)
        self.companie = companie
        self.salariu = salariu

    def descriere(self):
        super().descriere()
        print(f"Companie: ", self.companie)
        print(f"Salariu: ",self.salariu)

    def salariu_anual(self):
        return self.salariu * 12


class Profesor(Angajat):

    def __init__(self,nume,varsta,adresa,companie,salariu,curs,nr_ore):
        super().__init__(nume,varsta,adresa,companie,salariu)
        self.curs = curs
        self.nr_ore = nr_ore

    def descriere(self):
        super().descriere()
        print("Curs:",self.curs)
        print("Nr ore:",self.nr_ore)


andrei = Persoana("Andrei",33,"Timisoara")
andrei.descriere()
# print("Anul nasterii: ", andrei.anul_nasterii())

maria = Student("Maria",23,"Bucuresti","Litere", 2)
maria.descriere()
print("Anul nasterii: ", maria.anul_nasterii())

pavel = Angajat("Pavel",39,"Oradea","Emag",6700)
pavel.descriere()
print("Salariu anual:",pavel.salariu_anual())

matei = Profesor("Matei",43,"Cluj","Luxoft",4500,"Introducere in Python",120)
matei.descriere()
print("Salariu anual: ", matei.salariu_anual()) # metoda mostenita din clasa Angajat
print("Anul nasterii: ", matei.anul_nasterii()) # metoda mostenita din clasa Persoana

try:
    print(matei.faculate)
except AttributeError as error:
    print(error)