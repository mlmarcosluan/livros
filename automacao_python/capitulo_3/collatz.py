# ================================================
#        Importar pacotes
# ================================================
import time

# ================================================
#        Função collatz
# ================================================
def colattz():

    numero_inteiro = entrada() # Chama a função de input

    while numero_inteiro != 1:

        # Confere se é par ou impar
        paridade = impar_par(numero_inteiro)

        if paridade == "Par": # O numero é par
            print(f"Dividindo por 2 temos: {numero_inteiro}, / 2 = {numero_inteiro / 2}")
            numero_inteiro = numero_inteiro / 2
            time.sleep(0.5)
            
        
        else:
            print(f"Multiplicando por 3 e somando 1, {numero_inteiro} * 3 + 1 = {(numero_inteiro * 3) + 1}")
            numero_inteiro = (numero_inteiro * 3) + 1
            time.sleep(0.5)
            
    # Apenas pra conferir
    if numero_inteiro == 1:
        print("Chegamos no 1")

    else:
        print("Ocorreu um problema, vamos começar de novo...")

        # Inicio a função novamente
        colattz()
    return

# ================================================
# Função de input
# ================================================
def entrada():

    while True:

        try:
            numero_inteiro = int(input("Digite um número inteiro: "))
        except ValueError:
            print("Por favor, digite um número inteiro.")

        # Se o numero_interiro do input for int ele para a função, se não continua
        if type(numero_inteiro) == int:
            break


    return numero_inteiro

# ================================================
#        Função impar ou par
# ================================================
def impar_par(numero):
    if numero % 2 == 0: # Se for verdadeiro o numero é par
        numero = "Par"
    else: # O número é impar
        numero = "Impar"

    return numero
# ================================================
#        Função principal
# ================================================

def main():

    colattz()
    
    return True

main()