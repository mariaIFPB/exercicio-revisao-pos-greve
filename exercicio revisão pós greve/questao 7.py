def valorPagamento(valorp, diaA):
  if diaA < 1:
    valor = valorp
    print(valor)
    return valor
  else:
   valor = (valorp + (valorp * 0.03 + 0.01 * diaA))
   print(valor)
   return valor
valor = []
valorp = 0
diaA = 0
quantidade_de_p = 0
valortotal = 0

while True:
  quantidade_de_p += 1
  valorp = float(input('Qual o valor da prestacao? '))
  diaA = int(input('Quantos dias esta em atraso? '))
  if valorp == 0:
    break
  valor.append(valorPagamento(valorp, diaA))
 
quantidade_de_p -= 1
for i in range(quantidade_de_p):
  valortotal += valor[i]
  
print('Relatorio do dia, foram pagas %d prestacoes no valor: ' %quantidade_de_p, valor)
print('Valor total de prestacoes pagas: ', valortotal)
