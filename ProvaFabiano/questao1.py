def VerificarPolindromo(palavra):
    palavraInvertida = palavra[::-1]
    
    if palavraInvertida == palavra:
        polindromo = "Sim"
    else :
        polindromo = "Não"
    
    return "Palavra: " + palavra + " / Palavra Invertida: " + palavraInvertida + " / É polindromo: " + polindromo


palavra = input("Digite alguma entrada:")

print(VerificarPolindromo(palavra))