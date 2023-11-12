#coletando algumas informações 
nome = (input('digite seu nome:'))
print ('seja bem vindo ')
print(nome.capitalize().title())
idade = int(input('qual sua idade:'))
quantidade = input('quantas pessoas moram com voçê:')
 # Definir as fórmulas para o cálculo das emissões de GEE
def calcular_emissoes(carro, onibus, bicicleta):
    
    emissoes_carro = carro['distancia'] * carro['consumo'] * carro['fator_emissao']

    # Fórmula para o cálculo das emissões de GEE de um ônibus
    emissoes_onibus = onibus['distancia'] * onibus['consumo'] * onibus['fator_emissao']

    # Fórmula para o cálculo das emissões de GEE de uma bicicleta
    emissoes_bicicleta = bicicleta['distancia'] * bicicleta['fator_emissao']

    # Retornar as emissões de GEE calculadas
    return emissoes_carro, emissoes_onibus, emissoes_bicicleta

# Coletar os dados sobre o meio de transporte utilizado
carro = {'distancia': 10, 'consumo': 8, 'fator_emissao': 2.5}
onibus = {'distancia': 20, 'consumo': 5, 'fator_emissao': 1.5}
bicicleta = {'distancia': 5, 'fator_emissao': 0}

# Calcular as emissões de GEE
emissoes_carro, emissoes_onibus, emissoes_bicicleta = calcular_emissoes(carro, onibus, bicicleta)

print('selecione umas das opções abaixo:')

print ('1.carro')
print('2.onibus')
print('3.bicicleta')
veiculo = input('qual veiculos voçê gostaria de selecionar:')
if veiculo == '1':
    print('Emissões de GEE do carro aproximadamente, por pessoa:', emissoes_carro)
elif veiculo == '2':
    print('Emissões de GEE do ônibus aproximadamente, por pessoa:', emissoes_onibus)
elif veiculo == '3':
    print('Emissões de GEE da bicicleta aproximadamente, por pessoa:', emissoes_bicicleta)
else:
    print ('opção invalida')
