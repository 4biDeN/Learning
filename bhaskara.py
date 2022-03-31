import math
a = int(input("Digite o valor de a:"))
b = int(input("Digite o valor de b:"))
c = int(input("Digite o valor de c:"))

delta = b ** 2 - 4*a*c

if delta < 0 :
	print("esta equação não possui raízes reais")
else:
	if delta == 0:
		x = (- b + math.sqrt(delta)) / (2 * a)
		print("a raiz desta equação é", x)
	else:
		if delta > 0:
			x = (- b + math.sqrt(delta)) / (2 * a)
			y = (- b - math.sqrt(delta)) / (2 * a)
			print("as raízes da equação são", y, "e", x)