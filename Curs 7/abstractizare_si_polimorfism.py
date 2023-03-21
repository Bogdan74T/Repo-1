"""
Abstractizarea este un proces prin care putem sa ascudem o anumita functionalitate specifica fata de utilizator si de asemenea
de a putea forta un anumit comportament in clasele copil
Utilizatorul stie ce face functionlitatea, dar nu si cum.

Clasa parinte este o clasa abstractam deci nu putem crea obiecte din ea, ci doar o folosim ca un template pentru clasele copii


In abstractizare exista doua concepte:
- Interfata =  contine doar metode abstracte
- Clasa abstracta = contine atat metode abstracte cat si metode proprii, cu logica proprie

Clasa abstracta trebuie sa mosteneasca clasa ABC (Abstract Class Method)
Fiecare metoda a clasei abstracte trebuie sa arunce exceptia NotImplementedError sau pass
Clasa abstracta NU are constructor pentru ca nu cream obiecte din ea

O metoda abstracta e o metoda care nu are corp (fara logica)

"""
"""
Polimorfism  = poli (mai multe) morfis(form/forme) => ceva ce poate avea mai multe forme
In cazul nostru, In OOP, o metoda poate sa aibe acelasi nume in clase diferite dar implementari/logica diferita in interior
EX: Metodele de mai jos nr_roti si nr_locuri din clasele diferite
"""

from abc import ABC, abstractmethod

# punem (ABC) pentru a-i zice lui Python ca este o clasa abstracta
class Vehicule(ABC):

    @abstractmethod             # am folosit un decorator sa arcam aceasta metoda ca abstracta
    def nr_roti(self):
        raise NotImplementedError

    @abstractmethod
    def nr_locuri(self):
        pass                # in general metodele abstracte nu trebuie sa aibe logica implementat
                            # si pentru a nu avea errori, avem 2 optiuni:
                            # scriem pass
                            # raise NotImplementedError - ridicam/aruncam exceptie

    @classmethod                  # am folosit un decorator ca sa marcam metoda ca fiind una de clasa, cu logica proprie
    def metoda_logica_proprie(self):
        print(f"Aici este o metoda cu logica propie, nu trebuie sa fiu implementata in clasele copil")


class Masina(Vehicule):

    def __init__(self,culoare):
        self.culoare = culoare

    def nr_roti(self):
        return 4

    def nr_locuri(self):
        return 5

class Bicicleta(Vehicule):
    def __init__(self,roti_ajutatoare = False):
        self.roti_ajutatoare = roti_ajutatoare

    def nr_roti(self):
        if self.roti_ajutatoare == True:
            return 4
        else:
            return 2

    def nr_locuri(self):
        return 1

# vehicul = Vehicule() # nu putem crea obiecte din clasele abstracte
masina_gri = Masina("gri")
# masina_gri.metoda_logica_proprie()
# print(masina_gri.nr_roti())
# print(masina_gri.nr_locuri())

bicicleta = Bicicleta(True)
print(bicicleta.nr_roti())

bicicleta2 = Bicicleta()
print(bicicleta2.nr_roti())