# código de geração do gráfico 

dia =[]
venda =[]

#lendo o arquivo csv
with open(file="./gasolina.csv", mode="r", encoding="utf8") as arquivo:
   arquivo.readline()   #cabecalho
   k=0
   for k in range(10):
     info = arquivo.readline()
     dia.append(int(info.split(",")[0]))
     venda.append(float(info.split(",")[1].rstrip('\n')))
print(dia)
print(venda) 

#fazendo o gráfico

import matplotlib.pyplot as plt 

plt.plot(dia, venda)
plt.title("Gráfico diaXvenda de gasolina nos 10 primeiros dia do mês de Julho")
plt.xlabel("dia")  
plt.ylabel("venda")
fig1 = plt.gcf()
plt.show() 

#salvar gráfico
plt.draw() 
fig1.savefig('gasolina.png', dpi=100)