"""
O functie este o modalitate prin care putem sa economisim cod.
O functie putem sa o definim o singura data si apoi sa facem ceea ce se numeste apelare a functiei
Apelarea functiei inseamna trimiterea sistemului catre adresa de memorie care poarta
    numele functiei si la care este stocat codul pe care vrem sa il executam
Definirea unei functii se poate face pe baza keyword-ului def
O functie POATE sa aiba parametri, dar nu este obligatoriu sa aiba
Chiar daca functia NU are parametri, parantezele de dupa numele functiei sunt
    obligatorii atat la definire cat si la apelare
Un parametru reprezinta o informatie de care functia are nevoie din exterior
    pentru a putea executa toate instructiunile
Putem alege sa parametrizam o functie atunci cand vrem ca functia noastra
    sa poata sa fie rulata pentru o plaja mai mare de valori
    ex: suma intre doua numere, putem avea alte doua numere la fiecare rulare
O functie POATE sa aiba optiune de return, dar nu este obligatoriu sa aiba
Vom alege sa punem optiune de return pe functie atunci cand vrem sa salvam rezultatul
    acelei functii intr-o variabila sau sa trimitem acel rezultat catre un sistem extern
"""
from utils.utils import print_hi, say_hi_name_and_age
# definirea functiei (exemplu fara parametrii si fara return)
def say_hello():
    print("Hello!")

# apelarea functiei - va executa codul din interior-ul functiei
say_hello()
say_hello()
say_hello   # -> daca nu punem parantezele nu se va executa corpul functiei, pentru ca nu este vazuta ca o functie

# !!! Daca o functie nu este apelata, codul din interiorul ei nu va fi executat
# de aceea se spune ca functiile ruleaza independent, sunt niste programe in miniatura


"""
def - keyword ul care anunta inceputul definirii unei functii
say_hi - numele functiei, care este dat de catre user si care poate sa fie orice  (free text)
            in general, numele functiei trebuie sa fie sugestiv pentru actiunea pe care o face
() - reprezentant al zonei in care PUTEM sa specificam parametri. In cazul functiei say_hi
            nu avem parametri, motiv pentru care parantezele sunt goale
: - reprezentant al inceputului corpului functiei, adica locul in care vom incepe sa descriem
            actiunea pe care trebuie sa o faca functia
Corpul unei functii va fi definit la fel ca la structurile alternative (if) si repetitive  (while, for)
            prin intermediul indentarii (adica spatiul lasat liber de la marginea fisierul python
            pana la inceputul liniei de cod)
"""

print("----------")
x = say_hello()           # aici se va executa functia say_hi (adica se printeaza Hi) chiar daca se va "salva" in variabila x
                       # defapt pentru ca functia nu are return, x va lua valoarea None
print(f"x este {x}")
print(f"x este {say_hello()}")


print("----------------------------")


# say_hi_name()   # daca functia a fost definita cu parametru (si nu are o valoare default) iar noi o apelam fara
                  # atunci va da eroare

# functiile apelate aici sunt definite intr-un alt fisier
# vezi importul de la inceputul acestui fisier
print_hi("Iulia")
print_hi("Andrei")
say_hi_name_and_age("Mario", 33)

# putem sa apelam functia si doar cu un singur parametru, vezi cum a fost definita in helper > utile
say_hi_name_and_age("Aurel")
say_hi_name_and_age([56, "test"])

"""
definim functia = parametrii
apelam functia = argumente
"""

print("----------------")
lista_nume = ["Iulia", "Andrei", "Ion", " Anastasia", "Gabriel", "Matei"]
for nume in lista_nume:
    print_hi(nume)

print("---------------")
# am definit functia
# def is_even():
#     number = int(input("introduceti nr: "))
#     if number % 2 == 0:
#         return True
#     else:
#         return False
#
# # apelez functia
# x = is_even()
# print(x)



print("---------")
# Exercitiu: Vrem sa calculam suma tututor numerelor pare dintr-un anumit interval
# functia primeste ca si parametru limtia superioara din intervalul nostru(by default icnepe de la zero)
def suma_numere_pare(limita_superioara):
    suma = 0
    for numar in range(limita_superioara + 1):
        if numar % 2 == 0:
            suma += numar

    return suma

# ATENTIE !!! - variabila 'suma' este diferita de variabila din interiorul functiei noastre
suma = suma_numere_pare(10)
print(suma)


"""
Exercitiu:
Scrieti o functie care primeste ca parametru un string si calculeaza numarul de litere mari si litere mici din el si printeaza asta
"""

print("-------------------------")
def calculator_de_litere(text):
    count = {
        "upper_case": 0,
        "lower_case": 0
    }
    for litera in text:
        if litera.isupper():
            count["upper_case"] += 1
        elif litera.islower():
            count["lower_case"] += 1

    print(f"Textul a fost: {text}")
    print(f"Numarul de litere mici este {count['lower_case']}")
    print(f"Numarul de litere mari este {count['upper_case']}")


txt_tastatura = input("Introduceti un text: ")
calculator_de_litere(txt_tastatura)



# cum putem sa importam toate functiile dintr-un fisier
# from helper.utile import say_hi_name, say_hi_name_and_age
from utils.utils import *   # * inseamna ca importam tot

print("Andrei")
say_hi_name_and_age("teodor", 34)


# 1. cum sa denumim variabile si functii (nu trebuie sa folosim denumiri rezervate)

# ne subliniaza cu rosu si nu ne lasa, va da eroare
# def = 5

# pentru denumirile de functii, cel mai bine este sa denumim o functie in
# asa fel incat sa se deduca din denumire ce face acea functie

