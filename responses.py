import random

def handle__response(message: str) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return 'Hello, welcome to the server!'

    #if p_message == '

    if p_message == '!roll':
        return str(random.randint(1, 6))

    if p_message == '!help':
        return '`Hello, here are some server commands!\n !roll - Rolls a dice\n !coin - Flips a coin`'

    if p_message == '!coin':
        coin = random.randint(1,2)
        if coin == 1:
            return ('It\'s Heads')
        if coin == 2:
            return ('It\'s Tails')


    