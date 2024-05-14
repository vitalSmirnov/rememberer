from Gspread.gspread import Gspread
from static.utils import scheduler
from Bot.bot import app

if __name__ == "__main__":

    sheets = Gspread(
        app
    )
    # scheduler.add_job(sheets.monitoring, "cron", hour=00, minute=00)
    scheduler.add_job(sheets.monitoring, "interval", seconds=90)
    scheduler.start()

    try:
        app.run()
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
