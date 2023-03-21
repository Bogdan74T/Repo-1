"""
Exceptiile: clase speciale Python folosite atunci cand ceva nu merge bine in cod
Acest mecanism ne ajuta sa prindem exceptiile aruncate in codul nostru, astfel incat programul sa NU se opreasca
Sintaxa:
try:
    corp
except <Clasa eroare>:
    corp
<Clasa eroare> -> optional
"""


lista_numere = [12,4,5,7,8]

print(lista_numere[10])     # -> va sari o eroare pentru ca in lista nu exista un element la pozitia 10
                            # (nici index-ul 10 nu exista)

print("AM AJUNS AICI CU EXECUTAREA CODULUI")
try:
    print(lista_numere[10])
except IndexError as error:
    print(error)

print("AM AJUNS AICI CU EXECUTAREA CODULUI")

try:
    print(lista_numere[20])
except Exception as error:
    print(error)

assert 1 == 2, f"1  nu este egal cu 2"

print("AM AJUNS AICI CU EXECUTAREA CODULUI 2")

try:
    assert 1 == 2, f"1  nu este egal cu 2"
except Exception as error:
    print(error)

print("AM AJUNS AICI CU EXECUTAREA CODULUI 2")

try:
    assert 1 == 2, f"1  nu este egal cu 2"
except AssertionError as error:
    print(error)
lista_numere = [12,4,5,7,8]
try:
    # print(lista_numere[10])
    assert 100 == "100", f"100 ca string nu este egal cu 100 ca int"
except IndexError as error:
    print(error)

try:
    # print(lista_numere[10])
    assert 100 == "100", f"100 ca string nu este egal cu 100 ca int"
except:
    print("Suntem in except")

numar_studenti = int(input("Introduceti numarul de studenti: "))
lista_studenti = []

for student in range(numar_studenti):
    if student > 5:
        print(lista_studenti)
        raise IndexError("Nr de studenti sa nu fie peste 6")
    lista_studenti.append("Vlad")
    print(student,lista_studenti[student])

print(f"Lista studenti: {lista_studenti}")