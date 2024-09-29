# with open('messages.json', encoding="utf-8") as file_in:
#     dump = file_in.read()
# dump = dump.replace('генера', 'генера, ')
# dump = dump.replace('\n', '\\n')
# dump = dump.replace(',', '\n')
# with open('messages.json', "w", encoding="utf-8") as file:
#     file.write(str(dump))
import random

with open('messages.json', 'r', encoding="utf-8") as f:
    channels = f.readlines()
i = 0
while True:
    i += 1
    message = channels[i]
    print(message)


