import math
x1 = int(input("Digite um número da primeira coordenada:"))
y1 = int(input("Digite outro número da primeira coordenada:"))
x2 = int(input("Digite um número da segunda coordenada:"))
y2 = int(input("Digite outro número da segunda coordenada:"))

d = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
if d >= 10:
	print("longe")
else:
	print("perto")