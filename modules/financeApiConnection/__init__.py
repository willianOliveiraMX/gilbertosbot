import os
import requests
from dotenv import load_dotenv

load_dotenv()
FINNACE_API_URL = os.getenv('FINNACE_API_URL')

def getUserBytId(userId):
    return requests.get(url=f'http://{FINNACE_API_URL}/user/1').json()

def getUserByToken(token):
    return requests.get(url=f'http://{FINNACE_API_URL}/user/token/{token}').json()

def getBalanceByToken(token):
    return requests.get(url=f'http://{FINNACE_API_URL}/balance/{token}').json()

def createNewDebt(value, description, token):
    data = {
        'token': token,
        'description': description,
        'value': value,
        'installmentTotal': '1',
        'dateToPay': 'Fri Mar 18 2022 22:05:08 GMT-0300 (Horário Padrão de Brasília)',
        'isalreadypay': 'true'
    }
    try:
        requests.post(url=f'http://{FINNACE_API_URL}/debt', data=data)
        return True
    except:
        return False

def listDebtsByUserId(token, page):
    return requests.get(url=f'http://{FINNACE_API_URL}/debt/{token}/page/{page}').json()

def deletDebtById(debtId, token):
    return requests.delete(url=f'http://{FINNACE_API_URL}/debt/remove/{debtId}/{token}').json()

def listIncomeByUserId(token): 
    return requests.get(url=f'http://{FINNACE_API_URL}/income/{token}').json()

def createNewIncome(value, description, token):
    data = {
        "description": description,
        "value": value,
        "token": token
    }

    try:
        requests.post(url=f'http://{FINNACE_API_URL}/income', data=data)
        return True
    except:
        return False

def deleteIncomeById(incomeId, token):
    try:
        requests.delete(url=f'http://{FINNACE_API_URL}/income/{incomeId}/{token}')
        return True
    except:
        return False

def createTempUser(token):
    obj = {
        "token": token
    }
    return requests.post(url=f'http://{FINNACE_API_URL}/user', data = obj).json()

def createUser(token, email):
    obj = {
        "token": token,
        "email": email,
    }
    return requests.post(url=f'http://{FINNACE_API_URL}/user', data = obj).json()
