
#Programa Area del triagulo
Base = input("Digite la medida de la base del triagulo: ")

Altura = input("Digite la medida de la altura del triagulo: ")

Area = (int(Base) * int(Altura)) / 2 #Calcula area del triagulo en base a las medidas introducidas por el usuario

print(f"El area del triangulo es: {int(Area)}")


#Programa conversion Dolares a Colones
TipoCambio = 500

print(f"El tipo de cambio actual es de ¢{TipoCambio} por cada $ Dolar")

Cantidad_Dolares = input("Digite la catidad de Dolares que desea convertir: $")

Conversion = int(Cantidad_Dolares) * TipoCambio

print(f"La cantidad de colones despues de la conversion es: ¢{Conversion}")


#Programa convertir grados centigrados a fahrenheit 
GradosC = input("Digite los grados centigrados que desea convertir a fahrenheit: ")

GradosF = (float(GradosC) * 1.8) + 32

Resp_redondeada = str(round(GradosF, 2))

print(f"Los grados fahrenheit son: {Resp_redondeada}")