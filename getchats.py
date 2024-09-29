import io
import json

phone = ''
api_id = 10
api_hash = 'a835eadad9930'

from telethon.sync import TelegramClient
from telethon.errors.rpcerrorlist import PeerFloodError, SessionPasswordNeededError

client = TelegramClient(phone, api_id, api_hash)
client.connect()

if not client.is_user_authorized():
    #запрашиваем однаразовый код
    client.send_code_request(phone)
    try:
        client.sign_in(phone, input('Enter verification code: '))
    #дополнительный пароль двухфакторной авторизации если необходимо
    except SessionPasswordNeededError:
        client.sign_in(password=input("Enter password: "))



dump = {}

chats = [dialog.entity for dialog in client.get_dialogs() if dialog.is_group]
for chat in chats:
    if hasattr(chat, 'username') and hasattr(chat, 'title'):
        dump[chat.title] = f'https://t.me/{chat.username}'

    # for example, let's save everything to a file
    with open('dump.json', 'w', encoding='utf-8') as file:
        json.dump(dump, file, indent=4)

dump = 'dump.json'

links = {}
word = u'http'
with io.open('dump.json', encoding='utf-8') as file:
    for line in file:
        if word in line:
            lisst = line.split(':', 1)
            try:
                if not "None" in str(lisst):
                    links = lisst[1]
                else:
                    pass
            except Exception as e:
                print(e)
    with open('links.json', 'w', encoding='utf-8') as file:
        json.dump(links, file, indent=4)

with open('dump.json') as file_in:
    dump = file_in.read()
dump = dump.replace(',', '')

with open('dump.json', "w") as file:
    file.write(dump)