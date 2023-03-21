
class Angajat:


    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descrie(self):
        print (f'In firma lucreaza angjatul {self.nume} {self.prenume} cu salariul de {self.salariu} lei')

    def nume_complet(self):
        print(f'Numele complet al angajatului este {self.nume} {self.prenume}')

    def salariu_lunar(self):
        print(f'Salariul lunar al angajatului este de {self.salariu} lei')

    def salariu_anual(self):
        salariu_anual = self.salariu * 12
        print(f'Angajatul are un salariu anual de {salariu_anual} lei')

    def marire_salariu(self):
        marire = 500
        procent = (sum({self.salariu}, marire)) / 100
        print(f'Marirea este de {procent},%')



george = Angajat('George', 'Marinescu', 3500)
george.descrie()
george.nume_complet()
george.salariu_lunar()
george.salariu_anual()
george.marire_salariu()

