import re
from modules.financeApiConnection import createNewDebt

def addDebtByText (update, context):
    value = re.search("\d{1,9}[\,\.]{1}\d{1,2}", update.message.text)
    descriptionList = re.findall("\s.[a-zA-Z]+", update.message.text)
    description = ""

    for element in descriptionList:
        description = f'{description} {element}'


    if (hasattr(value, "group") and descriptionList):
        isDebtCreated = createNewDebt(value=value.group(0), description=description, token=update.message.chat_id)

        if (isDebtCreated):
            update.message.reply_text("Seu débito foi salvo")
            return True
        if (not isDebtCreated):
            update.message.reply_text("Infelizmente algo deu errado. Tente novamente depois.")
            return True
        return

    return False
