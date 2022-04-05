from modules.financeApiConnection import getUserBytId

def verifyUserAlreadyAdd(chatId):
    print(chatId)
    result = getUserBytId(chatId)
    print(result)
    return "Usuário já adicionado"
