
qpizza = int(input("informe a quantidade de pizzas:"))
Ppizza = eval(input("informe o preço da pizza no cardapio:"))
custo_sem_imp = qpizza * Ppizza
Vimp = (8/100) * custo_sem_imp
total = custo_sem_imp + Vimp

saber_custo_sem_imp = str(input("deseja saber o valor da conta sem o imposto?"))
if (saber_custo_sem_imp == "sim"):
    print (custo_sem_imp)
else:
    print("ok.")
saber_val_do_imp = str(input("deseja saber o valor do imposto?"))
if (saber_val_do_imp == "sim"):
    print (Vimp)
else:
    print ("ok.")

print("o total de sua conta é", total)
print("obrigado pela preferência!")
print ("volte sempre! :)")
