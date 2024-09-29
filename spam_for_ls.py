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


api_id = 27
api_hash = '1f7d1674a4'
phone = '+1'

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

with open('list.json', 'r') as f:
    chats = f.readlines()

with open('messages.json', 'r', encoding="utf-8") as f:
    messages = f.readlines()
# chats = [dialog for dialog in client.get_dialogs() if dialog.is_user]
#
#
# [print(str(chats.index(i) + 1) + ' - ' + i.title) for i in chats]
delay = random.randint(15, 40)


i = 0
#сделаю рассылку на первые 40 юзеров из списка
for chat in chats:
    print("Sending Message to: ", chat)
    try:
        #отправляем сообщение
        delay = random.randint(70, 110)
        i += 1
        send_entity = client.get_entity(chat)
        query = client.inline_query("@PostBot", "668863e8ae937")
        result = query[0].click(send_entity)
        # message = messages[i]
        # client.send_message(chat, message)
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
    except telethon.errors.rpcerrorlist.ChatWriteForbiddenError as e:
        print("[!] Error:", e, "\n ChatWriteForbiddenError")
        client.kick_participant(chat.id, 'me')
        print('exit')
        continue
    except telethon.errors.rpcerrorlist.UsernameInvalidError as e:
        print("[!] Error:", e, "\n userInvalid")
        continue
    except ValueError as e:
        print("[!] Error:", e, "\n userInvalid")
        continue
    except telethon.errors.rpcerrorlist.UserNotParticipantError as e:
        print("[!] Error:", e, "\n Continue")
        continue

print('\nEnd of the program')
