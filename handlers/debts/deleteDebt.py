from modules.financeApiConnection import deletDebtById

def deleteDebt(debtId, token):
    result = deletDebtById(debtId, token)
    print(result)
    if result["affected"] == 1:
        return 'Seu débito foi deletado com sucesso.'
    return 'Algo deu errado. Não pude deletar o débito'