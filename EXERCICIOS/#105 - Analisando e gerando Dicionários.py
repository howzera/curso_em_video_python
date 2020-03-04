# Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar 
# um dicionário com as seguintes informações:

# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação (opcional)
# https://youtu.be/Kbs97l38vVQ

def notas(*n, sit=False):
    """
        - > Função para analisar notas e situação de vários alunos.
        param n: uma ou mais notas dos alunos (aceita várias)
        param sit: valor opcional, indicando se deve ounão adicionar a situação.
        return: dicionário com várias informações sobre a situação da turma.
    """
    r = dict()
    r['Total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)

    if sit:
        if r['media'] >= 7:
            r['situação'] = 'BOA'
        elif r['media'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r

# MAIN
resp = notas(9.5, 9.5, 8.5, sit=True)
print(resp)
help(notas)