def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos
    :param n: uma o mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    """
    relação = dict()
    relação["total"] = len(n)
    org = sorted(n)
    relação["maior"] = org[-1]
    relação["menor"] = org[0]
    relação["média"] = sum(n)/len(n)
    if sit:
        if relação['média'] >= 7:
            relação["situação"] = "BOA"
            if relação['média'] >= 5:
                relação['situação'] = "RAZOÁVEL"
        else:
            relação['situação'] = "RUIM"
    return relação



#Programa Principal
resp = notas(6, 10, 5.5, sit=True)
print(resp)
