
def main():
    edad = int(input("Ingresa tu edad: "))
    #Aquí empieza tu programa...

    if (edad >= 18):
        id = str(input("¿Tienes identificación oficial? (s/n): "))
        if id == "s":
            print("Trámite de licencia concedido")
        else:
            print("No cumples requisitos")
    else:
        print("Respuesta incorrecta")

    


if __name__ == '__main__':
    main()
