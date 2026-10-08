import itertools
#Borrar de pantalla
import subprocess
subprocess.run('cls', shell = True)

def bloquear (A, B, D):
    return (A and B) or (not A and D)

variables = ["A", "B", "D"]

tabla = []

print("Tabla de Verdad A, B y D")

print("A".ljust(6), "B".ljust(6), "D".ljust(6), "A and B")
for A, B, D in itertools.product([True, False], repeat=3):
    resultado = bloquear(A, B, D)
    tabla.append(((A, B, D), resultado))
    print(str(A).ljust(7)+
          str(B).ljust(7)+
          str(D).ljust(7)+
          str(resultado))