from modules.financeApiConnection import getUserByToken, createTempUser, createUser

def verifyIfUserAlreadyAdd(token):
    result = getUserByToken(token)
    if(not result):
        return False
    return True

def createNewUser(token):
    return createTempUser(token=token)

def addUserEmail(token, email):
    return createUser(token=token, email=email)
