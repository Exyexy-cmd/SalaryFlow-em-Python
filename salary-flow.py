#inputs
try:
    ganho_hora = float(input("Digite quanto você ganha por hora (Digite . em vez de ,): "))
    hora_por_mes = int(input("Digite quantas horas trabalhou por mes: "))
    
except ValueError:
    print("Digite apenas o solicitado!")
    exit()
    
else:
    print("Tudo certo!\n")

#Variaveis globais
salario_bruto = ganho_hora * hora_por_mes
faixa_salarial = "".upper()
acumulo_salarial = 0
valor_a_ser_investido = 0
valor_reajuste = 0

#Descontos
d_ir = salario_bruto * 11 /100
d_inss = salario_bruto * 8 /100
d_sindicato = salario_bruto * 5 /100

#Salario real
salario_liquido = salario_bruto - d_inss - d_sindicato - d_ir
print(f"Seu salario de: {salario_bruto:.2f}, passou a ser: {salario_liquido:.2f} após os descontos!")

#aplicações de descontos
def reajuste20(valor):
    novosalario = valor + (valor*20 / 100)
    return novosalario

def reajuste15(valor):
    novosalario = valor + (valor*15 / 100)
    return novosalario

def reajuste10(valor):
    novosalario = valor + (valor*10 / 100)
    return novosalario

def reajuste05(valor):
    novosalario = valor + (valor*5 / 100)
    return novosalario

print("")

#Reajustes salariais
reajuste1 = reajuste20(salario_liquido)
reajuste2 = reajuste15(salario_liquido)
reajuste3 = reajuste10(salario_liquido)
reajuste4 = reajuste05(salario_liquido)

#Função para calcular apenas o valor do reajuste(gambiarra)
def valor_ajuste(rea, sal_liquido):
    novo_valor =  rea - sal_liquido
    return novo_valor

#Aplicação de descontos
print("Adicionando valor do reajuste salarial!\n")
if salario_liquido <= 1800.00:
    valor_reajuste = valor_ajuste(reajuste1, salario_liquido)
    print(f"Seu salario anterior era de: {salario_liquido:.2f}, aplicamos o valor de 20% que é: {valor_reajuste:.2f}, e que somando ao liquido fica: {reajuste1:.2f}\n")

elif 1800.00 < salario_liquido <= 2700.00:
    valor_reajuste = valor_ajuste(reajuste2, salario_liquido)
    print(f"Seu salario anterior era de: {salario_liquido:.2f}, aplicamos o valor de 15% que é: {valor_reajuste:.2f}, e que somando ao liquido fica: {reajuste2:.2f}\n")

elif 2700.00 < salario_liquido <= 5500.00:
    valor_reajuste = valor_ajuste(reajuste3, salario_liquido)
    print(f"Seu salario anterior era de: {salario_liquido:.2f}, aplicamos o valor de 10% que é: {valor_reajuste:.2f}, e que somando ao liquido fica: {reajuste3:.2f}\n")

else:
    valor_reajuste = valor_ajuste(reajuste4, salario_liquido)
    print(f"Seu salario anterior era de: {salario_liquido:.2f}, aplicamos o valor de 5% que é: {valor_reajuste:.2f}, e que somando ao fica: {reajuste4:.2f}\n")


#definindo faixa salarial
if salario_liquido <= 2000.00:
    print(f"Salário na faixa A — isento de investimentos obrigatórios.\n")
    faixa_salarial = "A"
elif 2000.00 < salario_liquido <= 5000.00:
    print(f"Salário na faixa B — recomenda-se investir 10% do líquido.\n")
    faixa_salarial = "B"
else:
    print(f"Salário na faixa C — recomenda-se investir 20% do líquido.\n")
    faixa_salarial = "C"

#Calculando valor de investimento
if faixa_salarial == "B":
    valor_investido = salario_liquido * 10 /100
    print(f"Seu valor sugerido para investimento é de: {valor_investido:.2f}\n")
elif faixa_salarial == "C":
    valor_investido = salario_liquido * 20 /100
    print(f"Seu valor sugerido para investimento é de: {valor_investido:.2f}\n")
else:
    print("Não precisa investir esse mês!\n")

#Calculando acumulo do salario liquido total
print("Calculando acumulo sob valor salarial total:\n")
for i in range(13):
    print(f"Mês {i}: Acumuado R$: {acumulo_salarial:.2f}")
    acumulo_salarial = acumulo_salarial + salario_liquido

print("")

#Calculando investimento acumulado
if faixa_salarial =="B" or faixa_salarial =="C":
    print("Calculando acumulo sob valor investido:\n")
    for a in range(13):
        print(f"Mês {a}: Acumulado R$: {valor_a_ser_investido:.2f}")
        valor_a_ser_investido = valor_a_ser_investido + valor_investido
else:
    print("Finalizando contas.")

