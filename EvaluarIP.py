def bloquear(A, B, D):
    return (A and B) or (not A and D)

def bool_a_vf(valor):
    """Convierte True/False a V/F para la impresión en pantalla"""
    return "V" if valor else "F"

def main():
    print("=== ¿DEBEMOS BLOQUEAR ESTA IP? ===")
    print("Responde según lo que se observó de la IP analizada.\n")
    
    resp_A = input("¿Se detectó un ataque de fuerza bruta? (s/n): ").strip().lower()
    resp_B = input("¿El tráfico supera el ancho de banda permitido? (s/n): ").strip().lower()
    resp_D = input("¿La IP está en la lista negra? (s/n): ").strip().lower()
    
    A = resp_A == 's'
    B = resp_B == 's'
    D = resp_D == 's'
    
    parte1 = A and B
    parte2 = not A and D
    resultado_final = bloquear(A, B, D)
    
    str_A = bool_a_vf(A)
    str_B = bool_a_vf(B)
    str_D = bool_a_vf(D)
    str_no_A = bool_a_vf(not A) 
    
    print("\n--- REGLA APLICADA ---")
    print("bloquear(A, B, D) = (A ∧ B) ∨ (¬A ∧ D)")
    print(f"Valores ingresados:  A={str_A}   B={str_B}   D={str_D}")
    
    print(f"(A ∧ B)    = ({str_A} ∧ {str_B}) = {bool_a_vf(parte1)}")
    print(f"(¬A ∧ D)   = ({str_no_A} ∧ {str_D}) = {bool_a_vf(parte2)}")
    print(f"Resultado = ({bool_a_vf(parte1)}) ∨ ({bool_a_vf(parte2)}) = {bool_a_vf(resultado_final)}")
    
    print("\n--- DECISIÓN ---")
    if resultado_final:
        print("La IP debe ser BLOQUEADA.")
    else:
        print("La IP NO debe ser BLOQUEADA.")

if __name__ == "__main__":
    main()