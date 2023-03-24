import telegram

import asyncio


# Crea una instancia del bot con tu token de acceso
bot = telegram.Bot(token='ID_TOKEN')

# Recupera el mensaje de la línea de comandos


# Envía el mensaje al bot
async def enviar_mensaje():
    await bot.send_message(chat_id='ID_CHAT', text='MENSAJE')

asyncio.run(enviar_mensaje())
