phone = '+'
api_id = 106
api_hash = 'a86bbaca4cb20ad9930'
import time
from telethon.tl.functions.channels import JoinChannelRequest
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


with open('dump.json', 'r') as f:
    channels = f.readlines()


def main():
    i = 0
    for channel in channels:
        print(channel)
        i += 1
        if i != 10:
            try:
                client(JoinChannelRequest(channel))
                print(f'Successfully joined {channel}')
                time.sleep(300)
            except Exception as e:
                print(f'Error joining {channel}, {e}')
        else:
            print('10')
            time.sleep(1000)

            main()

main()
