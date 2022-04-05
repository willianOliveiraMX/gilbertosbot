from chatterbot import ChatBot

chatbot = ChatBot(
    "Finance Chat", 
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            "statement_comparison_function": 'chatterbot.comparisons.LevenshteinDistance',
        },
        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',
            'input_text': 'Qual o seu nome?',
            'output_text': 'Olá!, meu nome é Gilberto FinBot.'
        }
    ],
    preprocessors=[
        'chatterbot.preprocessors.clean_whitespace'
    ]
)

def getChatBotResponse(message):
    response = chatbot.get_response(message)
    return str(response)