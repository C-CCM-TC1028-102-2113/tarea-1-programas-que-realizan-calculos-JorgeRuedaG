def main():
    #escribe tu código abajo de esta línea

    n = int(1000)
    u = int(350)

    nc = int(input("Dame la cantidad de juegos nuevos:"))
    uc = int(input("Dame la cantidad de juegos usados:"))

    comp = nc * n + uc * u

    print("El total de la compra es:", comp)


   pass



if __name__ == '__main__':
    main()
