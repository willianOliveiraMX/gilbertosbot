import re

from attr import has
from modules.financeApiConnection import getBalanceByUserId
from modules.financeApiConnection import createNewDebt
from handlers.debts.listDebts import listDebts
from handlers.debts.deleteDebt import deleteDebt

tempUserId = 1

def debts(update, context):
    value = re.search("\d{1,9}[\,\.]{1}\d{1,2}", update.message.text)
    description = re.split("\d+", update.message.text)
    isList = re.search("lista", update.message.text)
    isDelete = re.search("remover", update.message.text)

    if hasattr(isDelete, "group"):
        debtIdToDelete = re.search("\d+", update.message.text)

        if (hasattr(debtIdToDelete, "group")):
            debtId = int(debtIdToDelete.group(0))
            update.message.reply_text(deleteDebt(debtId), parse_mode="HTML")
            return

        if (not hasattr(debtIdToDelete, "group")):
            update.message.reply_text('Forneça o ID do débito, para que eu possa remove-lo.', parse_mode="HTML")
            return

    if hasattr(isList, "group"):
        page = 1
        numberPage = re.search("\d+", update.message.text)
        if (hasattr(numberPage, "group")):
            page = int(numberPage.group(0))
        update.message.reply_text(listDebts(tempUserId, page), parse_mode="HTML")
        return

    if hasattr(value, "group") and description:

        isDebtCreated = createNewDebt(value=value.group(0), description=description[-1], userId=tempUserId)

        if (isDebtCreated):
            update.message.reply_text("Seu débito foi salvo")
            return
        if (not isDebtCreated):
            update.message.reply_text("Infelizmente algo deu errado. Tente novamente depois.")
            return

    balance = getBalanceByUserId(tempUserId)
    update.message.reply_text(f"Esse é o total de seus débitos esse mês: <strong>{balance['debtTotal']}</strong>", parse_mode="HTML")
