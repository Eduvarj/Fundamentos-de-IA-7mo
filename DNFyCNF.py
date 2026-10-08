from TablaVerdad import bloquear, variables, tabla

def generarDNF(variables, tabla):
    cluaulas = []
    for valores, resultado in tabla:
        if resultado:
            literales = []
            for var, val in zip(variables, valores):
                literales.append(var if val else f"-{var}")
            cluaulas.append("("+ "∧ ".join(literales)+ ")")
    return "∧".join(cluaulas)

def generarCNF(variables, tabla):
    cluaulas = []
    for valores, resultado in tabla:
        if resultado:
            literales = []
            for var, val in zip(variables, valores):
                literales.append(f"-{var}" if val else var )
            cluaulas.append("("+ "V ".join(literales)+ ")")
    return "∧".join(cluaulas)

print("\n Forma nomral disyuntiva (DNF)")
print(generarDNF(variables, tabla))

print("\n Forma nomral conjuntiva (CNF)")
print(generarCNF(variables, tabla))
print("\n")