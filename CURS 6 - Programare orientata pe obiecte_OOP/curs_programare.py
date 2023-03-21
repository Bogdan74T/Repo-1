from Curs_6.persoana import Persoana

vlad = Persoana('Diaconescu', 'Vlad', 45)
vlad.prezentare()


"""
clasa CursProgramare
atribute: companie, nume,durata,nr_max_locuri, studenti
metode: inscriere_student, descriere_curs, get_locuri_disponibile
"""

class CursProgramare:

    def __init__(self,companie,nume,durata,nr_max_locuri):
        self.companie = companie
        self.nume = nume
        self.durata = durata
        self.nr_locuri = nr_max_locuri
        self.studenti = []

    def inscriere_student(self, student):
        if self.get_locuri_disponibile() > 0:
            self.studenti.append(student)
        else:
            print(f"Nu mai sunt locuri la acest curs")

    def descriere_curs(self):
        print(f"Companie:{self.companie} ---Curs: {self.nume} ----Durata: {self.durata} zile")
        print("_"*50)
        if len(self.studenti) > 0:
           for student in self.studenti:
               print(f"{student.nume} {student.prenume}, varsta {student.age}")
        else:
            print("Nu este inscris nici un student deocamdata")

    def get_locuri_disponibile(self):
        return self.nr_locuri - len(self.studenti)

curs_TA = CursProgramare("ABC","Testare Automata",24,10)
curs_TA.descriere_curs()
vlad = Persoana("Slavescu","Vlad",23)
alina = Persoana("Danescu","Alina",26)
curs_TA.inscriere_student(vlad)
curs_TA.inscriere_student(alina)
curs_TA.inscriere_student(alina)
curs_TA.inscriere_student(alina)
curs_TA.inscriere_student(alina)
curs_TA.inscriere_student(alina)
curs_TA.inscriere_student(alina)
curs_TA.inscriere_student(alina)
curs_TA.inscriere_student(alina)
curs_TA.inscriere_student(alina)

curs_TA.descriere_curs()

curs_TA.inscriere_student(alina)
curs_TA.inscriere_student(alina)