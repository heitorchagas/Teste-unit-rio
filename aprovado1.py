# Código primeiro aluno

def aprovado(media, total, faltas):
    presencas = total - faltas
    if not (presencas <= 0.75 * total):
        if media >= 6:
            return "Aprovado"
        else:
            return "Precisa fazer a prova final"
    else:
        return "Reprovado por faltas"