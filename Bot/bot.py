from pyrogram import filters, Client
from pyrogram.raw import functions
from static.config import BOT_TOKEN, API_HASH, API_ID, GROUP_ID
from pyrogram.raw.types import InputPeerChat

app = Client(
    "bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    in_memory=False,
)


async def next_birthday_scenario(birthday_id, group_link):
    async for user in app.get_chat_members(chat_id=GROUP_ID, limit=0):
        print(user, 'users')
        if birthday_id != user.user.id and not user.user.is_bot:
            await send_remember(user.user, group_link)


# async def clear_history(chat_id):
#     peer_id = InputPeerChat(chat_id=chat_id)
#     await app.invoke(
#         functions.messages.DeleteHistory(peer=peer_id, revoke=True, max_id=0)
#     )


async def check_commands(commands):
    print(commands, 'commands')
    if not commands:
        return
    else:
        for command in commands:
            print(command, 'command')
            if command[0] == 'next':
                await next_birthday_scenario(int(command[1]['tg id']), command[1]['group link'])
            if command[0] == 'prev':
                return
                # await clear_history(command[1]['group id'])

    return


async def send_remember(user, chat_link):
    await app.send_message(
        user.id,
        f"Скоро у [{user.first_name}](tg://user?id={user.id}) день рождения - вот ссылка на чат {chat_link}",
    )


@app.on_message(filters.command(['start']))
async def start(_, message):
    print(message)
    await app.send_message(
        chat_id=message.from_user.id,
        text='Спасибо за то, что написали! Это бот для уведомлений '
             'о днях рождения, который будет присылать напоминания за 2 недели'
    )
