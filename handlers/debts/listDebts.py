from datetime import datetime
from modules.financeApiConnection import listDebtsByUserId

def listDebts(token, page):
    debtsList = listDebtsByUserId(token=token, page=page)
    debtsMessage = ''
    for debts in debtsList:
        newMessage = f' Id: {debts["id"]} \n Descrição: {debts["description"]} \n Preço: <b>{debts["value"]}</b> \n Data: {debts["createdat"]} \n ---------------------------------------------------- \n'
        debtsMessage = debtsMessage + newMessage

    return f'Essa é a lista dos seus débitos: \n \n ---------------------------------------------------- \n {debtsMessage} \n página: {page}                                 >>>>>>\n Digite o comando abaixo para \n carregar mais débitos: \n\n <b> /ds lista {page + 1}</b>'
