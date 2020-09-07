cadena = '_servidor1'
cadena2 = '3servidor'


def AFD (entrada):
    estado = 0

    for i in range(len(entrada)):
        if (estado == 0):
            if (entrada[i] == '_'):
                estado = 1
            elif(entrada[i].isalpha()):
                estado = 2
            else:
                print("Palabra incorrecta")
                return
        elif (estado == 1):
            if entrada[i] == '_':
                estado = 1
            elif(entrada[i].isalpha()):
                estado = 3
            else:
                print("Palabra incorrecta")
                return
        elif (estado == 3):
            if entrada[i].isdigit():
                estado = 4
            else:
                print("Palabra incorrecta")
                return
        elif (estado == 2):
            if entrada[i].isalpha():
                estado = 2
            elif(entrada[i].isnumeric()):
                estado = 4
            else:
                print("Palabra incorrecta")
                return
    print("Palabra correcta")

AFD(cadena)
AFD(cadena2)











