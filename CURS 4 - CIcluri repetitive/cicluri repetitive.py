"""
Structuri repetitive = blocuri de cod care se vor executa
in mod repetitiv pana cand o anumita conditie nu mai este
respectata (este falsa)

Iteratie = procesul prin care un bloc de cod este executat
in cadrul structurii repetitive
"""
# ---------------------------------------------------

##### WHILE/WHILE ELSE ######

"""
while = "cat timp" = ne permite executarea unui bloc
de cod cat timp o conditie este adevarata

- Contorul de control (exemplu 'i') al structurii repetitive trebuie 
declarat inainte de structura repetitiva (while) si modificat in
interiorul structurii repetitive(while).

- !!!Atentie!!! Daca nu modificam valoarea contorului
in interiorul structurii repetitive vom crea un loop
(ciclu) infinit.
"""

i = 0
while i <= 3:
    print(f"Valoarea lui i inainte de incrementare: {i}")
    i += 1 #<=> i = i + 0

print('done')

"""
While-ul de mai sus se intereaza astfel:
i = 0 => i <=3 ? DA => se executa codul din interiorul ciclului
i = 1 => i <=3 ? DA => se executa codul din interiorul ciclului
i = 2 => i <=3 ? DA => se executa codul din interiorul ciclului
i = 3 => i <=3 ? DA => se executa codul din interiorul ciclului
i = 4 => i <=3 ? NU => se iese din ciclu
"""

# Exemplu ciclu infinit

