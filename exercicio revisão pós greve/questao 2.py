n = int(input("Digite um valor: "))

resultado = 1

for x in range(1,n+1):
  resultado = x * resultado

print ("%d! = %d" % (n, resultado))
