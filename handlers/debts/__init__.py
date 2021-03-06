import re
from modules.financeApiConnection import getBalanceByToken
from modules.financeApiConnection import createNewDebt
from handlers.debts.listDebts import listDebts
from handlers.debts.deleteDebt import deleteDebt

def debtsList(update, context):
    page = 1
    numberPage = re.search("\d+", update.message.text)
    if (hasattr(numberPage, "group")):
        page = int(numberPage.group(0))
    update.message.reply_text(listDebts(token=update.message.chat_id, page=page), parse_mode="HTML")

def debts(update, context):
    value = re.search("\d{1,9}[\,\.]{1}\d{1,2}", update.message.text)
    description = re.split("\d+", update.message.text)
    isList = re.search("lista", update.message.text)
    isDelete = re.search("remover", update.message.text)

    if hasattr(isDelete, "group"):
        debtIdToDelete = re.search("\d+", update.message.text)

        if (hasattr(debtIdToDelete, "group")):
            debtId = int(debtIdToDelete.group(0))
            update.message.reply_text(deleteDebt(debtId, token=update.message.chat_id), parse_mode="HTML")
            return

        if (not hasattr(debtIdToDelete, "group")):
            update.message.reply_text('Forneça o ID do débito, para que eu possa remove-lo.', parse_mode="HTML")
            return

    if hasattr(isList, "group"):
        debtsList(update, context)
        return

    if hasattr(value, "group") and description:

        isDebtCreated = createNewDebt(value=value.group(0), description=description[-1], token=update.message.chat_id)

        if (isDebtCreated):
            update.message.reply_text("Seu débito foi salvo")
            return
        if (not isDebtCreated):
            update.message.reply_text("Infelizmente algo deu errado. Tente novamente depois.")
            return

    balance = getBalanceByToken(token=update.message.chat_id)
    print(balance)
    update.message.reply_text(f"Esse é o total de seus débitos esse mês: <strong>{balance['debtTotal']}</strong>", parse_mode="HTML")
