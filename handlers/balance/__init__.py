from modules.financeApiConnection import getBalanceByUserId

def balance(update, context):
    balance = getBalanceByUserId(1)
    update.message.reply_text(f"Aqui está o seu saldo do mês atual: \n\nDébito: <b>{balance['debtTotal']}</b> \nReceita: <b>{balance['incomeTotal']}</b> \nSaldo: <b>{balance['balance']}</b>", parse_mode="HTML")