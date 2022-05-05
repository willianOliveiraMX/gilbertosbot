import os
import re
from telegram.ext.updater import Updater
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
from dotenv import load_dotenv
from modules.userActions import verifyIfUserAlreadyAdd, createNewUser, addUserEmail
from handlers.debts import debts
from handlers.balance import balance
from handlers.income import listIncome

load_dotenv()
CHAT_BOT_TOKEN_ID = os.getenv('CHAT_BOT_TOKEN_ID')

updater = Updater(CHAT_BOT_TOKEN_ID,
                  use_context=True)
  
def start(update, context):

    print(update.message.chat_id)
    userAlreadyAdd = verifyIfUserAlreadyAdd(update.message.chat_id)

    if (not userAlreadyAdd):
        newUserResult = createNewUser(token=update.message.chat_id)
        print(newUserResult)
        update.message.reply_text(
            "Olá, eu sou o Gilberto FinBot. Por favor me informe o seu email, para continuarmos."
        )
    
    if (userAlreadyAdd):
        update.message.reply_text(
            "Olá, eu sou o Gilberto FinBot. Estou aqui para te ajudar com suas finanças pessoais.")

def help(update, context):
    update.message.reply_text("<strong>Esses são meus comandos:</strong> \n\n /inicio - inicia a conversa \n\n /ajuda - Abre esse menu \n\n /debitos ou /ds - Mostra o seus débitos: \n      Exemplos  \n           -Adicionar débito --> /ds R$ 10,90 Lanche\n           -Remover débito --> /ds remover ID \n           -Listar débitos --> /ds lista\n\n /receitas ou /rs - Mostra seus ganhos \n      Exemplos\n           -Adicionar renda --> /rs R$ 100,00 Salário \n           -Remover renda --> /rs remover ID \n           -Listar renda --> /rs lista\n\n  /saldo ou /so - mostra o balanço total", parse_mode="HTML")

def unknown_text(update, context):
    update.message.reply_text(
        "Desculpe, não entendi.")

def unknown(update, context):
    emailRegex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if(re.fullmatch(emailRegex, update.message.text)):
        print("This is not mistake.")
        resultAddUser = addUserEmail(update.message.chat_id, update.message.text)
        if (resultAddUser):
            update.message.reply_text("Obrigado por completar o seu cadastro")
            return
        else:
            update.message.reply_text("Não foi possível finalizar o seu cadastro. Tente mais tarde.")
            return
    update.message.reply_text("Desculpe, não entendi.")

def error(update, context):
    print("Infelizmente, eu tive algum erro {context.error}")


updater.dispatcher.add_handler(CommandHandler('inicio', start))
updater.dispatcher.add_handler(CommandHandler('ajuda', help))

updater.dispatcher.add_handler(CommandHandler('debitos', debts))
updater.dispatcher.add_handler(CommandHandler('ds', debts))

updater.dispatcher.add_handler(CommandHandler('saldo', balance))
updater.dispatcher.add_handler(CommandHandler('so', balance))

updater.dispatcher.add_handler(CommandHandler('receitas', listIncome))
updater.dispatcher.add_handler(CommandHandler('rs', listIncome))

updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(
    Filters.command, unknown))  # Filters out unknown commands
  
# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))
  
updater.start_polling()
