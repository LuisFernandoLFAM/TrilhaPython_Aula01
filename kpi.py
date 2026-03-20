## Cálculo de Bônus com Entrada do Usuário

#Começar solicitando ao usuário que insira seu nome.
nome_usuario = input("Digite seu nome.")

#Em seguida, o programa deve pedir ao usuário para inserir o valor do seu salário. Considere que este valor pode ser um número decimal.
salario = float(input("Favor informar seu salário."))

#Depois, o programa deve solicitar a porcentagem do bônus recebido pelo usuário, que também pode ser um número decimal.
per_bonus = float(input("Favor também informar o percentual do seu bônus de forma decimal."))

#O cálculo do KPI do bônus de 2026 é de 1000 + salario * bônus.
valor_bonus = (salario * per_bonus) + 1000


#Finalmente, o programa deve imprimir uma mensagem no seguinte formato: "Olá [nome], o seu valor bônus foi de 5000".
print("Olá {}, informo que seus bönus será de {}".format(nome_usuario,valor_bonus))