# def is_even
# def calculate_sum

# nu e ok asa, pentru ca nu imi pot da seama ce face functia respectiva
# def void()

# recomandat ar fi si pentru variabile sa le denumim tot la fel, cat mai descriptiv
a = 0       # nu putem sa ne dam seama usor pentru ce este variabila
count = 0   # ne dam seama pentru ce este aceasta variabila


# 2. cum folosim *var intr-o functie si ce face
# Exercitiu: Vrem sa calculam suma mai multor numere date

# variabila globala
var_globala = 89
print(f"Variabila globala poate fi accesata in fisierul principal {var_globala}")

suma = 0

def calculeaza_suma(*numere):
    print(f"Variabila globala poate fi accesata si in functie {var_globala}")
    print(numere)  # le pune pe toate intr-un tuple

    # pentru a schimba valoarea unei variabile globale definite inafara functiei
    # trebuie sa mentionam ca este globala in functie
    global suma

    for numar in numere:
        suma = suma + numar
    # in momentul in care returnam mai multe valori, ele defapt sunt returnate intr-un tuple
    return suma, 8, 9


x = calculeaza_suma(5)
print(x)
print(calculeaza_suma(5))
print(calculeaza_suma(5, 10, 15))

# 3. variabilele care sunt definite intr-o functie nu pot fi accesate inafara ei

#print(suma)

# 4. variabilele care sunt definite in fisierul principal, inafara functiilor
# sunt variabile globale

# Definirea unei functii cu parametru
def print_hi(nume):
    print(f"hi {nume}")

# age are ca si valoare default 15, adica daca apela functia
# fara a seta valoarea lui age, aceasta va fi by default 15
def say_hi_name_and_age(nume, age=15):
    print(f"Hi! My name is {nume}, I am {age}")


    ###==--------------------------- CURS VALI Live -----------------------------------------------------------####

from utils.utils import say_hi_name_and_age, print_hi
# from utils.utils import * - importa tot functia din fisierul say_hi_name_and_age, print_hi

# definirea functiei (fara parametri si fara return)
def say_hi():
    print('Hi')
    print('Salutari din functia say_hi()')
    print('Inca un hi')

# Apelarea functiei de mai sus - ATENTIE !!!! Daca functia nu este apelata, aceasta nu se va executa
say_hi()

# Definirea unei functii cu parametru
def print_hi(nume):
    print(f'Hi {nume}')

#Apelarea functiei cu parametru (1 parametru, din fisierul utils.py care se afla in directorul utils - vezi import)
print_hi('Vali')
print_hi('Fanica')

#say_hi_name_and_age este o functie care se afla in utils.py
say_hi_name_and_age('Vali', 24)


'''
def - keyword ul care anunta inceputul definirii unei functii
say_hi - numele functiei, care este dat de catre user si care poate sa fie orice  (free text)
      ATENTIE: in general, numele functiei trebuie sa fie sugestiv pentru actiunea pe care o face
() - reprezentant al zonei in care PUTEM sa specificam parametri. In cazul functiei say_hi
            nu avem parametri, motiv pentru care parantezele sunt goale.
: - reprezinta inceputul functiei (ca si la if, for, while)
Corpul functiei (ATENTIE : IDENTAT, ca la if, for, while)
'''

'''
definim functia - parametrii(ex: say_hi_name_and_age(nume, age)) unde (nume, age) sunt parametrii
apelam functia - argumente (ex: say_hi_name_and_age('Fanica', 30) unde ('Fanica' si 30) sunt parametrii
'''

#in acest caz, parametru age va fi 15
say_hi_name_and_age('Tudor')
#in acest caz, parametru age va fi 56
say_hi_name_and_age('Tudor', 56)

#Atentie : daca parametru din functia noastra nu are o valoare default (vezi age din say_hi_name_and_age,
# suntem obligati sa o initializam cand apelam functia
# print_hi() = # arunca o eroareTypeError: print_hi() missing 1 required positional argument: 'nume'

valoare_returnata = say_hi_name_and_age('Tudor', 45)
print(valoare_returnata)

def numar_par(numar):
    if numar%2 == 0:
        return f'Numarul {numar} este par'
    else:
        return f'Numarul {numar} este impar'

valoare = numar_par(4)
print(valoare)

# Exercitiu: Vrem sa calculam suma tututor numerelor pare dintr-un anumit interval
# functia primeste ca si parametru limtia superioara din intervalul nostru(by default icnepe de la zero)
def suma_numere_pare(limita_superioara):
    suma = 0
    for numar in range(limita_superioara + 1):
        if numar % 2 == 0:
            suma += numar

    return suma

# ATENTIE !!! - variabila 'suma' este diferita de variabila din interiorul functiei noastre
suma = suma_numere_pare(10)
print(suma)

# Folosind suma calculata mai sus, verifica daca este mai mare decat 50 folosind o alta functie.
def verificare_suma(suma):
    if suma > 50:
        print('Suma este mai mare decat 50')
    else:
        print('Suma este mai mica decat 50')

verificare_suma(suma)

def variabila_in_functie():
    nume = 'Andrei'
    print(nume)
# print(nume) -> # eroare, nu vede variabila nume din interiorul functiei variabila_in_functie
variabila_in_functie()

#exercitiu
def exemplu_multiple_parameters(nume=None, prenume=None, varsta=0, cnp=0, sex=None):
    print(nume, prenume, varsta, cnp, sex)
    return nume, prenume, varsta, cnp, sex

nume, prenume, varsta, cnp, sex = exemplu_multiple_parameters(None, "Vasile", 0, '0234523')
exemplu_multiple_parameters(cnp='0234523', prenume='Vasile')