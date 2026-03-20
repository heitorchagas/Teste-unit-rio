# Código do segundo aluno

def aprovado(media, total, faltas):
    presencas = (total - faltas) * 100
    if media >= 6:
        return "Aprovado"
    elif presencas >= 75:
        return "Reprovado por faltas"
    else:
        return "Precisa fazer a prova final"