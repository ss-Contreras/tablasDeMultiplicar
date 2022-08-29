print("=============================")
contador = 0
valornum = int(input("Digite un numero maximo:"))
multiplo = int(input("digite el multiplo:"))

for i in range(valornum):
    contador = contador + 1
    print(f"{i*multiplo} es multiplo de {multiplo}\n{i} x {multiplo} = {i*multiplo}")
    print("=============================")
       

