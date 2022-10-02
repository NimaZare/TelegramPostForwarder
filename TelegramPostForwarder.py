from telethon.sync import TelegramClient, events, utils
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty

# Application Verson : 1.2
# Developer: Nima Zare
# Web : https://nimazare.github.io/
# Telegram, Instagram, Twitter Account : @DeveloperNima
# Email : NimaProgrammer@Gmail.com

api_id = YOUR_APP_ID(Ex: 123654)
api_hash = 'YOUR_APP_HASH_CODE (Ex: 85dewvs54d....)'
phone = input('Enter your phone number (ex. +989110000000) ==> ')
client = TelegramClient(phone, api_id, api_hash)
list_all_origins = []
list_all_origins_title = []
list_origins = []
list_destinations = []
 
client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the login code from Telegram : '))

print("----------------------------------------")
print("I'm Online")
print("----------------------------------------")
print("** Please choose your origin and destination :")
print("[All Your Origins List]")
counter_1 = 0

chats = []
last_date = None
chunk_size = 200
 
result = client(GetDialogsRequest(offset_date=last_date,
             offset_id=0,
             offset_peer=InputPeerEmpty(),
             limit=chunk_size,
             hash = 0))
chats.extend(result.chats)

for dialog in chats:
    try:
        list_all_origins.append(dialog)
        list_all_origins_title.append(dialog.title)
        print(counter_1, ". ", dialog.title)
        counter_1 += 1
    except:
        continue
    

print("----------------------------------------")
channels_index = input("Enter your origin number (ex. 1, 5, 4, 7): ")
list_origin = channels_index.split(',')
list_origin = [int(item) for item in list_origin]
for n in list_origin:
    list_origins.append(list_all_origins[n])

print("----------------------------------------")
print("OK. Your origins title is :")
for nz in list_origins:
    print(nz.title)

print("----------------------------------------")
channels_index2 = input("Enter your destination number (ex. 1, 5, 4, 7): ")
list_destination = channels_index2.split(',')
list_destination = [int(item) for item in list_destination]
for nz in list_destination:
    list_destinations.append(list_all_origins[nz])

print("----------------------------------------")
print("OK. Your destinations title is :")
for nnz in list_destinations:
    print(nnz.title)

print("----------------------------------------")
print("+++++  Robot is Working Now  +++++")

@client.on(events.NewMessage(chats=list_origins))
async def update_handler(event):
    if 'hello' in event.raw_text or event.raw_text == '/start':
        await event.reply('Hi, I\'m Robot 😎')
    else:
        for dialog in list_all_origins:
            if event.chat.title == dialog.title:
                for ds in list_destinations:
                    await client.send_message(ds, event.message)
                    

        


client.start()
client.run_until_disconnected()

