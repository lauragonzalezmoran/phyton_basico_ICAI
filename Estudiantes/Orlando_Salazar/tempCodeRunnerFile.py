GradosC = input("Digite los grados centigrados que desea convertir a fahrenheit: ")

GradosF = (float(GradosC) * 1.8) + 32

Resp_redondeada = str(round(GradosF, 2))

print(f"Los grados fahrenheit son: {Resp_redondeada}")