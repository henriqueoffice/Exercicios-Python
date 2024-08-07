

dados = dict()

dados['Nome'] = str(input('Nome: '))
dados['Media'] = float(input(f'Média de {dados["Nome"]}: '))
if dados['Media'] >= 7:
    dados['Situacao'] = "Aprovado"
elif 5 <= dados['Media'] < 7:
    dados['Situacao'] = 'Recuperação'
else:
    dados['Situacao'] = "Reprovado"

print('-=' * 30)
for k,v in dados.items():
    print(f'   - {k} é igual a {v}')
