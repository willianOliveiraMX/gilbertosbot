import requests

apiendpoint = "http://localhost:3000"

def getUserBytId(userId):
    return requests.get(url=f'{apiendpoint}/user/1').json()

def getBalanceByUserId(userId):
    return requests.get(url=f'{apiendpoint}/balance/{userId}/month/2').json()

def createNewDebt(value, description, userId):
    data = {
        'userId': userId,
        'description': description,
        'value': value,
        'groupId': 3,
        'monthId': 2,
        'installmentTotal': 1,
        'dateToPay': 'Fri Mar 18 2022 22:05:08 GMT-0300 (Horário Padrão de Brasília)',
        'isalreadypay': 'true'
    }
    try:
        requests.post(url=f'{apiendpoint}/debt', data=data)
        return True
    except:
        return False

def listDebtsByUserId(userId, page):
    return requests.get(url=f'{apiendpoint}/debt/{userId}/page/{page}').json()

def deletDebtById(debtId):
    return requests.delete(url=f'{apiendpoint}/debt/remove/{debtId}').json()

def listIncomeByUserId(userId): 
    return requests.get(url=f'{apiendpoint}/income/{userId}').json()
