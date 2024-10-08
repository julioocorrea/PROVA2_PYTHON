def temperatura_media(cidades_temperaturas):
    medias = []
    for cidade, temperaturas in cidades_temperaturas:
        media = sum(temperaturas) / len(temperaturas)
        medias.append((cidade, media))
    return medias

cidades_temperaturas = [
    ("Pouso Alegre", [19, 18, 25, 22, 21, 20, 15]),
    ("Conceição do ouros", [20, 21, 22, 23, 24, 25, 26]),
    ("Cachoeira de Minas", [30, 31, 27, 28, 36, 34, 35])
]

resultado = temperatura_media(cidades_temperaturas)
print(resultado)
