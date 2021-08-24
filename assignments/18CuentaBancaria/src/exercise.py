def main():
    #escribe tu código abajo de esta línea
    sma = float(input("Dame el saldo del mes anterior:"))
    ing = float(input("Dame los ingresos:"))
    eg = float(input("Dame los egresos:"))
    nce = int(input("Dame el número de cheques:"))

    res = ((sma + ing - eg - (nce * 13)) * .925) 

    print("El saldo final de la cuenta es:", res) 
    
    pass

if __name__ == '__main__':
    main()
