from modules.financeApiConnection import getBalanceByToken

def balance(update, context):
    balance = getBalanceByToken(token=update.message.chat_id)
    update.message.reply_text(f"Aqui está o seu saldo do mês atual: \n\nDébito: <b>{balance['debtTotal']}</b> \nReceita: <b>{balance['incomeTotal']}</b> \nSaldo: <b>{balance['balance']}</b>", parse_mode="HTML")