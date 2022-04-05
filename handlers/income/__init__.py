from modules.financeApiConnection import listIncomeByUserId

def listIncome(update, context):
    income = listIncomeByUserId(userId=1)
    newMessage = f'Total: {income["tatalIncome"]} \n'
    print(income["incomeList"])
    for incomeItem in income["incomeList"]:
        newMessage = newMessage + f'\n Id: {incomeItem["id"]} \n Descrição: {incomeItem["description"]} \n Valor: <b>{incomeItem["value"]}</b> \n Data: {incomeItem["createdAt"]} \n ---------------------------------------------------- \n'

    update.message.reply_text(f'Abaixo estão os seus ganhos: \n \n ---------------------------------------------------- \n {newMessage}', parse_mode="HTML")
