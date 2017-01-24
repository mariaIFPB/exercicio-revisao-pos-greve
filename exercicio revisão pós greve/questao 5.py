tempo_fumando = int(input("informe a quanto tempo que fuma (em anos):"))
cigarro_fumado_por_dia = int(input("informe a quantidade de cigarros fumados por dia:"))


tempo_perdido = (((((tempo_fumando * 365)* cigarro_fumado_por_dia)*10)/60)/24)


print("você perdeu " "%.2f" % tempo_perdido," dias de vida!!")
