import aiogram as aio
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import random as rnd
from modules.RPS import RSP

rock = RSP.GameItem('Камень', 0, 2, 1)
paper = RSP.GameItem('Бумага', 1, 0, 2)
scissors = RSP.GameItem('Ножницы', 2, 1, 0)

handGame = RSP.handItem(rock, scissors, paper)

with open('pivacy/DadOrange_bot.txt', 'r') as tokenBot_file:
    thisBotToken = tokenBot_file.read()

thisBot = aio.Bot(thisBotToken)
dp = aio.Dispatcher(thisBot)
flagEcho = 'False'
flagRSP = 'False'

with open('cache/flag_RSP.txt', 'w') as flagRSP_file:
    flagRSP_file.write('False')

with open('cache/flag_echo.txt', 'w') as flagEcho_file:
    flagEcho_file.write(str(flagEcho))

with open('cache/flag_echo.txt', 'r') as flagEcho_file:
    flagEcho = flagEcho_file.read()

with open('cache/flag_RSP.txt', 'r') as flagRSP_file:
    flagRSP = flagRSP_file.read()


@dp.message_handler(commands=["start"])
async def process_start_command(message: aio.types.Message):
    await message.reply("Привет! \nЯ на связи готов к работе! \nНапиши /help и я расскажу что могу")


@dp.message_handler(commands=["help"])
async def process_help_command(message: aio.types.Message):
    await message.reply("/help - список команд \n/echo - эхо-бот \n/RSP - Игра")


@dp.message_handler(commands=["echo"])
async def echo_bot(message: aio.types.Message):
    await message.reply(' Играем в эхо! \nНапиши /echostop, если хочешь закончить')
    flagEcho = "True"
    with open('cache/flag_echo.txt', 'w') as flagEcho_file:
        flagEcho_file.write(str(flagEcho))


@dp.message_handler(commands=["RSP"])
async def RSP_bot(message: aio.types.Message):
    await message.reply(' Играем в КНБ! \n/Rock \n/Scissors \n/Paper \nНапиши /RSPstop, если хочешь закончить')
    flagRSP = "True"
    with open('cache/flag_RSP.txt', 'w') as flagRSP_file:
        flagRSP_file.write(str(flagRSP))

with open('cache/flag_RSP.txt', 'r') as flagRSP_file:
    flagRSP = flagRSP_file.read()


if flagRSP == 'True':
    @dp.message_handler(commands=['Rock'])
    async def thisRock(message: aio.types.Message):
        player_hand = handGame.choise(thisPlayer=True, thisChoise=1)
        bot_hand = handGame.choise(thisPlayer=False, thisChoise=1)
        await thisBot.send_message(message.from_user.id, text=f"{player_hand['msg']}")
        await thisBot.send_message(message.from_user.id, player_hand)
        await thisBot.send_message(message.from_user.id, text=f"{bot_hand['msg']}")
        await thisBot.send_message(message.from_user.id,
                                   text=f"{RSP.compareHand(player_hand['Game_Item'], bot_hand['Game_Item'])}")


    @dp.message_handler(commands=['Scissors'])
    async def thisScissors(message: aio.types.Message):
        player_hand = handGame.choise(thisPlayer=True, thisChoise=3)
        await thisBot.send_message(message.from_user.id, text=f"{player_hand['msg']}")
        bot_hand = handGame.choise(thisPlayer=False, thisChoise=3)
        await thisBot.send_message(message.from_user.id, player_hand)
        await thisBot.send_message(message.from_user.id, text=f"{bot_hand['msg']}")
        await thisBot.send_message(message.from_user.id,
                                   text=f"{RSP.compareHand(player_hand['Game_Item'], bot_hand['Game_Item'])}")


    @dp.message_handler(commands=['Paper'])
    async def thisPaper(message: aio.types.Message):
        player_hand = handGame.choise(thisPlayer=True, thisChoise=2)
        await thisBot.send_message(message.from_user.id, text=f"{player_hand['msg']}")
        bot_hand = handGame.choise(thisPlayer=False, thisChoise=2)
        await thisBot.send_message(message.from_user.id, player_hand)
        await thisBot.send_message(message.from_user.id, text=f"{bot_hand['msg']}")
        await thisBot.send_message(message.from_user.id,
                                   text=f"{RSP.compareHand(player_hand['Game_Item'], bot_hand['Game_Item'])}")


@dp.message_handler()
async def get_text_from_message(message: aio.types.Message):
    with open('cache/flag_echo.txt', 'r') as flagEcho_file:
        flagEcho = flagEcho_file.read()
    with open('cache/flag_RSP.txt', 'r') as flagRSP_file:
        flagRSP = flagRSP_file.read()
    if flagRSP == 'False':
        if flagEcho == 'True':
            if message.text != '/echostop':
                await thisBot.send_message(message.from_user.id, f'Все говорят ({message.text}) а ты купи слона')
                flagEcho = 'True'
            elif message.text == '/echostop':
                await thisBot.send_message(message.from_user.id, 'Всё')
                flagEcho = 'False'
        else:
            flagEcho = 'False'
            await message.reply('Введите команду /help')
        with open('cache/flag_echo.txt', 'w') as flagEcho_file:
            flagEcho_file.write(str(flagEcho))
    else:
        if message.text == '/RSPstop':
            await thisBot.send_message(message.from_user.id, 'Не играем в КНБ')
            flagRSP = 'False'
            with open('cache/flag_RSP.txt', 'w') as flagRSP_file:
                flagRSP_file.write(str(flagRSP))


aio.executor.start_polling(dp)
