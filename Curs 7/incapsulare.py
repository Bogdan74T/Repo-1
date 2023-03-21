"""
Incapsulare = posibilitatea de a PROTEJA atributele/metodele unei clase, folosind modificatorii de vizibilitate (__  si _)

- private (privat, adica atributul/metoda poate fi accesata doar din interioril clasei in care a fost definit)
        -se defineste cu dublu underscore im fata (__example)
- protected (protejatm atributul/metoda poate fi accesata din clasa in care a fost definita,
            dar si in clasele copul al acesteia, INSA NU din exterior)
        se defineste cu un singur underscore (_exemplu)

Atunci cand avem un atribut ascuns putem folosi metode speciale pentru a interactiona cu ele:
getter-> pentru a-l vedea/accesa        (ex:get_ + numele variabile)
setter -> pentru a-i schimba valoarea   (ex: set_ + numele variabile)
deleter -> pentru a-i sterge valoarea   (ex: delete_ + numele variabile)
"""
class Car:

    #atribute din clasa
    __variabila_private = "private"
    _variabila_protected = "protected"
    nume = "Vlad"
    def __init__(self,var_protected):
        self._variabila_protected = var_protected

    #getter
    def get_variabila_private(self):
        return self.__variabila_private

    #setter
    def set_variabila_private(self,var):
        self.__variabila_private = var

    #deleter
    def delete_variabila_private(self):
        self.__variabila_private = None

    def get_nume(self):
        return self.nume

    def set_nume(self,nume):
        self.nume  = nume

    def delete_nume(self):
        self.nume = None

    def __metoda_ascunsa(self):
        print("Nu ma poti apela din exterior")
