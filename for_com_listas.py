'''
4) Escreva um programa que preencha uma lista com modelos de 05 (cinco) carros (exemplos: Gol, HB20, etc) e em seguida o consumo destes carros, isto é, quantos quilômetros cada um deles faz com 1 (um) litro de gasolina. Calcule e mostre:
a) O modelo mais econômico; 
b) Quantos litros de gasolina cada um dos carros cadastrados consome para percorrer uma distância de 1.000 quilômetros e quanto isto custará, considerando que a gasolina custe R$ 5,499 o litro.
Abaixo uma tela de exemplo. A disposição das informações deve ser o mais próximo possível ao exemplo. Os dados são fictícios e podem mudar a cada execução do programa. 
Comparativo de Consumo de Combustível
Veículo 1               Veículo 2               Veículo 3           Veículo 4               Veículo 5
Nome: fusca             Nome: gol               nome: uno           Nome: vectra            Nome: Peugeout
Km por litro: 7         Km por litro: 10        km por litro: 12.5  Km por litro: 9         Km por litro: 14.5

Relatório Final
1 - fusca - 7.0 - 142.9 litros - R$ 321.43
2 - gol - 10.0 - 100.0 litros - R$ 225.00
3 - uno - 12.5 - 80.0 litros - R$ 180.00
4 - vectra - 9.0 - 111.1 litros - R$ 250.00
5 - peugeout - 14.5 - 69.0 litros - R$ 155.17
O menor consumo é do peugeout.
'''
veiculo1 = []
veiculo2 = []
veiculo3 = []
veiculo4 = []
veiculo5 = []
veiculos = [veiculo1, veiculo2, veiculo3, veiculo4, veiculo5]
for i in range(0, 5):
    modelo = input('Qual o modelo do carro? ')
    veiculos[i].append(modelo)
    consumo_por_litro = float(input('Qual o consumo por litro dele? '))
    veiculos[i].append(consumo_por_litro)

consumo_em_mil_km_veiculo1 = (1000 / veiculo1[1])
consumo_em_mil_km_veiculo2 = (1000 / veiculo2[1])
consumo_em_mil_km_veiculo3 = (1000 / veiculo3[1])
consumo_em_mil_km_veiculo4 = (1000 / veiculo4[1])
consumo_em_mil_km_veiculo5 = (1000 / veiculo5[1])

custo_veiculo1 = (consumo_em_mil_km_veiculo1 * 5.499)
custo_veiculo2 = (consumo_em_mil_km_veiculo2 * 5.499)
custo_veiculo3 = (consumo_em_mil_km_veiculo3 * 5.499)
custo_veiculo4 = (consumo_em_mil_km_veiculo4 * 5.499)
custo_veiculo5 = (consumo_em_mil_km_veiculo5 * 5.499)

print('Comparativo de Consumo de Combustível')
for j in range(0, 5):
    print('Veículo', j + 1)
    print('Nome: ', veiculos[j][0])
    print('Km por litro: ', veiculos[j][1])
    print(" ")

print('Relatório Final: ')
print('1 - {0} - {1} - {2:.2f} litros - R${3:.2f}'.format(
    veiculo1[0], veiculo1[1], consumo_em_mil_km_veiculo1, custo_veiculo1))
print('2 - {0} - {1} - {2:.2f} litros - R${3:.2f}'.format(
    veiculo2[0], veiculo2[1], consumo_em_mil_km_veiculo2, custo_veiculo2))
print('3 - {0} - {1} - {2:.2f} litros - R${3:.2f}'.format(
    veiculo3[0], veiculo3[1], consumo_em_mil_km_veiculo3, custo_veiculo3))
print('4 - {0} - {1} - {2:.2f} litros - R${3:.2f}'.format(
    veiculo4[0], veiculo4[1], consumo_em_mil_km_veiculo4, custo_veiculo4))
print('5 - {0} - {1} - {2:.2f} litros - R${3:.2f}'.format(
    veiculo5[0], veiculo5[1], consumo_em_mil_km_veiculo5, custo_veiculo5))

if veiculos[0][1] > veiculos[1][1] and veiculos[0][1] > veiculos[2][1] and veiculos[0][1] > veiculos[3][1] and veiculos[0][1] > veiculos[4][1]:
    print(
        'O modelo mais econômico é o {0} com {1} km/L.'.format(veiculos[0][0], veiculos[0][1]))
elif veiculos[1][1] > veiculos[0][1] and veiculos[1][1] > veiculos[2][1] and veiculos[1][1] > veiculos[3][1] and veiculos[1][1] > veiculos[4][1]:
    print(
        'O modelo mais econômico é o {0} com {1} km/L.'.format(veiculos[1][0], veiculos[1][1]))
elif veiculos[2][1] > veiculos[0][1] and veiculos[2][1] > veiculos[1][1] and veiculos[2][1] > veiculos[3][1] and veiculos[2][1] > veiculos[4][1]:
    print(
        'O modelo mais econômico é o {0} com {1} km/L.'.format(veiculos[2][0], veiculos[2][1]))
elif veiculos[3][1] > veiculos[0][1] and veiculos[3][1] > veiculos[1][1] and veiculos[3][1] > veiculos[2][1] and veiculos[3][1] > veiculos[4][1]:
    print(
        'O modelo mais econômico é o {0} com {1} km/L.'.format(veiculos[3][0], veiculos[3][1]))
else:
    print(
        'O modelo mais econômico é o {0} com {1} km/L.'.format(veiculos[4][0], veiculos[4][1]))
