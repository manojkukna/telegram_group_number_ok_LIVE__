from telethon.sync import TelegramClient
from telethon.errors import SessionPasswordNeededError
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.types import InputPeerChannel
import csv


# Replace with your own values
api_id = '22696579'
api_hash = '04cca6e3feb85d1c91ab98f8a4056829'
phone_number = '+919106963281'  # Ensure this is in the correct international format
# gro
# Telegram API credentials
# api_id = 'your_api_id'
# api_hash = 'your_api_hash'

# Phone number and username for login
phone = phone_number
username = 'Manoj Kukna'

# Destination group or channel username  -1001352400960
group_username = -1001352400960

# # Create a client instance
# client = TelegramClient(username, api_id, api_hash)
#
# async def main():
#     try:
#         # Connect to Telegram
#         await client.start()
#         print("Client connected successfully")
#
#         # Resolve the group entity
#         entity = await client.get_entity(group_username)
#
#         # Get the history of the group chat
#         messages = await client(GetHistoryRequest(
#             peer=entity,
#             limit=0,  # Limit defines the number of messages to be retrieved
#             offset_date=None,
#             offset_id=0,
#             max_id=0,
#             min_id=0,
#             add_offset=0,
#             hash=0
#         ))
#
#         # Prepare CSV file for writing
#         with open('telegram_group_messages.csv', 'w', newline='', encoding='utf-8') as file:
#             writer = csv.writer(file)
#             writer.writerow(["Message ID", "Date", "Sender ID", "Message"])
#
#             # Iterate over messages and write to CSV
#             for msg in messages.messages:
#                 writer.writerow([msg.id, msg.date, msg.from_id, msg.message])
#             print(msg)
#         print("Messages saved to telegram_group_messages.csv")
#
#     except SessionPasswordNeededError:
#         print('Telegram account with 2FA enabled. Please enter your password.')
#         client.run_until_disconnected()
#
# # Run the main function
# with client:
#     client.loop.run_until_complete(main())
#




from telethon.sync import TelegramClient
from telethon.errors import SessionPasswordNeededError
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.types import InputPeerChannel
import pandas as pd

# Telegram API credentials
# api_id = 'your_api_id'
# api_hash = 'your_api_hash'
#
# # Phone number and username for login
# phone = 'your_phone_number'
# username = 'your_telegram_username'
#
# # Destination group or channel username
# group_username = 'group_username'


async def main():
    # Getting information about yourself
    me = await client.get_me()

    # "me" is a user object. You can pretty-print
    # any Telegram object with the "stringify" method:
    print(me.stringify())

    # When you print something, you see a representation of it.
    # You can access all attributes of Telegram objects with
    # the dot operator. For example, to get the username:
    username = me.username
    print(username)
    print(me.phone)

    # You can print all the dialogs/conversations that you are part of:
    async for dialog in client.iter_dialogs():
        print(dialog.name, 'has ID', dialog.id)

    # You can send messages to yourself...
    await client.send_message(-1001398310253, 'Hello, myself!')
    # # ...to some chat ID
    # await client.send_message(-100123456, 'Hello, group!')
    # # ...to your contacts
    # await client.send_message('+34600123123', 'Hello, friend!')
    # # ...or even to any username
    # await client.send_message('username', 'Testing Telethon!')
    #
    # # You can, of course, use markdown in your messages:
    # message = await client.send_message(
    #     'me',
    #     'This message has **bold**, `code`, __italics__ and '
    #     'a [nice website](https://example.com)!',
    #     link_preview=False
    #
    #
    # # Sending a message returns the sent message object, which you can use
    # print(message.raw_text)
    #
    # # You can reply to messages directly if you have a message object
    # await message.reply('Cool!')
    #
    # # Or send files, songs, documents, albums...
    # await client.send_file('me', '/home/me/Pictures/holidays.jpg')
    #
    # # You can print the message history of any chat:
    # async for message in client.iter_messages('me'):
    #     print(message.id, message.text)
    #
    #     # You can download media from messages, too!
    #     # The method will return the path where the file was saved.
    #     if message.photo:
    #         path = await message.download_media()
    #         print('File saved to', path)  # printed after download is done

# with client:
#     client.loop.run_until_complete(main())
#
#
# main()



all_phone_numbers = []
df_apdd = pd.DataFrame()

# Create a client instance
client = TelegramClient(username, api_id, api_hash)
# import cv2
import re
import csv
async def main():
    try:
        # Connect to Telegram
        await client.start()
        print("Client connected successfully")

        # Resolve the group entity
        entity = await client.get_entity(group_username)

        # Get the history of the group chat
        messages = await client(GetHistoryRequest(
            peer=entity,
            limit=10,  # Limit defines the number of messages to retrieve
            offset_date=None,
            offset_id=0,
            max_id=0,
            min_id=0,
            add_offset=0,
            hash=0
        ))
        result = ""
        # Print messages to console
        for msg in messages.messages:
            result += (msg.message or "") + "\n"

        # print( result)

        phone_numbers = re.findall(r'\b\d{10}\b',result)

        # Convert to integers
        phone_numbers_int = [int(number) for number in phone_numbers]

        # # Find all mobile numbers in the text
        # mobile_numbers = re.findall(mobile_number_pattern, result)
        all_phone_numbers.extend(phone_numbers_int)
        data = {'DIAMOND_WORKERS_UNION': all_phone_numbers}


        df = pd.DataFrame(data)
        df = df.drop_duplicates(subset=list(data.keys())[0], keep='last')
        df.reset_index()
        # print(df)

        # breakpoint()

        telegram_phone_numbers_csv_read = pd.DataFrame(pd.read_csv("telegram_phone_numbers.csv", on_bad_lines='skip'))
        Unnamed = telegram_phone_numbers_csv_read.loc[:, ~ telegram_phone_numbers_csv_read.columns.str.contains('^Unnamed')]


        df2 = pd.DataFrame(Unnamed)    # print(df)

        df = pd.concat([df, df2], ignore_index=True)
        print(df)

        df = df.drop_duplicates(subset=list(df.keys())[0], keep='last')
        # df.drop_duplicates(subset='DIAMOND_WORKERS_UNION', keep=False, inplace=True)    duplicates 'last'
        df.reset_index()



        print(df)

        df.to_csv('telegram_phone_numbers.csv')



    except SessionPasswordNeededError:
        print('Telegram account with 2FA enabled. Please enter your password.')
        client.run_until_disconnected()

import datetime
import time


start_time = datetime.time(1,15)  # 9:15 AM
qroff_time = datetime.time(23,59)  # 3:15 PM
end_time = datetime.time(23,59)   # 3:30 PM

while start_time <= datetime.datetime.now().time() < end_time:


      # Run the main function
      with client:
       client.loop.run_until_complete(main())
       time.sleep(1*60)