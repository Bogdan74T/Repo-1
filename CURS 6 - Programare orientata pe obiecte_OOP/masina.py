"""
Clasa Masina
Atribute: marca,model,culoare,motor_pornit, viteza
Metode: prezentare_masina, start, stop, accelereaza, incetineste, vopseste
"""

class Masina:
    #atribute default
    marca = None
    model = None
    culoare = "alb"
    motor_pornit = False
    viteza = 0

    # constructor-> o metoda care ne obliga sa dam ca valori
    # parametrii mentionati intre paranteze ()
    # (self nu se ia in considerare) atunci cand cream obiectul
    def __init__(self, marca, model):
        # self.marca este atributuil obiectului instantiat
        # "marca" este parametrul functiei,
        # prin el transmitem valoarea catre self.marca
        self.marca = marca
        self.model = model

    def prezentare_masina(self):
        print(f"Modelul masinii este {self.model}, marca {self.marca} si are culoarea {self.culoare}")

    def start(self):
        self.motor_pornit = True

    def stop(self):
        self.viteza = 0
        self.motor_pornit = False


    def accelereaza(self, valoare_acc):
        if self.motor_pornit == True:
            self.viteza += valoare_acc
            print(f"Am accelerat cu viteza de {valoare_acc}. Si acum am {self.viteza} km/h")
        else:
            print("Nu se poate accelera cu motorul oprit. Dai start la masina si incearca din nou.")

    def incetineste(self,valoare_deacc):
        if self.motor_pornit == True and self.viteza > 0:
            if self.viteza > valoare_deacc:
                self.viteza -= valoare_deacc
            else:
                self.viteza = 0
            print(f"Viteza s-a redus la {self.viteza} km/h")
        else:
            print("Viteza este 0 sau motorul nu este pornit")

    def vopseste(self, culoare):
        self.culoare = culoare