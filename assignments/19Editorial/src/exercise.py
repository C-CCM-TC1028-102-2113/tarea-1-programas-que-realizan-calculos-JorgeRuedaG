def main():
    #escribe tu código abajo de esta línea
    
     import math

    p = int(input("Dame el número de palabras:"))

    pag = math.ceil(p / 475)
    cost = (pag * 60) * .9

    print ("El costo de la publicación es:", cost
           
    pass


if __name__ == '__main__':
    main()
