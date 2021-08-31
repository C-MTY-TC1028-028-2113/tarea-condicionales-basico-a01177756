
def main():
    edad = int(input("Ingresa tu edad: "))
    #Aquí empieza tu programa...
    id = str(input("Tienes identificación oifical? (s/n)"))

    if (edad >= 18 and id == "s"):
        print("Trámite de licencia concedido.")
    elif(edad < 18 or id == "n"):
            print("No cumples requisitos")
    else:
        print("Respuesta incorrecta")

    


if __name__ == '__main__':
    main()
