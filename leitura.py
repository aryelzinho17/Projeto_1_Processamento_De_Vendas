arquivo=open("vendas_dia.txt","r")
total = 0
for linha in arquivo.readlines():
    total= total + float(linha.strip('\n'))
print(total)
arquivo.close()    