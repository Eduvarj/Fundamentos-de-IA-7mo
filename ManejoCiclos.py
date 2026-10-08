#Borrar de pantalla
import subprocess
import itertools
subprocess.run('cls', shell = True)

for numero in [1, 2, 3]:
    print(numero)
#for a in [True, False]:
#    print(a)

print(" ")

for p in [True, False]:
    for q in [True, False]:
        resultado = p and q
        print(resultado)

for a in [True, False]:
    for b in [True, False]:
        print(a,b, a and b)

for conjuncion in itertools.product([True, False], repeat=2):
    print(conjuncion)

print("Tabla de verdad Conjunción")
print("A".ljust(6), "B".ljust(6), "A and B")
for a,b in itertool.product