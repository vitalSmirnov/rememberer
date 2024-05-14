import gspread
from datetime import date, timedelta
from pyrogram import Client
from Bot.bot import check_commands


class Gspread:
    gc = None
    bot_instance = None

    def __init__(self, bot: Client):
        self.bot_instance = bot
        self.gc = gspread.oauth(
            credentials_filename='credentials.json',
            authorized_user_filename='authorized_user.json'
        )

    def get_table(self):
        sheet = self.gc.open('Rememberer')
        return sheet.sheet1.get_all_records()

    def check_birthdays(self, next_birthday_date, prev_birthday_date):
        return_value = []
        table = self.get_table()

        for row in table:
            if row['date'] == str(next_birthday_date):
                return_value.append(['next', row])
            if row['date'] == str(prev_birthday_date):
                return_value.append(['next', row])

        return return_value

    def monitoring(self):
        next_birthday_date = date.today() + timedelta(days=14)
        prev_birthday_date = date.today() + timedelta(days=-2)
        commands = self.check_birthdays(next_birthday_date, prev_birthday_date)
        check_commands(commands)
