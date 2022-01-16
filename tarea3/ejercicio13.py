#Escribir un programa que muestre la sumatoria de todos los múltiplos de 3 encontrados entre el 0 y el 100.

total=0
for i in range(101):
    if total % 3 == 0:
        total1=total+i
print("Sumatoria de los múltiplos de 3:", total1)
