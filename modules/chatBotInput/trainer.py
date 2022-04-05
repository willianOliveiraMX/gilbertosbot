from modules.chatBotInput import chatbot
from chatterbot.trainers import ListTrainer

trainer = ListTrainer(chatbot)

trainer.train([
    "Olá",
    "Oi, tudo bem?",
    "Tudo bem!",
    "Oi",
    "Olá",
])

trainer.train([
    "Bom dia",
    "Bom dia, como vai?",
])

trainer.train([
    "Boa noite",
    "Boa noite, como vai?",
])

trainer.train([
    "Boa tarde",
    "Boa tarde, como vai?",
])

trainer.train([
    "Boa tarde",
    "Boa tarde, como vai?",
])

trainer.train([
    "Qual o seu nome?",
    "Eu sou Gilberto FinBot. Sou um bot desenvolvido para te ajudar com suas finanças pessoais.",
    "Quantos anos você tem?",
    "Ainda sou muito neném, não fiz meu primeiro aniversário."
])

trainer.train([
    "Você pode declarar imposto de renda?",
    "Ainda não posso fazer esse tipo coisa.",
    "Você pode fazer contas?",
    "Posso fazer alguns cálculos."
])

trainer.train([
    "Você entende de economia?",
    "Apenas o suficiente para entender de finanças pessoais.",
])
