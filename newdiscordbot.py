#бот умеет отправлять ваши сообщения от своего имени и собирать логи со всех каналов, можете взять его за отснову для своих проектов


import discord
from discord.ext import commands, tasks
import logging
import datetime

logging.basicConfig(level=logging.INFO)

TOKEN = ''              #токен вашего бота
CHANNEL_ID =            #ID кадала, в который будет отправлять сообщения бот


intents = discord.Intents.default() #константы и интенты для бота(дайте их боту на сайте discord developers, а то будет конфликт)
intents.typing = False
intents.presences = False
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
sendtime = datetime.datetime.now()

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready(): #активация бота
    logging.info(f'Авторизован как: {bot.user}')
    channel = bot.get_channel(CHANNEL_ID)
    if channel is None:
        logging.error(f'ID вашего канала: {CHANNEL_ID} не найден')
        return
    await send_message_from_console(channel)

async def send_message_from_console(channel): #отправка сообщения из консоли
    while True:
        try:
            message = input("Какое сообщение вы хотите отправить от имени бота?: ")
            if message:
                await channel.send(message)
            else:
                print("Вы ничего не ввели")
        except Exception as e:
            logging.error(f"Ошибка: {e}")
            break

@bot.command(name='send_message') #отвечает за инициализацию ID канала
async def send_message(ctx, *, message):
    channel = bot.get_channel(CHANNEL_ID)
    if channel is None:
        await ctx.send(f'Канал с ID {CHANNEL_ID} не найден')
        return
    await channel.send(message)

try:
    bot.run(TOKEN)
except discord.errors.HTTPException as e:
    logging.error(f"Ошибка при запуске бота: {e}")
    print(f"Ошибка прои запуске бота: {e}")
except Exception as e:
    logging.error(f"Ошибка: {e}")
    print(f"Обнаружена ошибка: {e}")


@bot.event #для логов сообщений во всех каналах
async def on_message(message):
    if message.author == bot.user:
        return
    
    with open('logs.txt', "a") as file:
        file.write(f'{message.author} - {message.content} - {datetime.datetime.now()}\n')

                       
try:                        #для запуска бота
    bot.run(TOKEN)
except discord.errors.HTTPException as e:
    logging.error(f"Ошибка прт запуске бота: {e}")
    print(f"Ошибка прт запуске бота: {e}")
except Exception as e:
    logging.error(f"Обнаружена ошибка: {e}")
    print(f"Обнаружена ошибка: {e}")



@bot.event
async def ans_on_message(): #в будущем будет обновляться
    pass

    
