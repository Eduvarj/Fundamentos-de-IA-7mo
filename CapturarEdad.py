def MayorEdad(edad):
    return edad >= 18

def main():
    print("Programa para identificar si una persona es Mayor de Edad")
    edad = int (input("Ingrese su edad: "))
    resultado = MayorEdad(edad)
    
    print(f"\n Edad ingresada: {edad} años")
    print(f"¿Es mayor de edad? {' Si ' if resultado else ' No '}")

if __name__ == "__main__":
    main()