i = 0
while i <=3:
    print(f'INFINITY:{i})
    # nu incrementam valoarea lui i niciodata,
    # astfel conditia va ramane mereu TRUE(0 <= 3)

while TRUE:
    print('Ciclu infinit')

while 1:
    print('Ciclu infinit')

while 'Samanta':
    print('Ciclu infinit')

while None:
    print('Ciclu infinit')
print('None returneaza False')
    i = 0

i = 100
while i >= 0:
    print(f'valoarea lui i este {i}')
    i -= 1


# BREAK in while (break poate fi folosit doar intr-un 'while' sau intr-un 'for')

i = 0

while i <= 10:
    print(f"Valoarea lui i este {i}")
    if i == 5:
        break
    i += 1
print("Done")

i = 0
while i <=3:
    print(i)
    if i == -10:
        break
    i -=1
print("done")


# CONTINUE in while
i = 0
while i <=10:
    print(i)
    if i == 4:
        continue
    print(i)
    i += 1

while None:
    print("INFINITY")

"""
Folosim WHILE ELSE (Referinta la exemplul de mai sus)

WHILE = tipul structurii repetive
i<=3: = conditia care se evalueaza
else = setul de instructiuni care se va executa dupa ce se iese
din structura repetitiva (while)
"""

i = 0
while i <= 20:
    print(f"i = {i}")
    i += 1
else:
    print(f"i nu mai este mai mic sau egal cu 20, i={i}")
print("Done")

"""
Debugging = Depanare = procesul prin care gasim 
                    si rezolvam probleme in cod (bugs)
                    = punem pauza in cod ca sa vedem cum se parcurge
                    codul pas cu pas (linie cu linie)
"""

#Parcurgerea listelor cu while
lista_fructe =["mere","pere","banane","struguri"]

i = 0
while i < len(lista_fructe):
    print(f"fruct={lista_fructe[i]}")
    i += 1
print("Am iesit din while")

"""
Exercitiu:
Type a one-letter command and hit enter:
A to add a name to your list
R to remove a name from your list
S to show the names in your list
Q to quit
"""

names = []
ALLOW_COMMANDS = ['a','r','s','q']
continue_loop = True

while continue_loop: # Se va iesi din while atunci cand continue_loop = False
    command = input("Introduceti comanda ['A','R','S','Q']: ").lower()
    if command in ALLOW_COMMANDS:
        if command == 'a':
            name = input("Introduceti un nume pentru a-l adauga: ")
            names.append(name) # SAU names = names + name
        elif command == 'r':
            name = input("Introduceti un nume pentru a-l sterge: ")
            names.remove(name)
        elif command == 's':
            print(f"Lista actuala este: {names}")
        else:
            continue_loop = False
            # break
    else:
        print(f"Introduceti o comanda valida, alegeti intre ['A','R','S','Q']")


#------------------------------------------------------------------
#####   FOR/FOR ELSE    #######

"""
range -> range este o functie care definste un interval
    range(A,B,C)
    A = de unde incepem. Daca nu punem nimic atunci default 0 ex:range(4) <=> 0,1,2,3
    B = pana unde mergem. Daca nu punem atunci va fi limita superioara -1 ex:range(4) <=> 0,1,2,3
    C = pasul - optional (default 1)
"""
for i in range(3,12):
    print(i)
for i in range(3,12,2):      # iteram de la 2 la 24 din doi in doi
    print(i)
for i in range(12,2,-1):
    print(i)
for i in range(33):
    print(i)

#@ FOR EACH ##        (se foloseste in liste, dictionare sau orice alta structura de date)

for i in [3,4,6,"mere",7,True]:
    print(i)
print("-------------------")

lista_fructe = ['mere', 'pere', 'banane', 'struguri']
for fruct in lista_fructe:
    print(fruct)

# FOR simplu
lista_fructe = ['mere', 'pere', 'banane', 'struguri']

for i in range(len(lista_fructe)):  # range default porneste de la 0 pana la 4-1 = 3
    print(lista_fructe[i])

#------------------
#Calculeaza primele numere pare pana la 101
suma = 0
for i in range(0,102,2):
    suma += i
    print(suma)
print(suma)

#------ Inverseaza textul folosind for -------
text = "Ana are mere"
text_inversat = ""

for i in range(len(text)-1,-1,-1):  # echivalent cu range(11,-1,-1) deoarece len(text)=12
    text_inversat += text[i]
else:
    print("S-a terminat range-ul")
print(text_inversat)

"""
Exercitiu:
avem o lista de culori: ["roz","albastru","rosu","alb","galben"]
Parcurg lista iar cand ajung la valoarea culoarea alb dau skip 
"""
lista_culori = ["roz","albastru","rosu","alb","galben"]

for culoare in lista_culori:
    if culoare == "alb":
        continue
    print(culoare)
"""
Avem lista de mai sus. Stergem din lista toate nonculorile (Alb,Gri,Negru)
"""

lista_culori = ["roz","gri","albastru","rosu","alb","galben","negru"]
for culoare in lista_culori:
    if culoare == "alb" or culoare == "negru" or culoare == "gri":
        lista_culori.remove(culoare)
        print(f"{culoare} este nonculoare.")

print(lista_culori)

# Cum interam cheie valoare intr-un dictionar?

note_elevi={
        "Andrei":10,
        "Elena": 8,
        "Maria": 10,
}
# print(note_elevi.items())
for elev, nota in note_elevi.items():
    print(f"{elev} a luat nota {nota}")

# Cum iteram printr-un dicionar in dictionar in dictionar etc...

dict1 = {
    "HR":{
        "1":{
            "Andrei":4532,
            "Matei":2364,
            "Florin":12353
        },
        "2":{
            "Iulia":56435,
            "Georgiana":1235323,
            "Luca":1634523,
            "Andrei":653224
        }
    }
}
# print(dict1.items())

for cheie, valoare in dict1.items():
    print("----------------------------")
    print(cheie,valoare)
    print("----------------------------")
    for cheie_din_hr,valoari_din_hr in valoare.items():
        print("----------------------------")
        print(cheie_din_hr,valoari_din_hr)
        print("----------------------------")
        for chei_din_1_2,valori_din_1_2 in valoari_din_hr.items():
            print("----------------------------")
            print(chei_din_1_2,valori_din_1_2)
            print("----------------------------")


