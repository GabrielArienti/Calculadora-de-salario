

# COMO CALCULAR HORA TRABALHADA.
# Primeiro se calcular quanto é o valor da hora trabalhada, de acordo ao salário mensal e horas que se trabalhou no mes.
# Logo, o valor de cada hora adicional corresponde ao valor da hora mensal + 50% da hora.
# Por fim, se soma todas as horas extra ordinárias do mes, e se obtem o valor que será adicionado ao salário final.


# Variáveis e Inputs
nome = str(input('Qual seu nome completo? :'))
profissão = str(input('Qual a sua profissão? :'))
dias_trabalhados = float(input('Quantos dias por mês você trabalha? :'))
hora_por_dia = float(input('Quantas horas você trabalha por dia? :'))
salario_base = float(input('Qual é o seu salário base?'))
horas_extras_feitas = float(input('Quantas horas extras você fez este mês? :'))

# Calcular horas trabalhadas em um mes
horas_mensais = hora_por_dia * dias_trabalhados

# Calcular valor da hora
valor_hora = float(salario_base/horas_mensais)

# Calculo da hora * 50% do valor dela mesma (ou seja, x 1,5)
adicional = float(1.5)
valor_hora_extra = valor_hora*adicional


# Somando ao valor final
horas_extras_mes = valor_hora_extra*horas_extras_feitas
salario_final = salario_base + horas_extras_mes
print(f"""
-----
Relatório completo: 

Nome: {nome}
Profissão: {profissão}
- Salário base: R${salario_base}
- Valor da sua hora: R${valor_hora}
- Valor da hora extra: R${valor_hora_extra}
- Horas extras trabalhadas: {horas_extras_feitas}

---- Remuneração final: R${salario_final}

""")
