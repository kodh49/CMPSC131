a="1#25544U#98067A #  08264.51782528 #-.00002182 # 00000-0 #-11606-4 #0 # 2927"

lista = a.split("*")
print(lista)
for item in lista:
    print(item.strip(), end="|")
