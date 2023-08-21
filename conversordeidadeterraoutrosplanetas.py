import time
def calcular_idade_em_outro_planeta(idade_terra, periodo_orbital_outro_planeta):
    idade_outro_planeta = idade_terra / periodo_orbital_outro_planeta
    return idade_outro_planeta
periodo_orbital_mercurio = 87.97
periodo_orbital_venus = 224.7
periodo_orbital_marte = 1.88
periodo_orbital_jupiter = 11.86
periodo_orbital_saturno = 29.46
periodo_orbital_urano = 84.01
periodo_orbital_netuno = 164.79
periodo_orbital_plutao = 248.59

escolha = True
while escolha:
    print("\n")
    print("Idade da Terra para outros Planetas")
    print("""
    1. Mercúrio
    2. Vénus
    3. Marte
    4. Júpiter
    5. Saturno
    6. Úrano
    7. Neptuno
    8. Plutão   
    0. Sair
    """)
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        print("="*60)
        print("\t\t\t\tSua Idade em Mercúrio")
        print("=" * 60)
        idade_na_terra = int(input("Digite a sua idade na Terra: "))
        idade_mercurio = calcular_idade_em_outro_planeta(idade_na_terra, periodo_orbital_mercurio)
        time.sleep(2)
        print(f"\nIdade em Mercúrio: {idade_mercurio:.2f} anos terrestres")
        time.sleep(2)
    elif escolha == "2":
        print("=" * 60)
        print("\t\t\t\tSua Idade em Vénus")
        print("=" * 60)
        idade_na_terra = int(input("Digite a sua idade na Terra: "))
        idade_venus = calcular_idade_em_outro_planeta(idade_na_terra, periodo_orbital_venus)
        time.sleep(2)
        print(f"\nIdade em Vénus: {idade_venus:.2f} anos terrestres")
        time.sleep(2)
    elif escolha == "3":
        print("=" * 60)
        print("\t\t\t\tSua Idade em Marte")
        print("=" * 60)
        idade_na_terra = int(input("Digite a sua idade na Terra: "))
        idade_marte = calcular_idade_em_outro_planeta(idade_na_terra, periodo_orbital_marte)
        time.sleep(2)
        print(f"\nIdade em Marte: {idade_marte:.2f} anos terrestres")
        time.sleep(2)
    elif escolha == "4":
        print("=" * 60)
        print("\t\t\t\tSua Idade em Júpiter")
        print("=" * 60)
        idade_na_terra = int(input("Digite a sua idade na Terra: "))
        idade_jupiter = calcular_idade_em_outro_planeta(idade_na_terra, periodo_orbital_jupiter)
        time.sleep(2)
        print(f"\nIdade em Júpiter: {idade_jupiter:.2f} anos terrestres")
    elif escolha == "5":
        print("=" * 60)
        print("\t\t\t\tSua Idade em Saturno")
        print("=" * 60)
        idade_na_terra = int(input("Digite a sua idade na Terra: "))
        idade_saturno = calcular_idade_em_outro_planeta(idade_na_terra, periodo_orbital_saturno)
        time.sleep(2)
        print(f"\nIdade em Saturno: {idade_saturno:.2f} anos terrestres")
        time.sleep(2)
    elif escolha == "6":
        print("=" * 60)
        print("\t\t\t\tSua Idade em Úrano")
        print("=" * 60)
        idade_na_terra = int(input("Digite a sua idade na Terra: "))
        idade_urano = calcular_idade_em_outro_planeta(idade_na_terra, periodo_orbital_urano)
        time.sleep(2)
        print(f"\nIdade em Úrano: {idade_urano:.2f} anos terrestres")
        time.sleep(2)
    elif escolha == "7":
        print("=" * 60)
        print("\t\t\t\tSua Idade em Neptuno")
        print("=" * 60)
        idade_na_terra = int(input("Digite a sua idade na Terra: "))
        idade_neptuno = calcular_idade_em_outro_planeta(idade_na_terra, periodo_orbital_netuno)
        time.sleep(2)
        print(f"\nIdade em Neptuno: {idade_neptuno:.2f} anos terrestres")
        time.sleep(2)
    elif escolha == "8":
        print("=" * 60)
        print("\t\t\t\tSua Idade em Plutão")
        print("=" * 60)
        idade_na_terra = int(input("Digite a sua idade na Terra: "))
        idade_plutao = calcular_idade_em_outro_planeta(idade_na_terra, periodo_orbital_plutao)
        time.sleep(2)
        print(f"\nIdade em Plutão: {idade_plutao:.2f} anos terrestres")
        time.sleep(2)
    elif escolha == "0":
        time.sleep(2)
        print("\nAdeus")
        escolha = None
    else:
        print("\nEscolha inválida. Tente novamente.")