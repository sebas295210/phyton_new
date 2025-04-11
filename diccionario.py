# phyton_new
##este repositorio pertenece a Sebastián fiallos
meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "ESTA MUY XD":"algo muy gracioso",
            "WAWA":"niño o bebe",
            "PONTE PILAS":"piensa rapido"}
while True:
    A=input("¿Necesitas buscar algo?")
    if A=="si":
        word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
        if word in meme_dict.keys():
             print("la palabra que buscas significa:",meme_dict[word])
        else:
            print("no se encuentra la palabra")
    elif A=="no":
        break
        print("ok")
