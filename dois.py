def quantidade_a(palavra):
    palavra = palavra.lower()
    quantidade = 0

    for letra in palavra:
        if letra == "a":
            quantidade += 1

    if quantidade > 0:
        print("Nessa string tem 'a'.")
        print(quantidade)
    else:
        print("Nessa string não tem 'a'.")


quantidade_a("ADSFASQWDSaaaaA")