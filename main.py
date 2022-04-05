from telegram.ext.updater import Updater
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
from modules.chatBotInput import getChatBotResponse
from modules.verifyUserAlreadyAdd import verifyUserAlreadyAdd
from handlers.debts import debts
from handlers.balance import balance
from handlers.income import listIncome

updater = Updater("",
                  use_context=True)
  
def start(update, context):
    print(update.message.chat_id)
    userAlreadyAdd = verifyUserAlreadyAdd(update.message.chat_id)
    print(update.message.text)
    if (True):
        update.message.reply_text(
            "Olá, eu sou o Gilberto FinBot. Por favor me informe o seu email, para continuarmos."
        )
    
    if (False):
        update.message.reply_text(
            "Olá, eu sou o Gilberto FinBot. Estou aqui para te ajudar com suas finanças pessoais.")

def help(update, context):
    update.message.reply_text("Esses são meus comandos: \n \n /inicio - inicia a conversa \n /ajuda - Abre esse menu \n /debitos ou /ds - Mostra o seus débitos \n /receitas ou /rs - Mostra seus ganhos \n /saldo ou /so - mostra o balanço total")

def unknown_text(update, context):
    update.message.reply_text(
        "Desculpe, não entendi.")

def unknown(update, context):
    update.message.reply_text(getChatBotResponse(update.message.text))

def error(update, context):
    print("Infelizmente, tive algum erro {context.error}")


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
