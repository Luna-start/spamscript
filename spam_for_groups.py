from __future__ import print_function
import json
import time
import random

import telethon
from pyrogram import Client, filters, ContinuePropagation
from pyrogram.types import Message

import io
from telethon.sync import TelegramClient
from telethon.errors.rpcerrorlist import PeerFloodError, SessionPasswordNeededError
from telethon.tl.functions.channels import JoinChannelRequest

api_id = 29
api_hash = "e0c75275"
phone = '+'


client = TelegramClient(phone, api_id, api_hash)
client.connect()

app = Client(
    "bio",
    api_id=api_id,
    api_hash=api_hash,
    phone_number=phone
)
if not client.is_user_authorized():
    #запрашиваем однаразовый код
    client.send_code_request(phone)
    try:
        client.sign_in(phone, input('Enter verification code: '))
    #дополнительный пароль двухфакторной авторизации если необходимо
    except SessionPasswordNeededError:
        client.sign_in(password=input("Enter password: "))

chats = [dialog for dialog in client.get_dialogs() if dialog.is_group]
print('From which chat you want to parse members:')

# with open('messages.json', 'r', encoding="utf-8") as f:
#     messages = f.readlines()

# message = ('🥁Открытия магазина в телеграмме , не малоизвестный магазин , работающий на форумах- открылся и в тг, '
#            'открывайте салют 🎖\n\n💎У нас в наличие огромное число товара из даркнета 💎\n\nНе будем тянуть, смотрите сами:\n'
#            '•Доски объявлений (авито, wallapop, subitо и многое другое)\n•БА, Карты и ЛК различных банков и стран '
#            '(В наличие сотни банков со всего мира 🌍 )\n•Аккаунты, Вирт. банки, Криптобиржы\n•Тг премиум\n'
#            '•Физ. сим и ватсап (огромный выбор гео)\n•Дедик\n•Кошельки\n•Тг аккаунты и Соц.сети\n•Мануалы\nПереходи'
#            ' скорее , пока мы открыли доступ:\n\n💡ССЫЛКА : @accesoria_perehodnik\n\nдля тэга: купить, продам, продаю,'
#            ' симка, лк, карты, revolut, bunq, lydia, n26, revolut райффайзен, сбер, криптоком, яндекс, каршеринг,'
#             ' пвз, телеграмм аккаунты, paypal,  авито, в наличие, акк, банк, дедик, прокси, впн, тг акки, тг прем, карш'
#             ', вериф, документы, ватсап, тинек, бк, bybit, binance')

message = ('Качественные телеграм аккаунты для любых ваших нужд.\nСпам / инвайт / личное пользование.\n\n'
           'Форматы: TDATA для Telegram Portable версии, SESSION+JSON для софта.\n\nГео: \n🇷🇺 RU (+7)\n🇬🇧 GB (+44)\n'
           '🇮🇩 ID (+62)\n🇰🇿 KZ (+77)\n🇷🇴 RO (+40)\n🇳🇱 NL (+31)\n🇫🇷 FR (+33)\n🇲🇽 MX (+52)\n🇨🇦 CA (+1)\n\n'
           'Отлёжка от 7 дней до 3 месяцев и выше.\n\nЕжедневные бесплатные раздачи тг акков для клиентов!\n\n'
           '_____________\n📝 Ссылка: @accesoria_perehodnik')

[print(str(chats.index(i) + 1) + ' - ' + i.title) for i in chats]
delay = random.randint(15, 40)
chatt = random.choice(chats)

file = '2.jpg'
i = 0
#сделаю рассылку на первые 40 юзеров из списка
while True:
    for chat in chats:
        print("Sending Message to: ", chat)
        try:
            #отправляем сообщение
            delay = random.randint(70, 110)
            i += 1
            client.send_file(chat, file, caption=message)
            print("Message sent to: ", chat)
            print(delay)
            time.sleep(delay)
            random.shuffle(chats)
        #Возможно словить Flood Error, поэтому лучше сразу прекратить спам и разорвать связь
        except PeerFloodError:
            print("[!] Got Flood Error from telegram. \n[!] Try later.")
            app.stop()
            break
        # except You can't write in this chat:
        #
        except telethon.errors.rpcerrorlist.UserBannedInChannelError as e:
            print("[!] Error:", e, "\n UserBannedInChannelError")
            continue
        except telethon.errors.rpcerrorlist.ChatWriteForbiddenError as e:
            print("[!] Error:", e, "\n ChatWriteForbiddenError")
            client.kick_participant(chat.id, 'me')
            print('exit')
            continue
        # except Exception as e:
        #     print("[!] Error:", e, "\n Continue")
        #     continue
        except telethon.errors.rpcerrorlist.UserNotParticipantError as e:
            print("[!] Error:", e, "\n Continue")
            continue
        except telethon.errors.rpcerrorlist.SlowModeWaitError as e:
            print("[!] Error:", e, "\n Continue")
            continue
        except telethon.errors.rpcbaseerrors.ForbiddenError as e:
            try:
                client.send_message(chat, message)
            except:
                print("[!] Error:", e, "\n Continue")
            continue
        except Exception as e:
            continue



print('\nEnd of the program')
