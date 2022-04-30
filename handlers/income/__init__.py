import re
from modules.financeApiConnection import listIncomeByUserId, createNewIncome, deleteIncomeById

def listIncome(update, context):
    value = re.search("\d{1,9}[\,\.]{1}\d{1,2}", update.message.text)
    description = re.split("\d+", update.message.text)
    isDelete = re.search("remover", update.message.text)

    if hasattr(isDelete, "group"):
        incomeToDelete = re.search("\d+", update.message.text)

        if (hasattr(incomeToDelete, "group")):
            debtId = int(incomeToDelete.group(0))

            if (not debtId):
                update.message.reply_text('Forneça o ID da renda a ser deletada.', parse_mode="HTML")
                return

            deleteResult = deleteIncomeById(debtId, update.message.chat_id)
            if (deleteResult):
                update.message.reply_text('Renda deletada com sucesso!', parse_mode="HTML")
                return
            update.message.reply_text('Algo deu errado ao tentar deletar a renda.', parse_mode="HTML")
            return

        if (not hasattr(incomeToDelete, "group")):
            update.message.reply_text('Forneça o ID do débito, para que eu possa remove-lo.', parse_mode="HTML")
            return

    if hasattr(value, "group") and description:
        isIncomeCreated = createNewIncome(value=value.group(0), description=description[-1], token=update.message.chat_id)
        if (isIncomeCreated):
            update.message.reply_text("Seu ganho foi salvo")
            return
        if (not isIncomeCreated):
            update.message.reply_text("Infelizmente algo deu errado. Tente novamente depois.")
            return

    income = listIncomeByUserId(token=update.message.chat_id)
    newMessage = f'Total: {income["tatalIncome"]} \n'
    print(income["incomeList"])
    for incomeItem in income["incomeList"]:
        newMessage = newMessage + f'\n Id: {incomeItem["id"]} \n Descrição: {incomeItem["description"]} \n Valor: <b>{incomeItem["value"]}</b> \n Data: {incomeItem["createdat"]} \n ---------------------------------------------------- \n'

    update.message.reply_text(f'Abaixo estão os seus ganhos: \n \n ---------------------------------------------------- \n {newMessage}', parse_mode="HTML")
