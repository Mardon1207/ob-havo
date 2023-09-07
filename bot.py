from dotenv import load_dotenv
import os
from telegram.ext import(
    Updater,
    Dispatcher,
    CommandHandler,
    filters,
    MessageHandler,
    CallbackQueryHandler,
)
from handlers import(
    start
)
load_dotenv()
TOKEN = os.getenv("TOKEN")
API_KEY=os.getenv("API_KEY")

# create updater object
updater: Updater = Updater(token=TOKEN)

# create dispatcher object
dispatcher: Dispatcher = updater.dispatcher
# create main function
def main():
    # add the handlers
    dispatcher.add_handler(handler=CommandHandler(command="start",callback=start))

    #start the bot
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()