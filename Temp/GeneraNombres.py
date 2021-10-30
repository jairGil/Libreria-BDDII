f = open('Nombres.txt', 'r', encoding='UTF8')

datos3 = set()

datos = f.readlines()

datos_temp = []

for d in datos:
    for e in d.replace("\n", "").split(" "):
        if not(e=="" or e=="\n"):
            datos_temp.append(e)

datos2 = datos_temp

for i in range(len(datos)):
    for j in range(len(datos2)):
        for k in range(len(datos2)):
            datos3.add(datos_temp[i] + "   " + datos2[j] + "    " + datos2[k])

print(len(datos3))
f.close()