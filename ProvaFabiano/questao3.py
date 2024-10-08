def validaPrimos(numeros):
    for numero in numeros:
        if numero < 2:  
            resultado = str(numero) + " não é primo"
            print(resultado)
            continue

        is_primo = True
        for index in range(2, int(numero**0.5) + 1):  
            if numero % index == 0:
                is_primo = False
                break
        
        if is_primo:
            resultado = str(numero) + " é primo"
        else:
            resultado = str(numero) + " não é primo"
        
        print(resultado)

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
validaPrimos(numeros)
