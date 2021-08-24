def main():
    #escribe tu código abajo de esta línea
    import math

    num = int(input("Dame un número:"))

    flag = 0

    if 10000 > num > 1000:

        for i in range(4):
            
            if num % 2 == 0:
                flag = flag +1
                num = math.trunc(num / 10)
                
            elif num % 2 == 1:
                flag = flag 
                num = math.trunc(num / 10)
                
        print(flag)

    else:
        
        print("invalid number")
        
    pass


if __name__ == '__main__':
    main()
