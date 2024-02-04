x = input("Introdueix entre 1 i 3 paraules >>>")
arr = x.split()

#rago entre 1 y 3
if len(x)>=1 and len(arr)<=3:
    y=0
    while y<len(arr):
        print("\nParaula:",arr[y],"\nCaràcters:",len(arr[y]), "\nPrimera lletra:",arr[y][0], "\nÚltima lletra:", arr[y][-1])
        y = y+1
else:
    print("Ha de tenir entre 1 i 3 paraules")